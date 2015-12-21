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
            "format": "email",
            "messages": {
                "type": "E-mail needs to be string type.",
                "format": "E-mail is in wrong format."
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
