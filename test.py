import data_analysis
from unittest.mock import Mock
import unittest
import pandas

class Unit_test(unittest.TestCase):
    date_mocked = data_analysis.date_range('2013','1','01','2016','1','01')
    data_analysis.tree.insert=Mock(return_value=None)
    

    def test_read_file(self):
        self.assertIsInstance(data_analysis.readCsv('Crash Statistics Victoria.csv'),pandas.core.frame.DataFrame)
    
    def test_read_file_err(self):
        self.assertFalse(data_analysis.readCsv('Wrong File Name.csv'))
    
    def test_date_range(self):
        self.assertEqual(data_analysis.date_range('2013','1','01','2016','1','01'),('2013101','2016101'))
     
    def test_search_by_date(self):
        self.assertTrue(data_analysis.searchBy_date(self.date_mocked))
     
    def test_chart_hourly_accident(self):
        self.assertTrue(data_analysis.opt2(self.date_mocked,'title'))       

    def test_search_by_accident_type(self):
        self.assertTrue(data_analysis.opt3(self.date_mocked,'Pedestrian'))

    def test_chart_analyze_alcohol(self):
        self.assertTrue(data_analysis.opt4(self.date_mocked))
        
    def test_search_by_speedzone(self):
        self.assertTrue(data_analysis.opt5(self.date_mocked,'60 km/hr'))
        
    ########### from here , error_tests begin
        
    def test_error_search_by_date(self):
        self.assertNotEqual(data_analysis.searchBy_date('2013101'),True)
     
    def test_error_chart_hourly_accident(self):
        self.assertNotEqual(data_analysis.opt2('2013101','title'),True)       

    def test_error_search_by_accident_type(self):
        self.assertNotEqual(data_analysis.opt3('2013101','Pedestrian'),True)

    def test_error_chart_analyze_alcohol(self):
        self.assertNotEqual(data_analysis.opt4('2013101'),True)
        
    def test_error_search_by_speedzone(self):
        self.assertNotEqual(data_analysis.opt5('2013101','60 km/hr'),True)
       
unittest.main()