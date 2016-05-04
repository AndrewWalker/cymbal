cymbol
======

**cymbol adds functionality missing from the python libclang bindings**

This project builds on the work of the LLVM team and the University of Illinois
at Urbana-Champaign, but is no way affiliated with either group.

|license| |build| |coverage|

Usage
-----

Import libclang as normal, optionally configuring the path to the libclang
shared-library, then import cymbal and apply the monkey patches.

.. code:: python

    import clang.cindex
    
    # optionally 
    clang.cindex.conf.set_library_file('/path/to/libclang')

    import cymbal
    cymbal.monkey_patch()

Once the monkey patches have been applied, additional methods will be
available. For, the python libclang bindings omit functions to enumerate class
template arguments that cymbal injects. 

.. code:: python

    idx = clang.cindex.Index.create()
    tu = idx.parse('sample.cpp', args=['-std=c++11']) 
    for cursor in tu.cursor.walk_preorder():
        class_type = cursor.type
        cnt = class_type.get_num_template_arguments()
        for i in range(cnt):
            print(class_type.get_template_argument_type(i))

Installation
------------

Contributing
------------

If you experience problems with cymbal, `log them on GitHub`_. If you
want to contribute code, please `fork the code`_ and `submit a pull request`_.

.. _log them on Github: https://github.com/AndrewWalker/cymbal/issues
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

