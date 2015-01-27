# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

VALID = {
    "firstName": "Vojta",
    "lastName": "Bartos",
    "phoneNumber": "+420736202566",
    "email": "vojta@sleepio.com",
    "note": "Note description"
}

UPDATE = {
    "email": None,
    "note": None,
    "firstName": "Vojta",
    "lastName": "Bartos",
    "phoneNumber": "+420736202566"
}

INVALID_EMAIL = {
    "firstName": "Vojta",
    "lastName": "Bartos",
    "phoneNumber": "+420736202566",
    "email": "vojtasleepiocom"
}

INVALID_NUMBER = {
    "firstName": "Vojta",
    "lastName": "Bartos",
    "phoneNumber": "0736202566",
    "email": "vojta@sleepio.com"
}

MISSING_FIELD = {
    "firstName": "Vojta",
    "lastName": "Bartos",
    "email": "vojta@sleepio.com"
}