# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.resources import patterns

schema = {
    "description": "Schema for the application PUT endpoint",
    "type": "object",
    "method": "PUT",
    "additionalProperties": False,
    "properties": {
        "label": {
            "type": "string",
            "minLength": 3,
            "maxLength": 32,
            "messages": {
                "type": "Label needs to be string type",
                "minLength": "Min length of label is 2 characters.",
                "maxLength": "Max length of label is 32 characters."
            }
        },
        "prefix": {
            "type": "string",
            "minLength": 2,
            "maxLength": 5,
            "messages": {
                "minLength": "Min length of prefix is 2 characters.",
                "maxLength": "Max length of prefix is 5 characters."
            }
        },
        "callbackUrl": {
            "type": ["string", "null"],
            "maxLanegth": 128,
            "pattern": "^(%s)?$" % patterns.URL,
            "messages": {
                "pattern": "Callback url should be valid URL.",
                "maxLength": "Max length of callback url is 128 characters."
            }
        },
        "note": {
            "type": ["string", "null"],
            "maxLength": 255,
            "messages": {
                "maxLength": "Max length of note is 255 characters."
            }
        }
    }
}
