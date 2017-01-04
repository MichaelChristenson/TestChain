from test_chain import *
from example import TestChainMeta as TestChainMeta

if sys.version_info[0] == 2:
    class TestChain(unittest.TestCase):
        __metaclass__ = TestChainMeta

elif sys.version_info[0] == 3:
    class TestChain(unittest.TestCase, metaclass=TestChainMeta):
        """
        Creates an instance of a testChain class for easy implementation through extension
        This particular instance is created in the syntax of Python 3.5 to account for slight
        variations in the use of metaclasses between versions
        """
