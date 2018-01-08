
# coding: utf-8

# In[1]:

import urllib.request
import json


# In[7]:

class HttpClient(object):
    def __init__(self, url="localhost", port=str(8000)):
        self.url = "http://" + url + ":" + port
        self.params = {"directory": "/"} 
    def setParams(self, 
               directory="/", 
               method="GET", 
               headers={"Content-Type" : "application/json"}):
        self.params["directory"] = directory
        self.params["method"] = method
        self.params["headers"] = headers
    def request(self, data=None):
        reqFullUrl = self.url + self.params["directory"]
        request = urllib.request.Request(self.url, data=data, method=self.params["method"], headers=self.params["headers"])
        with urllib.request.urlopen(request) as response:
            response_body = response.read().decode("utf-8")
            return response_body


# In[ ]:



