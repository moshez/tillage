import os
import shutil
import unittest

from tillage import contents, description

class TestContents(unittest.TestCase):

    def setUp(self):
        self.descr = description.Description(name='tillagedemoproject',
                                             author='Demo Author',
                                             authorEmail='demo@example.com',
                                             description='A project to show how to till',
                                             year=1897,
                                             githubID='demo-author')
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

    def test_setup_py(self):
        self.assertIn(contents.getSetupPy, contents.canonical)
        name, setup = contents.getSetupPy(self.descr)
        self.assertEquals(name, 'setup.py')
        variables = dict(x.strip().strip(',').split('=', 1) for x in setup.splitlines() if '=' in x)
        self.assertEquals(variables['name'], repr(self.descr.name))
        self.assertEquals(variables['version'], repr('0.0.0'))
        self.assertEquals(variables['author'], repr(self.descr.author))
        self.assertEquals(variables['description'], repr(self.descr.description))
        self.assertEquals(variables['url'], repr('https://github.com/{}/{}'.format(self.descr.githubID, self.descr.name)))
