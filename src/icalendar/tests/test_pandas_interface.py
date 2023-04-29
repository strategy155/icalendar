import unittest

import pandas


class TestValueConversion(unittest.TestCase):
    """
    This class is used to test new pandas interface functionality
    """
    def test_vText_val(self):
        """
        We check here, if to_val method is working correctly in vtext
        """
        from ..prop import vText

        # Creating sample text
        sample_text = "Simple text"

        # Wrapping it in vtext
        sample_vtext = vText(sample_text)

        # getting the to_value value
        sample_vtext_value = sample_vtext.to_value()

        # checking if they are equal
        self.assertEqual(sample_text, sample_vtext_value)


    def test_vCategory_val(self):
        """
        we check here if vCategory to_value method works correctly
        """
        from ..prop import vCategory

        # simple categories set
        catz = ['cat 1', 'cat 2', 'cat 3']

        # converting them to ical vCategory
        v_cat = vCategory(catz)

        # getting the pure value
        v_cat_val = v_cat.to_value()

        # testing if they are equal
        self.assertEqual(catz, v_cat_val)

