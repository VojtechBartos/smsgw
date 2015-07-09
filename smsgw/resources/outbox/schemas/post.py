# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.resources import patterns

schema = {
    "description": "Schema for the outbox POST endpoint",
    "type": "object",
    "method": "POST",
    "required": ["message", "phoneNumber"],
    "additionalProperties": False,
    "properties": {
        "message": {
            "type": "string",
            "format": "email",
            "minLength": 1
        },
        "phoneNumber": {
            "type": "string",
            "pattern": patterns.PHONE_NUMBER
        }
    }
}
