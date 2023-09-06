import requests 

r=requests.get(('http://ip.jsontest.com'))
print('Response Object:',r)
print('Response Text:',r.text)

#request with payload
payload={'q':'sahvsergio'}
r=requests.get('https://github.com/search',params=payload)
print('Requests URL:',r.url)


#post request with payload, which is similar to filling up and posting a login or signup form on a website
payload={'key':'value1'}
r=requests.post('http://httpbin.org/post', data=payload)
print('Response text:',r.json())
"""
try:
    r=requests.get('http:www.google.com/')
except:
"""
payload={'s':'saw'}
r=requests.get('https://www.bloghorror.com', params=payload)
print('Requests URL:',r.url)
print('Requests text:',r.text)

