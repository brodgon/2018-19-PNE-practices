import http.client
import json

HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
GITHUB_ID = input("Insert your github user to obtain some information: ")
METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT + GITHUB_ID, None, headers)

r1 = conn.getresponse()

print()
print("Response received: ", end='')
print(r1.status, r1.reason)

text_json = r1.read().decode("utf-8")
conn.close()

user = json.loads(text_json)

login = user['login']
name = user['name']
bio = user['bio']
nrepos = user['public_repos']
reposurl = user['repos_url']

print()
print("User: {}".format(login))
print("Name: {}".format(name))
print("Repos: {}".format(nrepos))
print("Repository url: {}".format(reposurl))
print("Bio: \n{}".format(bio))

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT + GITHUB_ID + "/"+"repos", None, headers)

r1 = conn.getresponse()
text_json = r1.read().decode("utf-8")
conn.close()
repos = json.loads(text_json)
reponames = []
for i in range(len(repos)):
    reponames.append(repos[i]['name'])
reponame = repos[0]['name']
commits = repos[0]['size']
print("This user has {} public repositories".format(len(repos)))
print("His/her repositories are: ", "\n","\t", reponames)
print("In {} we find {} commits".format(reponame, commits))
