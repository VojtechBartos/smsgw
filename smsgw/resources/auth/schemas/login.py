# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.resources import patterns


schema = {
    "description": "Schema for the auth login POST endpoint",
    "type": "object",
    "method": "POST",
    "required": ["email", "password"],
    "additionalProperties": False, 
    "properties": {
        "email": {
            "type": "string",
            "pattern": patterns.EMAIL,
            "message": "Email does not have right format."
        },
        "password": {
            "type": "string"
        }
    }
}