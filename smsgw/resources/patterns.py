# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

EMAIL = "^[_a-z0-9-\+]+(\.[_a-z0-9-\+]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$"
TIME = "^([0-9]|0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])(\ (am|pm|AM|PM|a\.m\.|p\.m\.|A\.M\.|P\.M\.))?$"
DATE = "^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$"
UUID = "[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-" \
       "[0-9a-fA-F]{12}|\@me"
UNIX_TIMESTAMP = "[0-9]+"
TIMEZONE_CODE = "^(([a-zA-Z]+)(\/[a-zA-Z\-\_]+){1,2})|GMT|UTC$"