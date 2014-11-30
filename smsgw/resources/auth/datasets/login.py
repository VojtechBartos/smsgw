# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

USERS = [
    {
        "email": "vojta@bighealth.com",
        "password": "password",
        "isActive": True
    },
    {
        "email": "vojta+2@bighealth.com",
        "password": "password",
        "isActive": True
    },
    {
        "email": "vojtanotactive@bighealth.com",
        "password": "password",
        "isActive": False
    }
]


INVALID_EMAIL_FORMAT = {
    "email": "vojtasleepiocom",
    "password": "a"
}

NO_PASSWORD = {
    "email": "vojta@sleepio.com"
}

VALID = {
    "email": "vojta@bighealth.com",
    "password": "password"
}

INVALID = {
    "email": "vojta@bighealth.com",
    "password": "invalid"
}

NOT_ACTIVE = {
    "email": "vojtanotactive@bighealth.com",
    "password": "password"
}