============
django-cufon
============

Easy Cufon with Django.  Django-cufon provides easy-to-use template tags for use with rendering Cufon text in your
HTML with Django.

It provides:

* A tag named ``{% cufon-script %}`` that includes the Cufon JavaScripts.  This is meant to be put in ``HEAD``.
* A tag named ``{% cufon %}`` that handles rendering your Cufon texts.


Example
=======

In your ``HEAD`` be sure to include the Cufon scripts and your fonts::

    {% load cufon %}
    <html>
    <head>
        <title>My awesome page</title>
        {% cufon-script %}
        <script language="text/javascript" src="{{ STATIC_URL }}fonts/my_cufon_font.js"></script>
        [...]

Then, in your body where you want to Cufon some text::

    <h1>{% cufon "All your base are belong to us!" "MyAwesomeFont" %}</h1>

The above example will render the text ``All your base are belong to us!`` in the Cufon font called ``MyAwesomeFont``

Contents
========

.. toctree::
    :maxdepth: 2


Contribution
============

If you find this software useful, please feel welcome and encouraged
to contribute with bug fixes, documentation or new features.

GitHub project: `http://github.com/JonnyFunFun/django-cufon
<http://github.com/JonnyFunFun/django-cufon>`_

License
=======

This software is made available as-is under the GNU General Public License.

django-cufon is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

django-cufon is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with django-cufon.  If not, see `http://www.gnu.org/licenses/<http://www.gnu.org/licenses/>`_.

Authors & Special Thanks
========================

django-cufon was written by `Jonathan Enzinna`_

Many special thanks to `Simo Kinnunen`_ for creating `Cufon`_ in the first place.

.. _`Jonathan Enzinna`: https://github.com/JonnyFunFun
.. _`Simo Kinnunen`: https://twitter.com/sorccu
.. _`Cufon`: http://cufon.shoqolate.com/generate/