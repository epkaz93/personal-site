workdir = $(shell pwd)

build: build-templates build-media

build-templates:
	python3 build.py

build-media:
	cp -rf media www/

deploy-test:
	docker run --rm --name test-personal-site -v $(workdir)/www:/usr/local/apache2/htdocs/ -p 8080:80 httpd
