# Excel utils test
# https://docs.python.org/3/library/unittest.html
import unittest

from pythonutils import excelutils


class TestExcelUtils(unittest.TestCase):

    def setUp(self):
        self.xls_file = './data/考试成绩.xls'
        self.xls_file_sheet1_name = '成绩'
        self.xls_file_new = './data/考试成绩-tmp.xls'

    def test_read_excel_sheet1(self):
        records_of_include_header = excelutils.read_excel_sheet1(file_name=self.xls_file, include_header=True)
        records_of_no_headers = excelutils.read_excel_sheet1(file_name=self.xls_file)
        self.assertEqual(len(records_of_include_header), len(records_of_no_headers) + 1)

    def test_read_excel_by_sheet_index(self):
        records = excelutils.read_excel_sheet_by_index(file_name=self.xls_file, sheet_index=1)
        self.assertIsNotNone(records)

    def test_read_excel_by_sheet_name(self):
        records = excelutils.read_excel_sheet_by_name(file_name=self.xls_file, sheet_name=self.xls_file_sheet1_name)
        self.assertIsNotNone(records)

    def test_write_excel_one_sheet(self):
        headers = excelutils.read_excel_headers_sheet1(file_name=self.xls_file)
        records = excelutils.read_excel_sheet1(file_name=self.xls_file)
        excelutils.write_excel_one_sheet(file_name=self.xls_file_new, sheet_name='Sheet1', headers=headers,
                                         records=records)


if __name__ == '__main__':
    unittest.main()
