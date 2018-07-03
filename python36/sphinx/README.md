# Sphinx API Documentation

Minimum knowledge to get started with Sphinx document generation.

```commandline
pipenv install sphinx
```

# PyCharm Run Configuration
If you are going to setup a sphinx run configuration in pycharm.
Make the following changes to ~/pycharm-2018.1.3/helpers/rest_runners/sphinx_runner.py.  Sphinx changed their
commandline format a bit and this change is required to get it to run.

```python

__author__ = 'catherine'

# if __name__ == "__main__":
#   try:
#     from sphinx import cmdline
#   except:
#     raise NameError("Cannot find sphinx in selected interpreter.")
# 
#   import sys
#   cmdline.main(sys.argv)

if __name__ == '__main__':
    try:
        from sphinx.cmd import build
    except:
        raise NameError("Cannot find sphinx in selected interpreter.")
    
    import sys
    build.main(sys.argv[1:])
```

## sphinx-apidoc
sphinx-apidoc crawls you source tree and creates the appropriate .rst files that reference your modules
for sphinx to build your API documentation.  
[sphinx-apidoc documentation](http://www.sphinx-doc.org/en/1.5/man/sphinx-apidoc.html)

```commandline
sphinx-apidoc --force --separate -a -o docs/source app
```
* --force: Overwrite files
* --separate: Each module gets its own page
* -a: Append to sys.path to enable finding the modules
* -o: Directory to output .rst stubs

Run this from the root of your project.  In the above example it will search the module hierarchy in app.

## sphinx-quickstart
Switch to docs/source the output directory created by sphinx-apidoc.  
```commandline
sphinx-quickstart

Defaults on everything except:
* Project name:
* Author name(s):
* Project relase []:

* autodoc: y
* todo: y
```

###conf.py
This is the configuration file for Sphinx.  Uncomment and update the path to the modules directory.

```python
import os
import sys
sys.path.insert(0, os.path.abspath('../../app'))
```

###index.rst
This is the top level page for the generated API documentation.  
```commandline
.. Vehicle documentation master file, created by
   sphinx-quickstart on Tue Jul  3 07:53:11 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Vehicle's documentation!
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

Add the modules line to get all of the modules in the app directory included in the table of contents.  

###modules.rst
```commandline
app
===

.. toctree::
   :maxdepth: 4

   vehicle
```
 

###vehicle.rst
```commandline
vehicle package
===============

Submodules
----------

.. toctree::

   vehicle.base_vehicle
   vehicle.truck

Module contents
---------------

.. automodule:: vehicle
    :members:
    :undoc-members:
    :show-inheritance:
```

This file is the start of the guts that makes Sphinx work.  The toctree directive points to the submodules in 
the vehicle module.  The automodule directive generates the documentation for the module.  In this case
there is no module documentation.   

###vehicle.base_vehicle.rst
```commandline
vehicle.base\_vehicle module
============================

.. automodule:: vehicle.base_vehicle
    :members:
    :undoc-members:
    :show-inheritance:
```
Here again the automodule directive generates the documentation for the base_vehicle module.

##Generate the documents
Leverage the makefile to clean and build the documents.
```commandline
make clean
make html
```

##Documentaiton
The documentation is generated in _build/html/index.html.  Load this file and poke around at he generated
documentation.
