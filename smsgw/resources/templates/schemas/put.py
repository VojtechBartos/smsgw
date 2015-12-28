# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

schema = {
    "description": "Schema for the templates PUT endpoint",
    "type": "object",
    "method": "PUT",
    "required": ["label", "text"],
    "additionalProperties": False,
    "properties": {
        "label": {
            "type": "string",
            "minLength": 8,
            "maxLength": 128,
            "messages": {
                "type": "Label needs to be string type",
                "minLength": "Min length of label is 8 characters.",
                "maxLength": "Max length of label is 128 characters."
            }
        },
        "text": {
            "type": "string",
            "minLength": 8,
            "maxLanegth": 255,
            "messages": {
                "type": "Text needs to be string type",
                "minLength": "Min length of text is 8 characters.",
                "maxLength": "Max length of text is 255 characters."
            }
        }
    }
}
