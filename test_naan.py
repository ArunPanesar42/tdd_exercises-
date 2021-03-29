

from naan_factory import run_factory
import unittest

class makeNaanTest(unittest.TestCase):
    naanf = run_factory()

    def test_make_dough(self):
        self.assertEqual(self.naanf.make_dough("water", "flour"), "dough")

    def test_bake_dough(self):
        self.assertEqual(self.naanf.bake_dough("dough"), "naan")
