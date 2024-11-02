from typer.testing import CliRunner

from huhu.cli import app


runner = CliRunner()


def test_app_version():
    result = runner.invoke(app, "--version")
    assert result.exit_code == 0
    assert "huhu v0.1.0" in result.stdout


def test_app_add():
    result = runner.invoke(app, ["add", "1", "i wanna die"])
    assert result.exit_code == 0
    assert "foi adicionado às" in result.stdout
