import os
import shutil
import unittest

from tillage import contents, description

class TestContents(unittest.TestCase):

    def setUp(self):
        self.descr = description.Description(name='tillagedemoproject', author='Demo Author', year=1897)
    ##    myTemp = os.environ['TEMP']
    ##    if not os.path.isdir(myTemp):
    ##        os.mkdir(myTemp)
    ##    self.dname = tempfile.mkdtemp()
    ##    self.addCleanup(shutil.rmtree, self.dname)
    ##    self.fpath = filepath.FilePath(self.dname)

    def test_README(self):
        self.assertIn(contents.getREADME, contents.canonical)
        name, readme = contents.getREADME(self.descr)
        self.assertEquals(name, 'README.rst')
        lines = readme.strip().splitlines()
        self.assertEquals(lines[0], self.descr.name)
        self.assertEquals(set(lines[1]), set('-'))
        self.assertGreaterEqual(len(lines[1]), len(lines[0]))

    def test_LICENSE(self):
        self.assertIn(contents.getLICENSE, contents.canonical)
        name, license = contents.getLICENSE(self.descr)
        self.assertEquals(name, 'LICENSE')
        lines = [x for x in license.splitlines() if x != '']
        self.assertEquals(lines[0], 'The MIT License (MIT)')
        self.assertIn(str(self.descr.year), lines[1])
        self.assertIn(self.descr.author, lines[1])
