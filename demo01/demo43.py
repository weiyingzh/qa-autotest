import json

with open('demo.json') as f:
    users = json.load(f)
    # print(users)
    for user in users:
        # print(user)
        print(user['username'], user['password'])