import click
import nbformat
from nbclient import NotebookClient
from nbconvert.preprocessors import CellExecutionError


@click.group()
def cli():
    pass


def _execute_notebook(path):
    """
    Private method to execute the provided notebook and handle errors.
    """
    with open(path) as f:
        nb = nbformat.read(f, as_version=4)
    client = NotebookClient(
        nb,
        timeout=600,
        kernel_name='python3',
        resources={'metadata': {'path': 'notebooks/'}}
    )
    try:
        client.execute()
    except CellExecutionError:
        out = None
        msg = f'Error executing the notebook "{path}".\n\n'
        msg += f'See notebook "{path}" for the traceback.'
        print(msg)
        raise
    finally:
        with open(path, mode='w', encoding='utf-8') as f:
            nbformat.write(nb, f)


@cli.command()
def examples():
    """
    Run the downloader notebook.
    """
    print("Running examples notebook")
    notebook_filename = './notebooks/examples.ipynb'
    _execute_notebook(notebook_filename)


if __name__ == '__main__':
    cli()