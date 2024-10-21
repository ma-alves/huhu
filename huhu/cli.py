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


@app.command()
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
