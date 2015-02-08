# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

schema = {
    "description": "Schema for the user PUT endpoint",
    "type": "object",
    "method": "PUT",
    "required": ["email", "firstName", "lastName"],
    "additionalProperties": False,
    "properties": {
        "email": {
            "type": "string",
            "format": "email",
            "maxLength": 128
        },
        "password": {
            "type": "string",
        },
        "firstName": {
            "type": "string",
            "maxLength": 16
        },
        "lastName": {
            "type": "string",
            "maxLength": 16
        },
        "company": {
            "type": ["string", "null"],
            "maxLength": 16
        },
        "password": {
            "type": ["string", "null"]
        }
    }
}
