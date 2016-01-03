# SMS gateway App and API
[![Circle CI](https://circleci.com/gh/VojtechBartos/smsgw/tree/master.svg?style=svg)](https://circleci.com/gh/VojtechBartos/smsgw/tree/master)
[![Dependency Status](https://david-dm.org/VojtechBartos/smsgw.png)](https://david-dm.org/VojtechBartos/smsgw) [![devDependency Status](https://david-dm.org/VojtechBartos/smsgw/dev-status.png)](https://david-dm.org/VojtechBartos/smsgw#info=devDependencies)

master thesis **IN DEVELOPMENT**

## Provisioning new machine

1. Prepare new machine with SSH access. You need to have IP address and user
2. Copy sample host file
  - `cp provisioning/hosts.sample provisioning/hosts`
3. Update host file with SSH user, IP address of machine and domain/hostname in `provisioning/hosts`
4. Copy sample vars file
  - `cp provisioning/roles/smsgw/vars/main.yml.sample provisioning/roles/smsgw/vars/main.yml`
5. Update variables with real values in `provisioning/roles/smsgw/vars/main.yml`
6. Run ansible provisioning
  - `ansible-playbook provisioning/machine.yml -i provisioning/hosts -vvvv`
7. Access page on set up domain
8. It works!

## TODO's

- Better tests coverage
- Packages
  - upgrade `react-router`
  - upgrade `react-tagsinput`
- Functionality
  - verifying passwords during change in settings and admin page
- DevOps
  - write installation steps
  - build image on CircleCI and pushing to Docker Hub
  - after success push to Docker Hub run ansible provisioning script to deploy and update server
