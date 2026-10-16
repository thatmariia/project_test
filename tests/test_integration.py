"""Integration tests for generated interface adapters."""

import importlib.util
from pathlib import Path

import pytest

from project_test.services.processing import process_text


def test_service_integration_path_processes_text():
    """Ensure the reusable service path behaves consistently."""
    assert process_text("abc").output_text == "ABC"


def test_cli_application_processes_a_command():
    """Ensure the installed CLI surface reaches the service layer."""
    pytest.importorskip("typer")
    from typer.testing import CliRunner

    from project_test.adapters.cli.app import app

    result = CliRunner().invoke(app, ["process", "abc"])

    assert result.exit_code == 0
    assert result.stdout.strip() == "ABC"


def test_example_script_can_run_without_cli_process():
    """Ensure the generated script delegates to package code."""
    script_path = Path(__file__).parents[1] / "scripts" / "run_example.py"
    spec = importlib.util.spec_from_file_location("run_example", script_path)
    assert spec is not None
    assert spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    assert module.process_text("abc").output_text == "ABC"
