import unittest

import pandas


class TestPandas(unittest.TestCase):
    """
    This class is used to test new pandas interface functionality
    """
    def test_pandas_vCategory(self):
        """
        we check here if vCategory to pandas method works correctly
        """
        from ..prop import vCategory

        # simple categories set
        catz = ['cat 1', 'cat 2', 'cat 3']

        # converting them to ical vCategory
        v_cat = vCategory(catz)

        # converting them to pandas directly
        pd_catz = pandas.Categorical(values=catz)

        # converting v_cat through to_pandas mechanism
        v_cat_pd = v_cat.to_pandas()

        # testing if they are equal
        self.assertTrue(v_cat_pd.equals(pd_catz))

    def test_pandas_vCategory(self):
        """
        we check here if vCategory to pandas method works correctly
        """
        from ..prop import vCategory

        # simple categories set
        catz = ['cat 1', 'cat 2', 'cat 3']

        # converting them to ical vCategory
        v_cat = vCategory(catz)

        # converting them to pandas directly
        pd_catz = pandas.Categorical(values=catz)

        # converting v_cat through to_pandas mechanism
        v_cat_pd = v_cat.to_pandas()

        # testing if they are equal
        self.assertTrue(v_cat_pd.equals(pd_catz))

