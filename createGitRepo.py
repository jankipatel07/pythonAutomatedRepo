import requests
import json

#https://api.github.com/repos/{owner}/{repo}

def createNewRepo():
    url = 'https://api.github.com/user/repos'
    git_token = 'token TOKEN'
    myobj = {'name': 'pythonAutomatedRepo', 'description': 'Created with Github API', 'auto_init': 'true'}
    header = {'Authorization': git_token}

    res = requests.post(url, headers=header, data=json.dumps(myobj))
    print(res.json())

# curl \
#   -H "Authorization: token TOKEN" "Accept: application/vnd.github.v3+json" \
#   https://api.github.com/user/repos

def getRepoList():
    usr_repos = 'https://api.github.com/users/jankipatel07/repos'
    repoData = requests.get(usr_repos).json()
   
    for index in range(len(repoData)):
        print('{} repository is private or not: {}'.format(repoData[index]['name'], repoData[index]['private']))


createNewRepo()

if __name__ == '__main__': 
    getRepoList()
