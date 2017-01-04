from . import TestChain


class TestChainExample(TestChain):
    def test_raise_exception(self):
        raise Exception("Raising Exception")
    def test_skip_if_sub_test_fails(self):
        """ This should be skipped to show how sub testing failures are skipped """
        self.test_raise_exception()

if __name__ == "__main__":
    TestChainExample.main()