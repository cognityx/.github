from pathlib import Path

import yaml


ROOT = Path(__file__).parents[1]


def test_all_workflow_yaml_is_parseable() -> None:
    workflow_paths = sorted((ROOT / ".github" / "workflows").glob("*.yml"))
    template_paths = sorted((ROOT / "workflow-templates").glob("*.yml"))

    assert workflow_paths
    assert template_paths
    for path in workflow_paths + template_paths:
        assert isinstance(yaml.safe_load(path.read_text(encoding="utf-8")), dict)


def test_reusable_ci_runs_unrestricted_pytest_discovery() -> None:
    workflow = (
        ROOT / ".github" / "workflows" / "python-package-ci.yml"
    ).read_text(encoding="utf-8")

    assert "uv run pytest" in workflow
    assert "uv run pytest tests/" not in workflow
    assert "install-all-extras" in workflow


def test_repository_templates_target_main_and_publish_docs() -> None:
    ci_template = (
        ROOT / "workflow-templates" / "cognityx-python-ci.yml"
    ).read_text(encoding="utf-8")
    docs_template = (
        ROOT / "workflow-templates" / "publish-cognityx-docs.yml"
    ).read_text(encoding="utf-8")

    assert "pull_request:" in ci_template
    assert "branches:\n      - main" in ci_template
    assert "branches: [main]" in docs_template
    assert "event_type=documentation-updated" in docs_template
