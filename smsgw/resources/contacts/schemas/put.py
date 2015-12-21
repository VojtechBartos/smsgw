# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.resources import patterns

schema = {
    "description": "Schema for the contacts PUT endpoint",
    "type": "object",
    "method": "PUT",
    "required": [ "firstName", "lastName", "phoneNumber" ],
    "additionalProperties": False,
    "properties": {
        "firstName": {
            "type": "string",
            "minLength": 2,
            "maxLength": 16,
            "messages": {
                "minLength": "Max length of first name is 2 characters.",
                "maxLength": "Max length of first name is 16 characters."
            }
        },
        "lastName": {
            "type": "string",
            "minLength": 2,
            "maxLength": 16,
            "messages": {
                "minLength": "Max length of last name is 2 characters.",
                "maxLength": "Max length of last name is 16 characters."
            }
        },
        "email": {
            "type": ["string", "null"],
            "pattern": "(%s)?" % patterns.EMAIL,
            "messages": {
                "pattern": "E-mail is in wrong format."
            }
        },
        "phoneNumber": {
            "type": "string",
            "pattern": patterns.PHONE_NUMBER,
            "messages": {
                "type": "Phone number needs to be string.",
                "pattern": "Phone number has invalid format. (+420736202512 as example.)"
            }
        },
        "note": {
            "type": ["string", "null"],
            "maxLength": 255,
            "messages": {
                "maxLength": "Max length of note is 255 characters."
            }
        },
        "tags": {
            "type": ["array", "null"],
            "items": {
                "type": "string",
                "minLength": 1,
                "maxLength": 23
            }
        }
    }
}
