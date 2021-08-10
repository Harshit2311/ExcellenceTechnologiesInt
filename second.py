import requests


def countUser(myDict):
    return len(myDict['data'])

def Users():
    count = 0
    for i in range(1,13):
        myUrl = 'https://reqres.in/api/users?page=' + str(i)
        readata= requests.get (myUrl)
        myInfo = readata.json()
        no_of_user = countUser(myInfo)
        count += no_of_user
    return count

if __name__ == "__main__":
    total_number_of_user = Users()
    print("total no of user is ",total_number_of_user)

"""
Output Will be
total no of user is  12
"""