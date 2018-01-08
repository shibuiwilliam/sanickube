
# coding: utf-8

# In[1]:

from sanic import Sanic
from sanic.response import json


# In[2]:

app = Sanic()


# In[3]:

@app.route("/")
async def test(request):
    return json({"hello": "world"})


# In[4]:

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)


# In[ ]:



