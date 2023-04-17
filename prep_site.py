"""Prepare the OpenLists site."""

import os
from pathlib import Path
from copy import deepcopy
from shutil import copyfile

###################################################################################################
###################################################################################################

# Load the list of repositories
with open('repos.txt', 'r') as file:
    TEMP = file.readlines()
TEMP = [line.strip() for line in TEMP]
REPOS = {line.split(',')[0] : line.split(',')[1] for line in TEMP}

# Define the string definitions of commands to use
CLONE_COMMAND = 'git clone https://github.com/openlists/{}'
RM_COMMAND = 'rm -rf {}'

# Define what to add to the files
ADD_LINES = [
    '---\n',
    'title: {}\n',
    'layout: page\n',
    'permalink: /{}/\n',
    '---\n',
    '\n'
]

DROP_LINES = [
    '## List of OpenLists',
    'The collection of OpenLists includes',
    '- [',
    'permalink'
]

# Define output folder
FOLDER = Path('outputs')

###################################################################################################
###################################################################################################

def main():
    """Main function to manage site creation."""

    # Check for and create (if missing) outputs folder
    if not os.path.exists(FOLDER):
        os.mkdir(FOLDER)

    # Process index file
    os.system(CLONE_COMMAND.format('Overview'))
    copyfile(Path('Overview') / 'README.md', FOLDER / 'index.md')
    update_file(FOLDER / 'index.md', ADD_LINES, 'OpenLists')
    drop_lines(FOLDER / 'index.md', DROP_LINES)
    os.system(RM_COMMAND.format('Overview'))

    for label, repo in REPOS.items():

        print('\n', label, repo)

        # Clone the repository
        os.system(CLONE_COMMAND.format(repo))

        # Copy the README file
        copyfile(Path(repo) / 'README.md', FOLDER / (label.lower() + '.md'))

        # Update the markdown file
        update_file(FOLDER / (label.lower() + '.md'), ADD_LINES, label)

        # Delete the cloned repository
        os.system(RM_COMMAND.format(repo))


def update_file(filename, add_lines, label):
    """Helper function to update file contents.

    Parameters
    ----------
    filename : str or Path
        Name of the file to load and update.
    add_lines : list of str
        Lines to add to the file.
    label : str
        Label to add into the header information.
    """

    add_lines = deepcopy(add_lines)

    with open(filename, 'r') as file:
        contents = file.readlines()

    # Drop the first couple lines (title gets added from header info)
    contents = contents[2:]

    # Add in header information
    add_lines[1] = add_lines[1].format(label)
    add_lines[3] = add_lines[3].format(label.lower())

    # Add header lines
    for line in reversed(add_lines):
        contents.insert(0, line)

    with open(filename, 'w') as file:
        file.writelines(contents)


def drop_lines(filename, lines_to_drop):
    """Helper function to drop lines from files.

    Parameters
    ----------
    filename : str or Path
        Name of the file to load and update.
    lines_to_drop : list of str
        Lines to drop from the file.
    """

    with open(filename, 'r') as file:
        contents = file.readlines()

    output = []
    for line in contents:

        dropped = False
        for drop in lines_to_drop:
            if drop in line:
                dropped = True
                break
        if not dropped:
            output.append(line)

    with open(filename, 'w') as file:
        file.writelines(output)


if __name__ == "__main__":
    main()
