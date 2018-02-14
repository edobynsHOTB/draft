'''
Created on Feb 14, 2018

@author: Luis.Escobar-Driver
'''

import unittest, xmlrunner

# Import test modules   
from src.QA.test import testGetAgencies
# from test import testRegisterFacebook
# from test import testRegisterInstagram
# from test import testLoginEmail 
# from test import testLoginFacebook
# from test import testLoginInstagram
# from test import testUpdateUser

# Initialize a test loader & test suite package.
loader = unittest.TestLoader()
suite  = unittest.TestSuite()
 
# Add test suites to the runners suite package.
suite.addTests(loader.suiteClass(testGetAgencies.suite()))
# suite.addTests(loader.suiteClass(testRegisterFacebook.suite()))
# suite.addTests(loader.suiteClass(testRegisterInstagram.suite()))
# suite.addTests(loader.suiteClass(testLoginEmail.suite()))
# suite.addTests(loader.suiteClass(testLoginFacebook.suite()))
# suite.addTests(loader.suiteClass(testLoginInstagram.suite()))
# suite.addTests(loader.suiteClass(testUpdateUser.suite()))
 
# Initialize an xml runner.
testRunner=xmlrunner.XMLTestRunner(output='testReports', verbosity=2)
 
# Run the suite & save the results.
results = testRunner.run(suite)
  
print(results)