# -*- coding: utf-8 -*-
"""
A command-line interface for running Jupyter Notebooks.

Usage: run.py [OPTIONS] [NOTEBOOK_PATHS]...

    Executes Jupyter Notebooks from the command line.

    Expects one or more file paths input as arguments.

    Errors are raised and printed to the console.

    Example:

        $ python run.py ./src/notebooks.ipynb
    
    Options:
        --help  Show this message and exit.
"""
import os
import click
import pathlib
import nbformat
from nbclient import NotebookClient
from nbconvert.preprocessors import CellExecutionError


@click.command()
@click.argument('notebook_paths', nargs=-1, type=click.Path(exists=True))
def main(notebook_paths):
    """
    Executes Jupyter Notebooks from the command line.

    Expects one or more file paths input as arguments.

    Errors are raised and printed to the console.

    Example:

        $ python run.py ./src/notebooks.ipynb
    """
    for path_string in notebook_paths:
        click.echo(f"🐍🗒️  {path_string}")
        
        # Get the file name
        name = path_string.replace(".ipynb", "")

        # Get its parent directory so we can add it to the $PATH
        path = pathlib.Path(path_string).parent.absolute()

        # Set the intput and output file paths
        input_path = f"{name}.ipynb"
        output_path = f"{name}-output.ipynb"

        # Open up the notebook we're going to run
        with open(input_path) as f:
            nb = nbformat.read(f, as_version=4)

        # Configure nbclient to run the notebook
        client = NotebookClient(
            # What we want it to run
            nb,
            timeout=600,
            kernel_name='python3',
            # We want to allow errors so it doesn't fail silently
            allow_errors=False,
            force_raise_errors=True,
            # Here's where the path gets set
            resources={'metadata': {'path': path}}
        )
        try:
            # Run it
            client.execute()
        except CellExecutionError:
            # If there's an error, print it to the terminal.
            msg = f"Error executing {input_path}.\n See {output_path} for the traceback."
            click.echo(msg)
            # And then raise it too
            raise
        finally:
            # Once all that's done, write out the output notebook to the filesystem
            with open(output_path, mode='w', encoding='utf-8') as f:
                nbformat.write(nb, f)
        

if __name__ == '__main__':
    main()
