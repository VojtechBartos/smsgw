# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

schema = {
    "description": "Schema for the tag POST endpoint",
    "type": "object",
    "method": "POST",
    "required": ["label"],
    "additionalProperties": False, 
    "properties": {
        "label": {
            "type": "string",
            "minLength": 3,
            "maxLength": 32,
        },
        "note": {            
            "type": ["string", "null"],
            "maxLanegth": 255
        }
    }
}