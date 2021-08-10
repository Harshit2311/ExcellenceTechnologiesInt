import requests

def mixData(postData, comments):
    myDict={}
    result = []
    for p in postData:
        info = {}
        cList = []
        if 'id' in p and 'title' in p:
            info['id'] = p.get('id')
            info['title'] = p.get('title')
            for c in comments:
                cinfo = {}
                if 'postId' in c and p['id'] == c['postId']:
                    cinfo['id'] = c.get('id')
                    cinfo['body'] = c.get('body')
                    cinfo['postId'] = c.get('postId')
                    cList.append(cinfo)
            if len(cList) != 0:
                info['comment'] = cList
        result.append(info)
    myDict['post'] = result
    return myDict

def getMixData():
    postdata= requests.get ('https://my-json-server.typicode.com/typicode/demo/posts')
    comment= requests.get ('https://my-json-server.typicode.com/typicode/demo/comments')
    p = postdata.json()
    c =comment.json()
    value = mixData(postData=p, comments=c)
    return value

if __name__ == "__main__":
    data = getMixData()
    print(data)

""" 
Output will be:

{'post': [{'id': 1, 'title': 'Post 1', 'comment': [{'id': 1, 'body': 'some comment', 'postId': 1}, {'id': 2, 'body': 'some 
comment', 'postId': 1}]}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]}
"""


