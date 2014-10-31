# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

VALID = {
    "email": "vojta@bighealth.com",
    "password": "password",
    "firstName": "Vojta",
    "lastName": "Bartos",
    "company": "BigHealht.com"
}

VALID_NO_COMPANY = {
    "email": "vojta+nocompany@bighealth.com",
    "password": "password",
    "firstName": "Vojta",
    "lastName": "Bartos"
}

NO_PASSWORD = {
    "email": "vojta+nopassword@bighealth.com",
    "firstName": "Vojta",
    "lastName": "Bartos"
}

NO_EMAIL = {
    "password": "password",
    "firstName": "Vojta",
    "lastName": "Bartos",
    "company": "BigHealht.com"
}

LONG_NAMES = {
    "email": "vojta@bighealth.com",
    "password": "password",
    "firstName": "Vojta more than 16 characters",
    "lastName": "Bartos more than 16 characters",
    "company": "BigHealht.com"
}
