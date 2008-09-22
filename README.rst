=========================
Cachebuster Template Tags
=========================

Just that.  Use the cachebuster tag_helpers to ensure the browswers are not caching your css or javascript edits.
Using the template tags will return a full css or javascript tag with the filename and a sha1 string appended based on the name of the file and the edit date of the file.  When the file is changed the hash is also updated.

**Usage**

Load the tag

::
  
  {% load tag_helper %}


Javascript

::

  {% js_tag "jquery.js" %} or {% js_tag "jquery" %}
  
  will return

  <script src="/site_media/jquery.js?e90301f912ab5c1b72d6422aa690d76c1cbff357" type="text/javascript"></script> 
  

CSS

::

  {% css_tag "base.css" %} or {% css_tag "base" %}
 
   will return
  
  <link rel="stylesheet" href="/site_media/base.css?aa3117fb84ed9fddcd93ba62e459bf2211262ae4" />
 


