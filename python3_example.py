from seaborn.test.standard_import import *
from .test_chain import TestChainMeta

class TestChain(unittest.TestCase, metaclass=TestChainMeta):
    pass # todo put doc here
class TestChainExample3(TestChain):
    def test_raise_exception(self):
        raise Exception("Raising Exception")

    def test_skip_if_sub_test_fails(self):
        """ This should be skipped to show how sub testing failures are skipped """
        self.test_raise_exception()
