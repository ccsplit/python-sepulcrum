========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
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

.. |version| image:: https://img.shields.io/pypi/v/sepulcrum.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/sepulcrum

.. |commits-since| image:: https://img.shields.io/github/commits-since/ccsplit/python-sepulcrum/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/ccsplit/python-sepulcrum/compare/v0.0.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/sepulcrum.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/sepulcrum

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/sepulcrum.svg
    :alt: Supported versions
    :target: https://pypi.org/project/sepulcrum

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/sepulcrum.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/sepulcrum


.. end-badges

A collection of tools and scripts used in various python projects.

* Free software: MIT license

Installation
============

::

    pip install sepulcrum

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
