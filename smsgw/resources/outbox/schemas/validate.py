# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.resources import patterns

schema = {
    "description": "Schema for the outbox POST validate endpoint",
    "type": "object",
    "method": "POST",
    "required": ["phoneNumber"],
    "additionalProperties": False,
    "properties": {
        "phoneNumber": {
            "type": "string",
            "pattern": patterns.PHONE_NUMBER,
            "messages": {
                "type": "Phone number needs to be string.",
                "pattern": "Phone number has invalid format. (+420736202512 as an example.)"
            }
        }
    }
}
