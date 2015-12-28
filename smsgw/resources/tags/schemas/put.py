# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

schema = {
    "description": "Schema for the tag PUT endpoint",
    "type": "object",
    "method": "PUT",
    "required": ["label"],
    "additionalProperties": False,
    "properties": {
        "label": {
            "type": "string",
            "minLength": 3,
            "maxLength": 32,
            "messages": {
                "type": "Label needs to be string type",
                "minLength": "Min length of label is 2 characters.",
                "maxLength": "Max length of label is 32 characters."
            }
        },
        "note": {
            "type": ["string", "null"],
            "maxLanegth": 255,
            "messages": {
                "maxLength": "Max length of note is 255 characters."
            }
        }
    }
}
