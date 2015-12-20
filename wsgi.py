#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
