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
            "messages": {
                "type": "E-mail needs to be string type.",
                "pattern": "E-mail is in wrong format."
            }
        },
        "password": {
            "type": "string",
            "messages": {
                "type": "Password needs to be string type.",
            }
        }
    }
}
