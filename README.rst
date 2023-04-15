========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/tabular2imageencoder/badge/?style=flat
    :target: https://tabular2imageencoder.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/qiriro/tabular2imageencoder/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/qiriro/tabular2imageencoder/actions

.. |codecov| image:: https://codecov.io/gh/qiriro/tabular2imageencoder/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/qiriro/tabular2imageencoder

.. |version| image:: https://img.shields.io/pypi/v/tabular2imageencoder.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/tabular2imageencoder

.. |wheel| image:: https://img.shields.io/pypi/wheel/tabular2imageencoder.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/tabular2imageencoder

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/tabular2imageencoder.svg
    :alt: Supported versions
    :target: https://pypi.org/project/tabular2imageencoder

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/tabular2imageencoder.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/tabular2imageencoder

.. |commits-since| image:: https://img.shields.io/github/commits-since/qiriro/tabular2imageencoder/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/qiriro/tabular2imageencoder/compare/v0.0.0...main



.. end-badges

Tabular2ImageEncoder implements the latest state-of-the-art algorithms for image construction from tabular data.

* Free software: BSD 2-Clause License

Installation
============

::

    pip install tabular2imageencoder

You can also install the in-development version with::

    pip install https://github.com/qiriro/tabular2imageencoder/archive/main.zip


Documentation
=============


https://tabular2imageencoder.readthedocs.io/


Development
===========

To run all the tests run::

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
