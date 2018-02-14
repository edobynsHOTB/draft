import requests, sys

environmentBody = { 'staging':'INSERT/api/v1/',
                    'prod':'Production URL here.'
                  }
setEnv = ''

# Takes care of the out of index error in sys.argv
if len(sys.argv) == 2:
    if sys.argv[1] not in environmentBody.keys():
        print('\n[AutoScript] Defaulting to staging.\n')
        setEnv = environmentBody['staging']
    else:
        setEnv = environmentBody[sys.argv[1]]  
else:
    print('\n[AutoScript] Defaulting to staging.\n')
    setEnv = environmentBody['staging']

setEnv.strip()



## @class ADPQ Test Automation Shell 
# This shell provides a mechanisms from which to run python3 unittest 
# scripts. The user has absolute control over the header & body 
# parameters. Body & header Parameters can be left out of any call or be 
# assigned any values, including null. Class is called from an external 
# script which has inherited from unittest.TestCase
#
class QaADPQShell:
    
    ## @var Test variables which are used by calling unittest scripts.
    testEmail = 'ldriver@hotbsoftware.com'
    testPassword = 'p@assw0rd1!'
    testFirstName = 'Ragnar'
    testLastName = 'Lothbrok'
    testGender = 'Viking Male'
    testStatus = 'Still alive'
    testAge = '55'
    testOrientation = 'Viking'
    testEducation = 'UCI'
    testFcmId = "abc123321bca"
    
    ## @var URL end point completions.
    Agencies = 'agencies'
    Tags = 'tags'
    Articles = 'articles'
    Search = 'search'
    UsersLogin = 'users/login'
        
        
    ## @fn __init__ : Class initializations.
    def __init__(self, env=setEnv):
        # Essential information used to successfully run calling scripts.
        self.ClientID = 'ffcc8.4b0-and-??v27-93ae-92.361f002671'
        self.UserNetwork = ''
        self.AuthKey = ''
        self.UserID = ''
        self.email = ''
        self.password = ''
        self.placeId = []
        self.groupId = []
        self.environment = env
        
        
        

    ## @fn get_agency_list : Will return a list of all agencies.
    # 
    # :required -
    # :required -
    # :required -
    #
    def get_agency_list(self):
        # URL end point.
        url = self.environment + QaADPQShell.Agencies

        # HTTP Action.
        HTTP_action = 'GET'
        
        # Header Parameters.
        headers = {
            'Content-Type' : 'application/json',
            'Cache-Control': 'no-cache'#,
            #'ClientId' : self.ClientID
        }
        
#         # Add the ClientId header parameter.
#         if ClientIdExclude == True:
#             pass
#         elif ClientId != '':
#             body['ClientId'] = self.ClientId
#         else:
#             body['ClientId'] = ''
        
        
        # Dynamically set key/value body pairs. Add all body parameters.
        # Null values indicates the field was left blank.
        body = {}
        
#         # Add the network body parameter.
#         if networkExclude == True:
#             pass
#         elif network != '':
#             body['network'] = network
#         else:
#             body['network'] = ''
#             
#         # Add the email body parameter.
#         if emailExclude == True:
#             pass
#         elif email != '':
#             body['email'] = email
#         else:
#             body['email'] = ''
#             
#         # Add the password body parameter.
#         if passwordExclude == True:
#             pass
#         elif password != '':
#             body['password'] = password
#         else:
#             body['password'] = ''
            
        # Make HTTPS Request.
        response = requests.request(HTTP_action, url, json=body, 
                                    headers=headers, verify=False)
    
        # Return requests object of json data.
        responseBody = response.json()
        
        # ~~ TESTING ~~
        print('\nget_agency_list\n', responseBody)
        print('response.status_code: ', response.status_code)
        
        return responseBody
    
    
    

    ## @fn get_tag_list : Will 
    # 
    # :required -
    # :required -
    # :required -
    #
    def get_tag_list(self):
        # URL end point.
        url = self.environment + QaADPQShell.Tags

        # HTTP Action.
        HTTP_action = 'GET'
        
        # Header Parameters.
        headers = {
            'Content-Type' : 'application/json',
            'Cache-Control': 'no-cache'#,
            #'ClientId' : self.ClientID
        }
        
#         # Add the ClientId header parameter.
#         if ClientIdExclude == True:
#             pass
#         elif ClientId != '':
#             body['ClientId'] = self.ClientId
#         else:
#             body['ClientId'] = ''
        
        
        # Dynamically set key/value body pairs. Add all body parameters.
        # Null values indicates the field was left blank.
        body = {}
        
#         # Add the network body parameter.
#         if networkExclude == True:
#             pass
#         elif network != '':
#             body['network'] = network
#         else:
#             body['network'] = ''
#             
#         # Add the email body parameter.
#         if emailExclude == True:
#             pass
#         elif email != '':
#             body['email'] = email
#         else:
#             body['email'] = ''
#             
#         # Add the password body parameter.
#         if passwordExclude == True:
#             pass
#         elif password != '':
#             body['password'] = password
#         else:
#             body['password'] = ''
            
        # Make HTTPS Request.
        response = requests.request(HTTP_action, url, json=body, 
                                    headers=headers, verify=False)
    
        # Return requests object of json data.
        responseBody = response.json()
        
        # ~~ TESTING ~~
        print('\nget_tag_list\n', responseBody)
        print('response.status_code: ', response.status_code)
        
        return responseBody
    
    
    
    ## @fn get_article_list : Will 
    # 
    # :required -
    # :required -
    # :required -
    #
    def get_article_list(self):
        # URL end point.
        url = self.environment + QaADPQShell.Articles

        # HTTP Action.
        HTTP_action = 'GET'
        
        # Header Parameters.
        headers = {
            'Content-Type' : 'application/json',
            'Cache-Control': 'no-cache'#,
            #'ClientId' : self.ClientID
        }
        
#         # Add the ClientId header parameter.
#         if ClientIdExclude == True:
#             pass
#         elif ClientId != '':
#             body['ClientId'] = self.ClientId
#         else:
#             body['ClientId'] = ''
        
        
        # Dynamically set key/value body pairs. Add all body parameters.
        # Null values indicates the field was left blank.
        body = {}
        
#         # Add the network body parameter.
#         if networkExclude == True:
#             pass
#         elif network != '':
#             body['network'] = network
#         else:
#             body['network'] = ''
#             
#         # Add the email body parameter.
#         if emailExclude == True:
#             pass
#         elif email != '':
#             body['email'] = email
#         else:
#             body['email'] = ''
#             
#         # Add the password body parameter.
#         if passwordExclude == True:
#             pass
#         elif password != '':
#             body['password'] = password
#         else:
#             body['password'] = ''
            
        # Make HTTPS Request.
        response = requests.request(HTTP_action, url, json=body, 
                                    headers=headers, verify=False)
    
        # Return requests object of json data.
        responseBody = response.json()
        
        # ~~ TESTING ~~
        print('\nget_article_list\n', responseBody)
        print('response.status_code: ', response.status_code)
        
        return responseBody
    
    
    
    ## @fn get_search_list : Will 
    # 
    # :required -
    # :required -
    # :required -
    #
    def get_search_list(self):
        # URL end point.
        url = self.environment + QaADPQShell.Search

        # HTTP Action.
        HTTP_action = 'GET'
        
        # Header Parameters.
        headers = {
            'Content-Type' : 'application/json',
            'Cache-Control': 'no-cache'#,
            #'ClientId' : self.ClientID
        }
        
#         # Add the ClientId header parameter.
#         if ClientIdExclude == True:
#             pass
#         elif ClientId != '':
#             body['ClientId'] = self.ClientId
#         else:
#             body['ClientId'] = ''
        
        
        # Dynamically set key/value body pairs. Add all body parameters.
        # Null values indicates the field was left blank.
        body = {}
        
#         # Add the network body parameter.
#         if networkExclude == True:
#             pass
#         elif network != '':
#             body['network'] = network
#         else:
#             body['network'] = ''
#             
#         # Add the email body parameter.
#         if emailExclude == True:
#             pass
#         elif email != '':
#             body['email'] = email
#         else:
#             body['email'] = ''
#             
#         # Add the password body parameter.
#         if passwordExclude == True:
#             pass
#         elif password != '':
#             body['password'] = password
#         else:
#             body['password'] = ''
            
        # Make HTTPS Request.
        response = requests.request(HTTP_action, url, json=body, 
                                    headers=headers, verify=False)
    
        # Return requests object of json data.
        responseBody = response.json()
        
        # ~~ TESTING ~~
        print('\nget_search_list\n', responseBody)
        print('response.status_code: ', response.status_code)
        
        return responseBody
    
    
    
    ## @fn user_login : Will 
    # 
    # :required -
    # :required -
    # :required -
    #
    def user_login(self):
        # URL end point.
        url = self.environment + QaADPQShell.UsersLogin

        # HTTP Action.
        HTTP_action = 'POST'
        
        # Header Parameters.
        headers = {
            'Content-Type' : 'application/json',
            'Cache-Control': 'no-cache'#,
            #'ClientId' : self.ClientID
        }
        
#         # Add the ClientId header parameter.
#         if ClientIdExclude == True:
#             pass
#         elif ClientId != '':
#             body['ClientId'] = self.ClientId
#         else:
#             body['ClientId'] = ''
        
        
        # Dynamically set key/value body pairs. Add all body parameters.
        # Null values indicates the field was left blank.
        body = {}
        
#         # Add the network body parameter.
#         if networkExclude == True:
#             pass
#         elif network != '':
#             body['network'] = network
#         else:
#             body['network'] = ''
#             
#         # Add the email body parameter.
#         if emailExclude == True:
#             pass
#         elif email != '':
#             body['email'] = email
#         else:
#             body['email'] = ''
#             
#         # Add the password body parameter.
#         if passwordExclude == True:
#             pass
#         elif password != '':
#             body['password'] = password
#         else:
#             body['password'] = ''
            
        # Make HTTPS Request.
        response = requests.request(HTTP_action, url, json=body, 
                                    headers=headers, verify=False)
    
        # Return requests object of json data.
        responseBody = response.json()
        
        # ~~ TESTING ~~
        print('\nuser_login\n', responseBody)
        print('response.status_code: ', response.status_code)
        
        
#         # Assertion - only if request was successful.
#         if 'error' in responseBody.keys():
#             if response.status_code == 200 and responseBody['error'] == False:
#                 # Capture the objects information for future use.
#                 self.AuthKey = responseBody['authorizeKey']
#                 self.email = responseBody['data']['email']
#                 self.UserID = responseBody['data']['id']
#                 self.UserNetwork = responseBody['data']['network']
#                 self.password = password
        
        return responseBody
    
    
    
    
    
    
    
    
    

## @fn Test_Class()  
# Test_Class function allows the user to 'test drive' every class 
# method above. This function provides example calls. 
# Above each class method call is the method signature.
# 
#     
def Test_Class():
    # Declare class objects. Create class instance. DONE
    user = QaADPQShell()
    
    # Stage one (LANDING PAGE END POINTS)
    user.get_agency_list()
    user.get_tag_list()
    user.get_article_list()
    user.get_search_list()
    user.user_login()
    
    
#     # Method signature. 
#     # remove_user(self, email=''):
#     user.remove_user(user.testEmail)
    
    
    
Test_Class()