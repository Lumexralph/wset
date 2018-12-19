import os
from subprocess import call

import click

# to make the function a command line program
@click.command()
# to get arguments passed
@click.argument('directory')
def cli(directory):
    """Example script."""
    default_file_path = '/Users/olumideogundele/Projects/{}'
    new_dir = default_file_path.format(directory)

    click.echo('The directory for the new project is {}'.format(directory))
    os.mkdir(new_dir)
    os.chdir(new_dir)
    call("git init",  shell=True)
    call("code .", shell=True)

    click.echo('The current directory {}'.format(os.getcwd()))


if __name__ == '__main__':
    cli()
