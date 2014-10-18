# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import re
from flask import request, abort
from smsgw.models import UserToken

def auth_required(f):
       
    @wraps(f)
    def decorated_function(*args, **kwargs):
        
        auth_header = request.headers.get('Authorization')
        match = re.search('Token ([a-zA-Z0-9]+)', text)
        token_hash = match.group(1) if m else None
        if token_hash is None:
            return abort(401)

        try:
            token = UserToken.query().filter_by(token=token_hash).one()




        except Exception, e:
            return abort(401)
        

        return f(*args, **kwargs)

    return decorated_function
