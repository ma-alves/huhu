from typing import Annotated, List, Optional

from huhu import __app_name__, __version__, DATABASE
from huhu.huhu import HuhuController

import typer


app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f'{__app_name__} v{__version__}')
        raise typer.Exit()
    

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        '--version',
        '-V',
        help='Display app version.',
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return


@app.command(name='add')
def add(
    humor: int = typer.Argument(..., min=1, max=5),
    description: Annotated[List[str], typer.Argument()] = None,
) -> None:
    '''Add a new humor record to the humor tracker.'''
    
    huhu_controller = HuhuController(DATABASE)
    record = huhu_controller.add_record(humor, description)
    
    typer.secho(
        f"Record '{record['humor']}' was added at {record['datetime']}.",
        fg=typer.colors.GREEN
    )

@app.command(name='list')
def list_all() -> None:
    '''List all humor records.'''

    huhu_controller = HuhuController(DATABASE)
    records = huhu_controller.read_records()

    typer.secho('ID - MOOD - DESCRIPTION - DATETIME')
    for record in records:
        typer.secho(f"{record.doc_id} - {record['humor']} - {record['description']} - {record['datetime']}")


@app.command(name='get')
def list_one(record_id: int = typer.Argument(...)) -> None:
    '''Get humor record by id.'''

    huhu_controller = HuhuController(DATABASE)
    record = huhu_controller.read_record_by_id(record_id)

    if not record:
        typer.secho('Record not found.', fg=typer.colors.RED)
        raise typer.Exit(1)
    else:
        typer.secho(
            f'Humor: {record['humor'].capitalize()}\n'
            f'Description: {record['description']}\n'
            f'Datetime: {record['datetime']}'
        )


@app.command(name='remove')
def remove(record_id: int = typer.Argument(...)) -> None:
    '''Remove humor record by id.'''

    huhu_controller = HuhuController(DATABASE)
    record = huhu_controller.remove_record(record_id)

    if not record:
        typer.secho('Record not found.', fg=typer.colors.RED)
        raise typer.Exit(1)
    
    typer.secho(f'Record #{record_id} was removed.')
