# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.resources import patterns

schema = {
    "description": "Schema for the outbox POST external endpoint",
    "type": "object",
    "method": "POST",
    "required": ["message", "phoneNumber"],
    "additionalProperties": False,
    "properties": {
        "message": {
            "type": "string",
            "minLength": 1,
            "messages": {
                "minLength": "Min length of message is 1 character.",
            }
        },
        "phoneNumber": {
            "type": "string",
            "pattern": patterns.PHONE_NUMBER,
            "messages": {
                "type": "Phone number needs to be string.",
                "pattern": "Phone number has invalid format. (+420736202512 as an example.)"
            }
        },
        "send": {
            "type": "string",
            "pattern": patterns.DATE_TIME
        }
    }
}
