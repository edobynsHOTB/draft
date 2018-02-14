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
class TestUpdateUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            # Create user object.
            cls.user = QaAdpqShell.QaADPQShell()
            assert(cls.user != None)
            
#             # Register this user with a facebook account.
#             cls.user.register_with_facebook('facebook', cls.user.testEmail, 
#                                             cls.user.testNetworkAuthToken,
#                                             cls.user.testNetworkUserId)
#             assert(cls.user != None)
        except:
            print("Unexpected error during setUp:", sys.exc_info()[0])
            raise

    
    
    # Test successfully insert
    def test_success(self):
        pass
#         # Attempt to insert
#         responseBody = self.user.update_user(_id = self.user.GetUserID(),
#                                  firstName = TestUpdateUser.testFirstName,
#                                  lastName = TestUpdateUser.testLastName,
#                                  email = self.user.testEmail,
#                                  gender = TestUpdateUser.testGender,
#                                  status = TestUpdateUser.testStatus,
#                                  age = TestUpdateUser.testAge,
#                                  orientation = TestUpdateUser.testOrientation,
#                                  education = TestUpdateUser.testEducation,
#                                  isStudent = False,
#                                  network = 'facebook')
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
    # *                           Id tests                                *
    # *********************************************************************
     
     
     
    # Missing INSERT information from request call.
    def test_missing(self):
        pass
#         # Missing INSERT value.
#         responseBody = self.user.update_user(_id = self.user.GetUserID(),
#                                  idExclude=True)
#                
#         self.assertEqual(responseBody['err']['err'], 'User ID required',
#                           msg='test_missing assert#1 has failed.')
         
         
         
    # Test a null INSERT value call.
    def test_null(self):
        pass
#         # Null INSERT value.
#         responseBody = self.user.update_user(_id = '')
#          
#         self.assertEqual(responseBody['err']['err'], 'User ID required',
#                           msg='test_null assert#1 has failed.')
         
         
         
    # Test an int INSERT value call.
    def test_int(self):
        pass
#         # Int INSERT value.
#         responseBody = self.user.update_user(_id = 530351020650)
#          
#         self.assertEqual(responseBody['error'], True,
#                           msg='test_int assert#1 has failed.')
          
          
          
    # Test a float INSERT value call.
    def test_float(self):
        # Float INSERT value.
        responseBody = self.user.update_user(_id = -.020350545)
         
        self.assertEqual(responseBody['err']['err'], 'user does not exist',
                          msg='test_float assert#1 has failed.') 
         
         
         
    # Test a string INSERT value call.
    def test_string(self):
        pass
#         # String INSERT value.
#         responseBody = self.user.update_user(_id = "';:.>,</?]}[{!@#$%^&*()-_=+|\"")
#          
#         self.assertEqual(responseBody['err']['err'], 'user does not exist',
#                           msg='test_string assert#1 has failed.')
         
         
         
    # Test an array INSERT value call.
    def test_array(self):
        pass
#         # Array INSERT value.
#         responseBody = self.user.update_user(_id = ['hodl', 666, [.6, 0], {}])
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
    
#     suite.addTest(TestUpdateUser('test_success'))
#                       
#     suite.addTest(TestUpdateUser('test_missingId'))
#     suite.addTest(TestUpdateUser('test_nullId'))
#     suite.addTest(TestUpdateUser('test_intId'))
#     suite.addTest(TestUpdateUser('test_floatId'))
#     suite.addTest(TestUpdateUser('test_stringId'))
#     suite.addTest(TestUpdateUser('test_arrayId'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())