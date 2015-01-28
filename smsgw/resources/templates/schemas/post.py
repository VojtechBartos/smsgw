# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

schema = {
    "description": "Schema for the templates POST endpoint",
    "type": "object",
    "method": "POST",
    "required": ["label", "text"],
    "additionalProperties": False, 
    "properties": {
        "label": {
            "type": "string",
            "minLength": 8,
            "maxLength": 128,
        },
        "text": {            
            "type": "string",
            "minLength": 8,
            "maxLanegth": 255
        }
    }
}