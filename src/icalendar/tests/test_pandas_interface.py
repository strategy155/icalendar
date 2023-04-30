import unittest
import datetime


class TestValueConversion(unittest.TestCase):
    """
    This class is used to test new pandas interface functionality
    """

    def test_vDDDTypes_val(self):
        """
        This function checks to value method of every vdddtype type
        """
        from ..prop import vDDDTypes

        # sample datetime
        sample_datetime = datetime.datetime(2001, 1, 1, 12, 30, 0)

        # wrapping datetime into vdddtype
        wrapped_datetime = vDDDTypes(sample_datetime)

        # getting its value
        wrapped_datetime_value = wrapped_datetime.to_value()

        # checking for their equality
        self.assertEqual(sample_datetime, wrapped_datetime_value)

        # sample date
        sample_date = datetime.date(2001, 2, 3)

        # wrapping date into vdddtype
        wrapped_date = vDDDTypes(sample_date)

        # getting wrapped date value
        wrapped_date_value = wrapped_date.to_value()

        # checking for their equality
        self.assertEqual(sample_date, wrapped_date_value)

        # getting sample duration
        sample_duration = datetime.timedelta(seconds=15)

        # wrapping duration into vdddtype
        wrapped_duration = vDDDTypes(sample_duration)

        # getting wrapped duration value
        wrapped_duration_value = wrapped_duration.to_value()

        # checking for the equality of the results
        self.assertEqual(sample_duration, wrapped_duration_value)

        # getting sample time
        sample_time = datetime.time(hour=3)

        # wrapping time int the vdddtype
        wrapped_time = vDDDTypes(sample_time)

        # getting wrapped to value result
        wrapped_time_value = wrapped_time.to_value()

        # checking the equality
        self.assertEqual(sample_time, wrapped_time_value)

        # getting period
        sample_period = (datetime.datetime(2000, 1, 1), datetime.datetime(2000, 1, 2))

        # wrapping period into vdddtypes
        wrapped_period = vDDDTypes(sample_period)

        # getting wrapped value of period
        wrapped_period_value = wrapped_period.to_value()

        # checking their equality
        self.assertEqual(sample_period, wrapped_period_value)









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


    def test_vURI_val(self):
        """
        We check if the vURI to_val method is working right
        """
        from ..prop import vUri

        # getting sample website address
        example_website_address = "http://www.example.com/"

        # loading it into vUri
        vuri_item = vUri(example_website_address)

        # getting to_value value
        vuri_parsed_address_value = vuri_item.to_value()

        # checking if they're equal
        self.assertEqual(vuri_parsed_address_value, example_website_address)



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

