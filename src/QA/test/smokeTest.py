import sys, unittest, src.QA.QaAdpqShell as QaAdpqShell

## @package smoke test
#

'''
    ADPQ v1 - All end points.
    
    Purpose - Will test all end points for their status. 
    
    Method signature:
        INSERT
                     
    Notes: INSERT
    
    Required:
        INSERT
        
    Optional:
        INSERT

    Test cases
        Successfully INSERT
        
        INSERT missing from request call.
        Null INSERT value. 
        Int INSERT value.
        Float INSERT value.
        String INSERT value.
        Array INSERT value.
'''
class SmokeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass
#         try:
#             # Create user object.
#             cls.user = QaAdpqShell.QaADPQShell()
#             assert(cls.user != None)
#             
#         except:
#             print("Unexpected error during setUp:", sys.exc_info()[0])
#             raise

     
     
     
    # Get the status of the end point.
    def test_GetAgenciesStatus(self):
        pass
#         url = QaADPQShell.BaseURL + QaADPQShell.GetAgencies 
         
         
         
    # Get the status of the end point.
    def test_GetTagStatus(self):
        pass
#         url = QaADPQShell.BaseURL + QaADPQShell.GetTags
         
         
         
    # Get the status of the end point.
    def test_GetArticleStatus(self):
        pass
#         url = QaADPQShell.BaseURL + QaADPQShell.GetArticles
          
          
          
    # Get the status of the end point.
    def test_GetSearchStatus(self):
        pass
#         url = QaADPQShell.BaseURL + QaADPQShell.GetSearch
         
         
         
    # Get the status of the end point.
    def test_UserLoginStatus(self):
        pass
#         url = QaADPQShell.BaseURL + QaADPQShell.UsersLogin
         
         
         
        
        
        
        
    @classmethod
    def tearDownClass(cls):
        pass
#         try:
#             pass
# #             cls.user.remove_user(cls.user.testEmail)
#         except:
#             print("Unexpected error during setUp:", sys.exc_info()[0])
#             #raise
#         #cls.user.remove_user(cls.user.testEmail)
    
    
    
def suite():
    suite = unittest.TestSuite()
    
#     suite.addTest(SmokeTest('test_success'))
#                       
#     suite.addTest(SmokeTest('test_GetAgenciesStatus'))
#     suite.addTest(SmokeTest('test_GetTagStatus'))
#     suite.addTest(SmokeTest('test_GetArticleStatus'))
#     suite.addTest(SmokeTest('test_GetSearchStatus'))
#     suite.addTest(SmokeTest('test_UserLoginStatus'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())