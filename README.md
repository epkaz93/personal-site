# Personal Website
This repository is a static website generator for my own personal use. It contains everything to generate the website except for _/media_, since that
folder is to big to commit to a public repository.

## Python Requirements
  * jinja2
  * libsass
  * pyyaml

## System Requirements
  * sass
  * GNU Make
  * docker (testing only)
  * httpd docker container (testing only)


## Building
`make build`

## Test Deploying
`make deploy-test`
