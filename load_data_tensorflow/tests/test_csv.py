from unittest import TestCase
from load_data_tensorflow import csv


class CSV(TestCase):
    def test_is_string(self):
        test_result = [[[['mangoes', 4,], ['Python codes', 6]]], ['Keyword', 'Impressions', 'Cost_Micros']]
        column_names = test_result[1]

        obj = csv.csv_creator(test_result)
        self.assertTrue(obj.extract_column_names(),column_names)
        