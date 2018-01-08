
# coding: utf-8

# In[31]:

import pytest
import httpclient


# In[29]:

class TestHttpClient(object):
    def setup(self):
        print("setup httpclient")
        self.hc = httpclient.HttpClient()
        self.hc.setParams(directory="/", method="GET")
    def test_setparams(self):
        assert self.hc.params["directory"] == "/"
        assert self.hc.params["method"] == "GET"
        assert self.hc.params["headers"] == {"Content-Type" : "application/json"}
    def test_request(self):
        assert self.hc.request() == '{"hello":"world"}'
    def teardown(self):
        self.hc = None
        print("teardown httpclient")


# In[ ]:



