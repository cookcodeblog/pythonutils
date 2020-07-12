import unittest

from pythonutils import webutils
import os


class WebUtilsTest(unittest.TestCase):

    def test_unquote(self):
        self.assertEqual('测试', webutils.unquote('%E6%B5%8B%E8%AF%95'))

    def test_quote(self):
        self.assertEqual('%E6%B5%8B%E8%AF%95', webutils.quote('测试'))

    def test_fake_dummy_headers(self):
        headers = webutils.fake_request_headers()
        self.assertIn('Chrome', headers['User-Agent'])

    def test_fake_login_headers(self):
        headers = webutils.fake_request_headers(refer='http://localhost:8080',
                                                cookie='JSESSIONID=EABD8D1A79BD947B0B66E4F4BE989342')
        self.assertIn('Chrome', headers['User-Agent'])
        self.assertIn('http', headers['Refer'])
        self.assertIn('JSESSIONID', headers['Cookie'])

    def test_get_attachment_name_without_quote(self):
        self.assertEqual('测试.xls', webutils.get_attachment_name('Content-Disposition: attachment;filename=测试.xls'))

    def test_get_attachment_name_with_quote(self):
        self.assertEqual('测试.rar', webutils.get_attachment_name(
            'Content-Disposition: attachment;filename=%E6%B5%8B%E8%AF%95.rar'))

    def test_download_file_with_name(self):
        url = 'https://readthedocs.org/projects/python-guide/downloads/pdf/latest/'
        target_file = './data/python-guide.pdf'
        webutils.download_file(url, target_file)
        self.assertTrue(os.path.isfile(target_file))

    def test_download_file_without_name(self):
        url = 'https://readthedocs.org/projects/python-guide/downloads/pdf/latest/'
        webutils.download_file(url)
        self.assertTrue(os.path.isfile('docs-python-guide-org-en-latest.pdf'))

    def test_download_large_file(self):
        url = 'https://readthedocs.org/projects/python-guide/downloads/pdf/latest/'
        target_file = './data/python-guide-large.pdf'
        webutils.download_large_file(url, target_file, chunk_size=1024 * 1024)
        self.assertTrue(os.path.isfile(target_file))


if __name__ == '__main__':
    unittest.main()
