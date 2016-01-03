# SMSGW SMS management system
[![Circle CI](https://circleci.com/gh/VojtechBartos/smsgw/tree/master.svg?style=svg)](https://circleci.com/gh/VojtechBartos/smsgw/tree/master)
[![Dependency Status](https://david-dm.org/VojtechBartos/smsgw.png)](https://david-dm.org/VojtechBartos/smsgw) [![devDependency Status](https://david-dm.org/VojtechBartos/smsgw/dev-status.png)](https://david-dm.org/VojtechBartos/smsgw#info=devDependencies)

SMSGW is open source web-based SMS (Short Message Service) management system, it use gammu-smsd (part of gammu family) as SMS gateway engine to deliver and retrieve messages from your phone/modem.

**NOTICE: still in active development as part of the master thesis**

![SMSGW Dashboard](https://raw.githubusercontent.com/VojtechBartos/smsgw/master/docs/_static/images/screen-dashboard.png "SMSGW Dashboard")

## Requirements

- [docker](https://github.com/docker/docker) >= 1.9.0
- [docker-compose](https://github.com/docker/compose) >= 1.5.2
- for deployment and provisioning
  - [ansible](http://www.ansible.com/) >= 1.8.2
- for development
  - [node.js](https://nodejs.org/en/) >= 5.1.0
  - [gulp](https://www.npmjs.com/package/gulp) >= 3.9.0
    - `npm install -g gulp`

## Getting started

```sh
# cloning repository
git clone git@github.com:VojtechBartos/smsgw.git
cd smsgw

# creating .env file with environment variables and replacing placeholders
cp .env.sample .env
vim .env

# running app
make dev # for dev environment with container output
# OR
make # for production env in background
```

## Provisioning fresh new server

You need to have prepared fresh new machine with SSH access and IP address

```sh
# copy sample host file
cp provisioning/hosts.sample provisioning/hosts

# update host file with SSH user, IP address and domain/hostname of machine
vim provisioning/hosts

# copy sample vars file for SMSGW project
cp provisioning/roles/smsgw/vars/main.yml.sample provisioning/roles/smsgw/vars/main.yml

# update vars file for SMSGW project with your env variables for production,
# new DB and RabbitMQ will be created
vim provisioning/roles/smsgw/vars/main.yml

# run ansible provisioning which will prepare and start SMSGW project on your machine
make deploy

# open browser on hostname, if your DNS pointing to right machine you should
# see SMSGW sign in page
```

## TODO's

- Documentation
- Better tests coverage
- Packages
  - upgrade `react-router`
  - upgrade `react-tagsinput`
- Functionality
  - ~~verifying passwords during change in settings and admin page~~
- DevOps
  - ~~write installation steps~~
  - build image on CircleCI and pushing to Docker Hub [via rarous](https://github.com/rarous/rarousnet/blob/master/circle.yml)
  - after success push to Docker Hub run ansible provisioning script to deploy and update server
