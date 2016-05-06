Cymbal
======

Overview
--------

Cymbal makes it easy to add functionality missing from libclang Python bindings

The Clang `libclang python bindings` use `ctypes`_ to invoke functions present
in libclang dynamic library.  In some cases, only a subset of the C functions
are available, because the platform or version specific Python bindings omit
functions.  Cymbal simplfies the process of dynamically adding those methods to
Types and Cursors.

|license| |build| |coverage|

Usage
-----

Import Cymbal, monkeypatch any required functions, adding appropriate ctypes
annotations as necessary. 

.. code:: python

    import clang.cindex
    from clang.cindex import *
    import cymbal
    from ctypes import *

    # add functions omitted from the pip installable clang packages on OSX

    cymbal.monkeypatch_type('get_template_argument_type',
                            'clang_Type_getTemplateArgumentAsType',
                            [Type, c_uint],
                            Type)

    cymbal.monkeypatch_type('get_num_template_arguments',
                            'clang_Type_getNumTemplateArguments',
                            [Type],
                            c_int)


Requirements
------------

The only requirements are libclang and the python bindings for libclang.

Contributing
------------

If you experience problems with Cymbal, `log them on GitHub`_. If you
want to contribute code, please `fork the code`_ and `submit a pull request`_.

Licensing
---------

This project builds on the work of the LLVM team and the University of Illinois
at Urbana-Champaign, but is no way affiliated with either group.

.. _libclang: http://clang.llvm.org/doxygen/group__CINDEX.html
.. _libclang python bindings: https://github.com/llvm-mirror/clang/tree/master/bindings/python
.. _log them on Github: https://github.com/AndrewWalker/cymbal/issues
.. _ctypes: https://docs.python.org/2/library/ctypes.html
.. _fork the code: https://github.com/AndrewWalker/cymbal
.. _submit a pull request: https://github.com/AndrewWalker/cymbal/pulls

.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/andrewwalker/cymbal/master/LICENSE
   :alt: MIT License

.. |build| image:: https://travis-ci.org/AndrewWalker/cymbal.svg?branch=master
   :target: https://travis-ci.org/AndrewWalker/cymbal
   :alt: Continuous Integration

.. |coverage| image:: https://coveralls.io/repos/github/AndrewWalker/cymbal/badge.svg?branch=master
   :target: https://coveralls.io/github/AndrewWalker/cymbal?branch=master
   :alt: Coverage Testing Results

