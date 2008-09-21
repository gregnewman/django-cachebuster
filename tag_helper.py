""" 
returns the javascript filename with a cachebuster apppended 
example: cachebuster_tag(filename_without_extension)
>>> filename_without_extension.js?hash
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

def cbuster_jstag(filename):

    return filename + ".js?" + _hashit(filename)

def cbuster_csstag(filename):

    return filename + ".css?" + _hashit(filename)


print cbuster_jstag("test")
print cbuster_csstag("testcss")
