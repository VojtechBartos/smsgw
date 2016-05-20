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
            "minLength": 1,
            "messages": {
                "minLength": "Min length of message is 1 character.",
            }
        },
        "phoneNumbers": {
            "type": "array",
            "items": {
                "type": "string",
                "pattern": patterns.PHONE_NUMBER,
                "messages": {
                    "type": "Phone number needs to be string.",
                    "pattern": "Phone number has invalid format. (+420736202512 as an example.)"
                }
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
