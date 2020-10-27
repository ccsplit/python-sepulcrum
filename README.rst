========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |master_workflow| |multi_python|
        | |requires| |codecov|
    * - package
      - | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-sepulcrum/badge/?style=flat
    :target: https://readthedocs.org/projects/python-sepulcrum
    :alt: Documentation Status

.. |master_workflow| image:: https://github.com/ccsplit/python-sepulcrum/workflows/Python%20Master%20Workflow/badge.svg
    :alt: Python Coverage Build Status

.. |multi_python| image:: https://github.com/ccsplit/python-sepulcrum/workflows/Python%20package/badge.svg
    :alt: Multiple Python Tests Build

.. |requires| image:: https://requires.io/github/ccsplit/python-sepulcrum/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/ccsplit/python-sepulcrum/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/ccsplit/python-sepulcrum/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/ccsplit/python-sepulcrum

.. |commits-since| image:: https://img.shields.io/github/commits-since/ccsplit/python-sepulcrum/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/ccsplit/python-sepulcrum/compare/v0.0.0...master


.. end-badges

A collection of tools and scripts used in various python projects.

* Free software: MIT license

Installation
============

::

    python setup.py install

Documentation
=============


https://python-sepulcrum.readthedocs.io/en/latest/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
