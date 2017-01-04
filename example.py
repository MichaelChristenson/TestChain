from seaborn.test.standard_import import *
from .test_chain import TestChainMeta

if sys.version_info[0] == 2:
    class TestChain(unittest.TestCase):
        __metaclass__ = TestChainMeta

    class TestChainExample2(TestChain):
        __metaclass__ = TestChainMeta
        def test_raise_exception(self):
            raise Exception("Raising Exception")
        def test_skip_if_sub_test_fails(self):
            """ This should be skipped to show how sub testing failures are skipped """
            self.test_raise_exception()
elif sys.version_info[0] == 3:
    class TestChain(unittest.TestCase, metaclass=TestChainMeta):
        """
        Creates an instance of a testChain class for easy implementation through extension
        This particular instance is created in the syntax of Python 3.5 to account for slight
        variations in the use of metaclasses between versions
        """
    class TestChainExample3(TestChain):
        def test_raise_exception(self):
            raise Exception("Raising Exception")

        def test_skip_if_sub_test_fails(self):
            """ This should be skipped to show how sub testing failures are skipped """
            self.test_raise_exception()
