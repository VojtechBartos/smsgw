# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import multiprocessing


# setting up address, port, name of app and number of workers
bind = '0.0.0.0:5000'
name = 'smsgw'
workers = multiprocessing.cpu_count() * 2 + 1
proc_name = 'smsgw'
