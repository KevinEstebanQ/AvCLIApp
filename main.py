
from db.init_db import init_db
from data_import.batch_import import import_from_csv
from pathlib import Path
import csv
from db.seed import seed_assignment_types
from crud.read_db import show_per_role
from app_logging import AppLogger
import click


logger = AppLogger().get_logger()
@click.group()
def cli():
    init_db()
    logger.info("db initialized")
    seed_assignment_types()
    logger.info("db seeded")

@cli.command()
@click.option('--filename', required=False,
               help="path to the filename in data_import directory")
def process(filename):
    """ process a file to update the database """
    path: Path
    if filename:
        path = Path(filename).resolve()
        if not path.is_file:
            click.echo("file does not exist")
            logger.error("file does not exits")
        else:
            import_from_csv(path)
            
    else: 
        path = Path(__file__).resolve().parent / "data_import"
        path_dir: dict[int, Path] = dict()
        count=0
        for f in path.iterdir():
            path_dir[count] = f
            count+=1
        for k,v in path_dir.items():
            click.echo(f"{k} --- {"".join(v.as_posix().split("/")[-1])}")
        selection = click.prompt("select (1,2,3, etc..) the csv file to parse...", type=int)
        selected_path = path_dir.get(selection, None)
        if not selected_path:
            click.echo("incorrect option")
            logger.error("incorrect path selected")
        else:
            import_from_csv(selected_path)

        
if __name__ == "__main__":
    cli()
