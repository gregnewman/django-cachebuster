""" 
This will return the filename with the cachebuster apppended 

Useage::
    {% js_tag 'test.js' %}
        or 
    {% js_tag 'test' %}

Returns::
    test.js?188a8a2c905fac2670ec4b254d40dadcc7f93f7a

    Author: Greg Newman > greg@20seven.org
"""
from django import template
import hashlib
import time
import datetime
import os

def _cleanfilename(filename):
    
    return os.path.splitext(filename)[0]

def _hashit(filename):
    cb = hashlib.sha1()
    cb.update(filename)
    cb.update(str(datetime.datetime.now()))
    
    return str(cb.hexdigest())

def js_tag(filename):
    f = _cleanfilename(filename)

    return f + ".js?" + _hashit(f)

def css_tag(filename):
    f = _cleanfilename(filename)

    return f + ".css?" + _hashit(f)

register = template.Library()
register.simple_tag(js_tag)
register.simple_tag(css_tag)
