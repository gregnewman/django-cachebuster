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
from django.conf import settings
import hashlib
import time
import datetime
import os
from distutils.dir_util import mkpath


def _cleanfilename(filename):
    
    return os.path.splitext(filename)[0]

def _getfiletime(filename):
    basedir = "%s/" % (settings.MEDIA_ROOT)
    if os.path.exists(basedir + "/" + filename):
        return os.path.getmtime(basedir + "/" + filename)
    else:
        return ""

def _hashit(filename):
    cb = hashlib.sha1()
    cb.update(_cleanfilename(filename))
    cb.update(str(_getfiletime(filename)))
    
    return str(cb.hexdigest())

def js_tag(filename):
    tag = "<script src=\"%s%s/\" type=\"text/javascript\"></script>" % (settings.MEDIA_URL, _cleanfilename(filename) + ".js?" + _hashit(filename))
    
    return tag 

def css_tag(filename):
    tag = "<link rel=\"stylesheet\" href=\"%s%s\" />" % (settings.MEDIA_URL, _cleanfilename(filename) + ".css?" + _hashit(filename))

    return tag

register = template.Library()
register.simple_tag(js_tag)
register.simple_tag(css_tag)


