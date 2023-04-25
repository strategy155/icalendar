import unittest


class TestPandas(unittest.TestCase):

    def test_pandas_vCategory(self):
        from ..prop import vCategory

        catz = ['cat 1', 'cat 2', 'cat 3']
        v_cat = vCategory(catz)
        print(v_cat.to_pandas())
        self.assertEqual(v_cat.to_ical(), b'cat 1,cat 2,cat 3')
        self.assertEqual(vCategory.from_ical(v_cat.to_ical()), catz)
