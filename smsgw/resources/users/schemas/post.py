# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

schema = {
    "description": "Schema for the user POST endpoint",
    "type": "object",
    "method": "POST",
    "required": ["email", "password", "firstName", "lastName"],
    "additionalProperties": False,
    "properties": {
        "email": {
            "type": "string",
            "format": "email",
            "maxLength": 128
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
            "type": "string",
            "maxLength": 16
        },
        "password": {
            "type": "string",
            "minLength": 16
        }
    }
}
