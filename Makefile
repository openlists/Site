# Makefile for the OpenLists site

##########################################################################
## VARIABLES
#
ORG 	    = https://github.com/OpenLists
SITE        = openlists.github.io
OUTPUTS     = outputs
DOCS        = docs


##########################################################################
## PREPARE SITE

prepare:

	python prep_site.py


##########################################################################
## CLEAN UPS

clear:

	rm -rf $(OUTPUTS)/
	mkdir $(OUTPUTS)


##########################################################################
## DEPLOY SITE

deploy:

	# Clone the website host repository
	git clone --depth 1 $(ORG)/$(SITE)

	# Copy in the website files & processed pages
	cp $(DOCS)/* $(SITE)/
	cp $(OUTPUTS)/* $(SITE)/

	# Push the update from the host repository
	cd $(SITE)
	git add *
	git commit -m 'deploy site'
	git push
	cd ..

	# Clear out the site repo
	rm -rf $(SITE)