# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.resources import patterns

schema = {
    "description": "Schema for the outbox POST endpoint",
    "type": "object",
    "method": "POST",
    "required": ["message"],
    "additionalProperties": False,
    "properties": {
        "message": {
            "type": "string",
            "format": "email",
            "minLength": 1
        },
        "phoneNumbers": {
            "type": "array",
            "items": {
                "type": "string",
                "pattern": patterns.PHONE_NUMBER
            }
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "string",
                "pattern": patterns.UUID
            }
        },
        "contacts": {
            "type": "array",
            "items": {
                "type": "string",
                "pattern": patterns.UUID
            }
        },
        "send": {
            "type": "string",
            "pattern": patterns.DATE_TIME_SECONDS
        }
    }
}
