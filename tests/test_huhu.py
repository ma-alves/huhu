from typer.testing import CliRunner

from huhu.cli import app


runner = CliRunner(echo_stdin=True)


def test_app_version():
    result = runner.invoke(app, "--version")

    assert result.exit_code == 0
    assert "huhu v0.1.0" in result.stdout


def test_app_add():
    result = runner.invoke(app, ["add", "1", "-d", "tá paia"])

    assert result.exit_code == 0
    assert "'péssimo' foi adicionado às" in result.stdout


def test_app_get():
    result = runner.invoke(app, ["get", "1"])

    assert result.exit_code == 0
    assert "Humor: Péssimo\nDescrição: Tá paia." in result.stdout


def test_app_get_not_found():
    result = runner.invoke(app, ["get", "0"])

    assert result.exit_code == 1
    assert "Registro não encontrado." in result.stdout


def test_app_list():
    result = runner.invoke(app, "list")

    assert result.exit_code == 0
    assert "ID - HUMOR - DATA" in result.stdout


def test_app_list_is_empty():
    runner.invoke(app, "remove-all", input="y\n")
    result = runner.invoke(app, "list")

    assert result.exit_code == 0
    assert "Nenhum registro de humor foi feito ainda." in result.stdout
