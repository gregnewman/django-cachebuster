""" 
returns the tagged filename with the cachebuster apppended 
example: js_tag('test.js') or js_tag('test')
>>> test.js?188a8a2c905fac2670ec4b254d40dadcc7f93f7a

Author: Greg Newman > greg@20seven.org
"""

import hashlib
import time
import datetime
import os

def _hashit(filename):
    cb = hashlib.sha1()
    cb.update(os.path.splitext(filename)[0])
    cb.update(str(datetime.datetime.now()))
    
    return str(cb.hexdigest())

def js_tag(filename):

    return filename + ".js?" + _hashit(filename)

def css_tag(filename):

    return filename + ".css?" + _hashit(filename)


print js_tag("test")
print css_tag("testcss")
