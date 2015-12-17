FROM python:2.7-onbuild
MAINTAINER Vojta Bartos <hi@vojtech.me>

# default necessary packages
RUN \
  apt-get update && \
  apt-get install -y curl && \
  apt-get install -y python && \
  apt-get install -y git-core && \
  apt-get install -y libmysqlclient-dev && \
  apt-get install -y cmake

# installing gammu
RUN \
  mkdir -p /usr/src/gammu && \
  mkdir -p /var/log/gammu && \
  git clone https://github.com/gammu/gammu.git /usr/src/gammu && \
  (cd /usr/src/gammu; git checkout tags/1.34.0 -b 1.34.0) && \
  (cd /usr/src/gammu; ./configure) && \
  (cd /usr/src/gammu; make) && \
  (cd /usr/src/gammu; make install)
# fixing error gammu-smsd: error while loading shared libraries: libGammu.so.7:
# cannot open shared object file: No such file or directory
# http://comments.gmane.org/gmane.linux.drivers.gammu/10260
RUN ldconfig

# nodejs installation for building client-side javascript
RUN \
  curl -sL https://deb.nodesource.com/setup_5.x | bash - && \
  apt-get install -y nodejs && \
  npm install && \
  npm install -g gulp && \
  gulp -e release

# python app port
EXPOSE 5000

# running python app
CMD ["bin/run"]
