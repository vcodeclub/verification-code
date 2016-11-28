# -*- coding: utf-8 -*-

import vcode


class TestVerificationCodeCommands(object):

    def test_digits(self):
        # Common
        code = vcode.digits()
        assert isinstance(code, str)
        assert len(code) == 6
        # NDigits
        code = vcode.digits(ndigits=4)
        assert isinstance(code, str)
        assert len(code) == 4
        # CodeCastFunc
        code = vcode.digits(code_cast_func=int)
        assert isinstance(code, int)
