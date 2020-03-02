#!/usr/bin/env python3

import unittest
import pytest

class AppTest(unittest.TestCase):
    def test_dummy(self):
        from remote.light.hitachi.ir_a03h import remote
        r = "hoge"
        assert r == "hoge"

#if __name__ == '__main__':
#    unittest.main()
