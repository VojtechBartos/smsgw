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
        },
        "note": {            
            "type": ["string", "null"],
            "maxLanegth": 255
        }
    }
}