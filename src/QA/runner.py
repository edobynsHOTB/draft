'''
Created on Feb 14, 2018

@author: Luis.Escobar-Driver
'''

import unittest, xmlrunner

# Import test modules   
from src.QA.test import smokeTest
from src.QA.test import testGetAgencies
from src.QA.test import testGetTags
from src.QA.test import testGetArticles
from src.QA.test import testGetSearch
from src.QA.test import testUserLogin


# Initialize a test loader & test suite package.
loader = unittest.TestLoader()
suite  = unittest.TestSuite()
 
# Add test suites to the runners suite package.
suite.addTests(loader.suiteClass(smokeTest.suite()))
suite.addTests(loader.suiteClass(testGetAgencies.suite()))
suite.addTests(loader.suiteClass(testGetTags.suite()))
suite.addTests(loader.suiteClass(testGetArticles.suite()))
suite.addTests(loader.suiteClass(testGetSearch.suite()))
suite.addTests(loader.suiteClass(testUserLogin.suite()))
 
# Initialize an xml runner.
testRunner=xmlrunner.XMLTestRunner(output='testReports', verbosity=2)
 
# Run the suite & save the results.
results = testRunner.run(suite)
  
print(results)