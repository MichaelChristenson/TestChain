from test_chain import *
if sys.version_info[0] == 2:
    from python2_example import TestChainMeta as TestChainMeta
elif sys.version_info[0] == 3:
    from python3_example import TestChainMeta as TestChainMeta