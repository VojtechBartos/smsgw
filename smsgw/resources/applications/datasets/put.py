# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

APPS = [
    {
        'label': 'app 1',
        'prefix': 'abc'
    },
    {
        'label': 'app 2',
        'prefix': 'cba'
    },
    {
        'label': 'app 3',
        'prefix': '123'
    }
]


DUPLICATED_CODE = {
    'label': 'new label',
    'prefix': 'cba'
}

INVALID_LABEL = {
    'label': 'L'
}

INVALID_URL = {
    'label': 'new app',
    'callbackUrl': 'url'
}

INVALID_CODE = {
    'label': 'new app label',
    'prefix': 'c'
}

VALID = {
    'label': 'new app label',
    'prefix': 'KOD',
    'callbackUrl': 'http://github.com'
}