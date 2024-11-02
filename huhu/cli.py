from typing import Annotated, List, Optional

from huhu import __app_name__, __version__, DATABASE
from huhu.huhu import HuhuController

import typer


app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-V",
        help="Mostrar versão do aplicativo.",
        callback=_version_callback,
        is_eager=True,
    ),
) -> None:
    return


@app.command(name="add")
def add(
    humor: int = typer.Argument(..., min=1, max=5),
    description: Annotated[List[str], typer.Argument()] = None,
) -> None:
    """Adicionar novo registro de humor."""

    huhu_controller = HuhuController(DATABASE)
    record = huhu_controller.add_record(humor, description)

    typer.secho(
        f"'{record['humor']}' foi adicionado às {record['datetime']}.",
        fg=typer.colors.GREEN,
    )


@app.command(name="list")
def list_all() -> None:
    """Lista todos os registros de humor."""

    huhu_controller = HuhuController(DATABASE)
    records = huhu_controller.read_records()

    if len(records) > 0:
        typer.secho("ID - HUMOR - DESCRIÇÃO - DATA")
        for record in records:
            typer.secho(
                f"{record.doc_id} - {record['humor']} - {record['description']} - {record['datetime']}"
            )
    else:
        typer.secho(
            "Nenhum registro de humor foi feito ainda.", fg=typer.colors.RED
        )


@app.command(name="get")
def list_one(record_id: int = typer.Argument(...)) -> None:
    """Mostrar registro de humor por id."""

    huhu_controller = HuhuController(DATABASE)
    record = huhu_controller.read_record_by_id(record_id)

    if not record:
        typer.secho("Registro não encontrado.", fg=typer.colors.RED)
        raise typer.Exit(1)
    else:
        typer.secho(
            f'Humor: {record['humor'].capitalize()}\n'
            f'Descrição: {record['description']}\n'
            f'Data: {record['datetime']}'
        )


@app.command(name="remove")
def remove(record_id: int = typer.Argument(...)) -> None:
    """Remove registro de humor por id."""

    huhu_controller = HuhuController(DATABASE)
    record = huhu_controller.remove_record(record_id)

    if not record:
        typer.secho("Registro não encontrado.", fg=typer.colors.RED)
        raise typer.Exit(1)

    typer.secho(f"Registro #{record_id} foi removido.")
