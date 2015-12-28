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
            "maxLength": 128,
            "messages": {
                "type": "E-mail needs to be string type.",
                "format": "E-mail is in wrong format.",
                "maxLength": "E-mail is too long."
            }
        },
        "password": {
            "type": ["string", "null"],
            "minLength": 16,
            "messages": {
                "type": "Password needs to be string type.",
                "minLength": "Password is too short. Minimal length is 16 characters."
            }
        },
        "firstName": {
            "type": "string",
            "maxLength": 16,
            "messages": {
                "type": "First name needs to be string type.",
                "maxLength": "First name is too long."
            }
        },
        "lastName": {
            "type": "string",
            "maxLength": 16,
            "messages": {
                "type": "Last name needs to be string type.",
                "maxLength": "Last name is too long."
            }
        },
        "company": {
            "type": ["string", "null"],
            "maxLength": 16,
            "messages": {
                "type": "Company needs to be string type.",
                "maxLength": "Company name is too long."
            }
        },
        "role": {
            "enum": ["user", "admin"],
            "messages": {
                "enum": "Wrong value for user role."
            }
        },
        "isActive": {
            "type": "boolean",
            "messages": {
                "type": "Is Active it should be boolean."
            }
        }
    }
}
