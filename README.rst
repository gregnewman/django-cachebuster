=========================
Cachebuster Template Tags
=========================

Just that.  Use to ensure the browswers are not caching your css or javascript edits.
Using the template tags will return a filename with a sha1 string appended based on the name of the file and the current datetime.

**Usage**

Javascript

::

  {% js_tag "jquery.js" %} or {% js_tag "jquery" %}
  
  will return

  <script src="/site_media/jquery.js?e90301f912ab5c1b72d6422aa690d76c1cbff357/" type="text/javascript"></script> 
  

CSS

::

  {% css_tag "base.css" %} or {% css_tag "base" %}
 
   will return
  
  <link rel="stylesheet" href="/site_media/base.css?aa3117fb84ed9fddcd93ba62e459bf2211262ae4" />
 


**TODO**

Change the time to use the files time instead of system time.
