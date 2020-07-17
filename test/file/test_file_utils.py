import unittest
from pythonutils import fileutils


class FileUtilsTest(unittest.TestCase):

    def test_write_file(self):
        test_file = './data/test.txt'
        fileutils.write_file(test_file, 'a test file')
        self.assertTrue(fileutils.exists_file(test_file))
        self.assertTrue(fileutils.is_not_empty_file(test_file))

    def test_create_an_new_empty_file(self):
        new_empty_file = './data/new_empty.txt'
        fileutils.create_file(new_empty_file)
        self.assertTrue(fileutils.exists_file(new_empty_file))
        self.assertTrue(fileutils.is_empty_file(new_empty_file))

    def test_override_an_existed_file(self):
        existed_file = './data/existed.txt'
        fileutils.write_file(existed_file, 'Something already existed')
        self.assertTrue(fileutils.is_not_empty_file(existed_file))

        fileutils.create_file(existed_file)
        self.assertTrue(fileutils.is_empty_file(existed_file))

    def test_touch_file(self):
        existed_file = './data/existed.txt'
        fileutils.write_file(existed_file, 'Something already existed')
        self.assertTrue(fileutils.is_not_empty_file(existed_file))

        fileutils.touch(existed_file)
        self.assertTrue(fileutils.is_not_empty_file(existed_file))

    def test_get_file_ext(self):
        self.assertEqual(fileutils.get_file_ext('/etc/mysql/my.cnf'), '.cnf')
        self.assertEqual(fileutils.get_file_ext('/data/测试 2020.xlsx'), '.xlsx')
        self.assertEqual(fileutils.get_file_ext('/etc/nginx/conf.d/xdevops.cn.conf'), '.conf')
        self.assertEqual(fileutils.get_file_ext('~/.bashrc'), '')
        self.assertEqual(fileutils.get_file_ext('/etc/profile'), '')


if __name__ == '__main__':
    unittest.main()
