# Python Requests Library is a simple and powerful tool to send HTTP requests and interact with web resources. 
# It allows you to easily send GET, POST, PUT, DELETE, PATCH, HEAD requests to web servers, handle responses, and work with REST APIs and web scraping tasks.
"""""
Syntax
requests.get(url, params={key: value}, **kwargs)

Parameter:

url: The URL you want to send the request to. (Required)
params: Dictionary or bytes to be sent in the query string for GET requests. (Optional)
**kwargs: Additional optional arguments such as headers, cookies, authentication, timeout, proxies, verify (SSL), stream, etc."""""


import requests
response = requests.get("https://www.geeksforgeeks.org/")
print(response.status_code)
print(response.content)
print(response.ur)