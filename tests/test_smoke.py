"""Smoke tests for the generated Python package."""

from importlib.metadata import PackageNotFoundError, version

import pytest

from project_test import __version__, process_text
from project_test.main import main


def test_package_has_version():
    """Ensure the package exposes its installed distribution version."""
    try:
        installed_version = version("project-test")
    except PackageNotFoundError:
        installed_version = "0+unknown"

    assert __version__ == installed_version


def test_main_is_callable():
    """Ensure the runtime entry point can be imported."""
    assert callable(main)


def test_library_api_processes_text():
    """Ensure reusable service logic is available from the package API."""
    result = process_text("example")

    assert result.input_text == "example"
    assert result.output_text == "EXAMPLE"


def test_cli_entry_point_imports():
    """Ensure the selected command-line application imports."""
    pytest.importorskip("typer")
    from project_test.adapters.cli.app import app

    assert callable(app)
