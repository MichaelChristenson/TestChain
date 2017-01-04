from seaborn.test.standard_import import *
from .test_chain import TestChainMeta
from . import TestChain

if sys.version_info[0] == 2:
    class TestChainExample(TestChain):
        __metaclass__ = TestChainMeta
        def test_raise_exception(self):
            raise Exception("Raising Exception")
        def test_skip_if_sub_test_fails(self):
            """ This should be skipped to show how sub testing failures are skipped """
            self.test_raise_exception()
elif sys.version_info[0] == 3:
    class TestChainExample(TestChain):
        def test_raise_exception(self):
            raise Exception("Raising Exception")

        def test_skip_if_sub_test_fails(self):
            """ This should be skipped to show how sub testing failures are skipped """
            self.test_raise_exception()
