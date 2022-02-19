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

# Define output folder
FOLDER = Path('outputs')

###################################################################################################
###################################################################################################

def main():

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


if __name__ == "__main__":
    main()
