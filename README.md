# Site

This repository creates the OpenLists website.

Note that the website content gets pushed to the
[host repository](https://github.com/openlists/openlists.github.io), 
which makes the site available at 
[openlists.github.io](https://openlists.github.io/).

This repository is used to organize and create the site content.
It does so by copying in the content from all the individual list repositories, organizing these files, 
and then deploying this content. This is an automatic process, requiring no manual intervention. 

## Instructions

Creating the website is managed through the `Makefile`.

The following are the key commands for regenerating the website:
- `make prepare`: runs the Python script to clone and organize website content files
- `make deploy`: deploys the website content to the hosting repository

To re-deploy the website, these two commands should be run in order.

## Details

In addition to the Makefile, this repo contains:
- `_config.yml`: the config file for the site, which gets copied over
- `repos.txt`: a list of the OpenLists repositories to process and add
- `prep_site.py`: script for getting and converting website content

Note that an interim folder, `outputs`, is created and used when deploying the website.
