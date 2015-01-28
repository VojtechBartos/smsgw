# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.resources import patterns

schema = {
    "description": "Schema for the application PUT endpoint",
    "type": "object",
    "method": "PUT",
    "additionalProperties": False, 
    "properties": {
        "label": {
            "type": "string",
            "minLength": 3,
            "maxLength": 32
        },
        "prefix": {
            "type": ["string", "null"],
            "minLength": 2,
            "maxLength": 5
        },
        "callbackUrl": {            
            "type": ["string", "null"],
            "maxLanegth": 128,
            "pattern": patterns.URL
        },
        "note": {            
            "type": ["string", "null"],
            "maxLanegth": 255
        }
    }
}