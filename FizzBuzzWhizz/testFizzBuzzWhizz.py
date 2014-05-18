import unittest
import dictProcess

class testdictProcess(unittest.TestCase):

  def setUp(self):
    self.dpclass = dictProcess.IsValidArgus()
    self.avfailed =  'argusValidity Failed'
    self.ovfailed =  'optValidity Failed'

  def tearDown(self):
    pass

  def testargusValidity_ok(self):
    self.assertTrue(self.dpclass.argusValidity(3), self.avfailed)

  def testargusValidity_fail(self):
    with self.assertRaises(SystemExit) as cm:
      self.dpclass.argusValidity('a')
    self.assertEqual(cm.exception.code, 1, self.avfailed)

  def testoptValidity_ok(self):
    self.assertTrue(self.dpclass.optValidity('fizz'), self.ovfailed)

  def testoptValidity_fail(self):
    with self.assertRaises(SystemExit) as cm:
      self.dpclass.optValidity('abc')
    self.assertEqual(cm.exception.code, 1)

  def testcreateRelDict(self):
    with self.assertRaises(SystemExit) as cm:
      self.dpclass.createRelDict()
    self.assertEqual(cm.exception.code, 0)

    # defaultlist = {'scope': 100, 'buzz': 5, 'whizz': 7, 'fizz': 3}
    # self.assertEqual(self.dpclass.createRelDict(), defaultlist, 'createRelDict Failed')


if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(testdictProcess)
  unittest.TextTestRunner(verbosity=2).run(suite)

  # unittest.main(exit=False)

# vi:set tabstop=2 shiftwidth=2 shiftwidth=2: