=================
verification-code
=================

Verification Code

Installation
============

::

    pip install vcode


Usage
=====

::

    In [1]: import vcode

    In [2]: vcode.digits()
    Out[2]: '249792'

    In [3]: vcode.digits(ndigits=4)
    Out[3]: '6092'

    In [4]: vcode.digits(code_cast_func=int)
    Out[4]: 997531

