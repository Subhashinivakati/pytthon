import requests
import json
def get_data():
    API_URL="https://jsonplaceholder.typicode.com/posts"
    resp=requests.get(API_URL)
    #return resp
    if resp.status_code == 200:
        data=resp.json()
        return data
    else:
        print('error')

    
post=get_data()
if post:
 for i in range(0,100):
    print("user ID:",post[i]['userId'])
    print("ID:",post[i]['id'])
    print("Title:",post[i]['title'])
    print("Body:",post[i]['body'])
    print("=====================")
else:
    print('failed to fetch the data')
