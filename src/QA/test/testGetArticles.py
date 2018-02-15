import sys, unittest, src.QA.QaAdpqShell as QaAdpqShell

'''
    ADPQ v1 INSERT end point.
    
    Purpose - INSERT
    
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
class TestGetArticles(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            # Create user object.
            cls.user = QaAdpqShell.QaADPQShell()
            assert(cls.user != None)
            
        except:
            print("Unexpected error during setUp:", sys.exc_info()[0])
            raise

    
    
    # Test successfully insert
    def test_success(self):
        pass
#         # Attempt to insert
#         responseBody = self.user.get_article_list()
#           
#         # Ensure insert
#         self.assertEqual(responseBody['error'], False,
#                           msg='test_Success assert#1 has failed.')
#          
#         self.assertEqual(responseBody['data']['firstName'], TestUpdateUser.testFirstName,
#                             msg='test_Success assert#2 has failed.')
#           
#         self.assertEqual(responseBody['data']['lastName'], TestUpdateUser.testLastName,
#                           msg='test_Success assert#3 has failed.')
#           
#         self.assertEqual(responseBody['data']['email'], self.user.testEmail,
#                           msg='test_Success assert#4 has failed.')
#           
#         self.assertEqual(responseBody['data']['gender'], TestUpdateUser.testGender,
#                           msg='test_Success assert#5 has failed.')
#           
#         self.assertEqual(responseBody['data']['status'], TestUpdateUser.testStatus,
#                           msg='test_Success assert#6 has failed.')
#          
#         self.assertEqual(responseBody['data']['age'], TestUpdateUser.testAge,
#                             msg='test_Success assert#7 has failed.')
#           
#         self.assertEqual(responseBody['data']['orientation'], TestUpdateUser.testOrientation,
#                           msg='test_Success assert#8 has failed.')
#           
#         self.assertEqual(responseBody['data']['education'], TestUpdateUser.testEducation,
#                           msg='test_Success assert#9 has failed.')
#           
#         self.assertEqual(responseBody['data']['isStudent'], 'False',
#                           msg='test_Success assert#10 has failed.')
#           
#         self.assertEqual(responseBody['data']['network'], 'facebook',
#                           msg='test_Success assert#11 has failed.')
         
         
         
         
    # *********************************************************************
    # *                         INSERT tests                              *
    # *********************************************************************
     
     
     
    # Missing INSERT information from request call.
    def test_missing(self):
        pass
#         # Missing INSERT value.
#         responseBody = self.user.get_article_list()
#                
#         self.assertEqual(responseBody['err']['err'], 'User ID required',
#                           msg='test_missing assert#1 has failed.')
         
         
         
    # Test a null INSERT value call.
    def test_null(self):
        pass
#         # Null INSERT value.
#         responseBody = self.user.get_article_list()
#          
#         self.assertEqual(responseBody['err']['err'], 'User ID required',
#                           msg='test_null assert#1 has failed.')
         
         
         
    # Test an int INSERT value call.
    def test_int(self):
        pass
#         # Int INSERT value.
#         responseBody = self.user.get_article_list()
#          
#         self.assertEqual(responseBody['error'], True,
#                           msg='test_int assert#1 has failed.')
          
          
          
    # Test a float INSERT value call.
    def test_float(self):
        pass
#         # Float INSERT value.
#         responseBody = self.user.get_article_list()
#          
#         self.assertEqual(responseBody['err']['err'], 'user does not exist',
#                           msg='test_float assert#1 has failed.') 
         
         
         
    # Test a string INSERT value call.
    def test_string(self):
        pass
#         # String INSERT value.
#         responseBody = self.user.get_article_list("';:.>,</?]}[{!@#$%^&*()-_=+|\"")
#          
#         self.assertEqual(responseBody['err']['err'], 'user does not exist',
#                           msg='test_string assert#1 has failed.')
         
         
         
    # Test an array INSERT value call.
    def test_array(self):
        pass
#         # Array INSERT value.
#         responseBody = self.user.get_article_list(['hodl', 666, [.6, 0], {}])
#              
#         self.assertEqual(responseBody['err']['err'], 'User ID required',
#                           msg='test_array assert#1 has failed.') 
        
        
        
        
        
    @classmethod
    def tearDownClass(cls):
        try:
            pass
#             cls.user.remove_user(cls.user.testEmail)
        except:
            print("Unexpected error during setUp:", sys.exc_info()[0])
            #raise
        #cls.user.remove_user(cls.user.testEmail)
    
    
    
def suite():
    suite = unittest.TestSuite()
    
#     suite.addTest(TestGetArticles('test_success'))
#                       
#     suite.addTest(TestGetArticles('test_missing'))
#     suite.addTest(TestGetArticles('test_null'))
#     suite.addTest(TestGetArticles('test_int'))
#     suite.addTest(TestGetArticles('test_float'))
#     suite.addTest(TestGetArticles('test_string'))
#     suite.addTest(TestGetArticles('test_array'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())