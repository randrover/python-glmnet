Python GLMNET (Fixed Build)
===========================

This is a maintained fork of `civisanalytics/python-glmnet <https://github.com/civisanalytics/python-glmnet>`__,
which was archived in 2024. The original package on PyPI (``glmnet``) can no longer be installed
with modern Python toolchains due to build system issues.

Changes from the original
~~~~~~~~~~~~~~~~~~~~~~~~~

This fork applies **minimal fixes** to restore installability:

- Fixed invalid ``python_requires`` specifier (``>=3.6.*`` → ``>=3.6``)
- Added ``pyproject.toml`` with proper build dependencies (``setuptools<60``, ``numpy<2``)
  to support pip build isolation

No changes were made to the library code itself. All credit goes to the original authors
at `Civis Analytics <https://github.com/civisanalytics>`__.

- Original repository: https://github.com/civisanalytics/python-glmnet (archived)
- Fork repository: https://github.com/randrover/python-glmnet
- License: GPLv2 (same as original)

Installation
------------

.. code:: bash

    pip install python-glmnet-fix

A Fortran compiler is required for building from source.
For Mac users, ``brew install gcc`` will take care of this requirement.

Usage
-----

The import name remains ``glmnet``, same as the original:

.. code:: python

    from glmnet import LogitNet, ElasticNet

    # Regularized Logistic Regression
    m = LogitNet()
    m = m.fit(x, y)
    p = m.predict_proba(x)

    # Regularized Linear Regression
    m = ElasticNet()
    m = m.fit(x, y)
    p = m.predict(x)

The API follows the conventions of
`Scikit-Learn <http://scikit-learn.org/stable/>`__, so it is expected to
work with tools from that ecosystem. Both models accept dense or sparse arrays.

Dependencies
~~~~~~~~~~~~

- numpy
- scikit-learn
- scipy
