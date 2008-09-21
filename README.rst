=========================
Cachebuster Template Tags
=========================

Just that.  Use to ensure the browswers are not caching your css or javascript edits.
Using the template tags will return a filename with a sha1 string appended based on the name of the file and the current datetime.

**Usage**

Javascript

::

  {% js_tag somejsfile.js %} >> somejsfile.js?98960263c918137c7678eae54e689ea7407fc5fe

CSS

::

  {% css_tag somecssfile.js %} >> somecssfile.css?98960263c918137c7678eae54e689ea7407fc5fe


**TODO**

Reduce the length of the sha1 output.  It's a little long for my taste.
