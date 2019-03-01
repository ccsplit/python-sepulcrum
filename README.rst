========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |codecov|
    * - package
      - | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-sepulcrum/badge/?style=flat
    :target: https://readthedocs.org/projects/python-sepulcrum
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/ccsplit/python-sepulcrum.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ccsplit/python-sepulcrum

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ccsplit/python-sepulcrum?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ccsplit/python-sepulcrum

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


https://python-sepulcrum.readthedocs.io/


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
