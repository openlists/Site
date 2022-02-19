# Makefile for the OpenLists site

##########################################################################
## VARIABLES
#
ORG 	    = https://github.com/openlists
SITE        = openlists.github.io
OUTPUTS     = outputs


##########################################################################
## PREPARE SITE

prepare:

	python prep_site.py


##########################################################################
## CLEAN UPS

clear:

	@rm -rf $(OUTPUTS)/
	@mkdir $(OUTPUTS)
	@echo 'Cleared outputs folder'


##########################################################################
## DEPLOY SITE

deploy:

	# Clone the website host repository
	git clone --depth 1 $(ORG)/$(SITE)

	# Copy in the website files & processed pages
	cp _config.yml $(SITE)/
	cp $(OUTPUTS)/* $(SITE)/

	# Push the update from the host repository
	cd $(SITE) && \
	git add * && \
	git commit -m 'deploy site' && \
	git push

	# Clear out the site repo
	rm -rf $(SITE)
