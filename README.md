# SMS gateway App and API
[![Build Status](https://secure.travis-ci.org/VojtechBartos/smsgw.png?branch=master)](http://travis-ci.org/VojtechBartos/smsgw)
[![Dependency Status](https://david-dm.org/VojtechBartos/smsgw.png)](https://david-dm.org/VojtechBartos/smsgw) [![devDependency Status](https://david-dm.org/VojtechBartos/smsgw/dev-status.png)](https://david-dm.org/VojtechBartos/smsgw#info=devDependencies)

master thesis **IN DEVELOPMENT**

## Installation

### Local env with vagrant

#### Dependencies (only if you would like to run it in Vagrant)

1. [Virtual Box with Extension Pack](https://www.virtualbox.org/wiki/Downloads)
2. [Vagrant](https://www.vagrantup.com/)
3. https://forums.virtualbox.org/viewtopic.php?f=6&t=55483#p255997

## Issues

- `gammu-smsd: error while loading shared libraries: libGammu.so.7: cannot open shared object file: No such file or directory`
  - `sudo ldconfig` via [link](http://comments.gmane.org/gmane.linux.drivers.gammu/10260)

## TODO's

- Database
  - `INSERT INTO `gammu` (`id`, `Version`, `Info`) VALUES (NULL, '14', '');`
- React
  - autobinding at the component
- DevOps
  - ~~add vagrant setup~~
  - write installation steps
