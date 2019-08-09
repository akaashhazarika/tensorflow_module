import numpy as np
from unittest import TestCase
from load_data_tensorflow import csv


class CSV(TestCase):

    def test_column_names(self):
        test_result = [[[['mangoes', 4,], ['Python codes', 6]]], ['Keyword', 'Impressions', 'Cost_Micros']]
        column_names = test_result[1]

        obj = csv.csv_creator(test_result)
        self.assertEqual(obj.extract_column_names(),column_names)
    
    def file_saving_incorrect(self):
        test_result = [[[['mangoes', 4,], ['Python codes', 6]]], ['Keyword', 'Impressions', 'Cost_Micros']]
        obj = csv.csv_creator(test_result)
        val = obj.get_data_frame()
        self.assertEqual(None, obj.save_to_csv('random.temp'))

    def file_saving_correct(self):
        test_result = [[[['mangoes', 4,], ['Python codes', 6]]], ['Keyword', 'Impressions', 'Cost_Micros']]
        obj = csv.csv_creator(test_result)
        val = obj.get_data_frame()
        self.assertEqual(0, obj.save_to_csv('random.csv'))


    def check_data_extraction(self):
        test_result = [[[['mangoes', 4,], ['Python codes', 6]]], ['Keyword', 'Impressions', 'Cost_Micros']]
        obj = csv.csv_creator(test_result)
        data = numpy.asarray(test_result[0])
        shape = data.shape[1:]
        res = lis(np.reshape(data,shape))
        self.assertEqual(obj.extract_data(), res)


    def data_frame_not_created(self):
        test_result = [[[['mangoes', 4,], ['Python codes', 6]]], ['Keyword', 'Impressions', 'Cost_Micros']]
        obj = csv.csv_creator(test_result)
        self.assertEqual(False, obj.save_to_csv('result.csv'))


    def check_flatten_step(self):
        test_result = [[[['mangoes', 4,], ['Python codes', 6]]], ['Keyword', 'Impressions']]
        test_result = np.asarray(test_result)
        self.assertEqual(test_result.shape[1:], None)

        
