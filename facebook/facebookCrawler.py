import facebook #pip install facebook-sdk
import json

#Archivos
postsFile = open('posts.txt', 'w')
likesFile = open('likes.txt', 'w')
commentsFile = open('comments.txt', 'w')

#To obtain the access token enter to the url: https://developers.facebook.com/tools/explorer
accessToken = ''
graph = facebook.GraphAPI(access_token=accessToken, version='2.2')

profile = graph.get_object("hamburguesaselcorral")
print(profile)

name = profile['name'] # Get name
print(name)

profile = graph.get_object(profile['id'])
print(profile)

posts = graph.get_object(profile['id']+"/posts")
Jstr = json.dumps(posts)
JDict= json.loads(Jstr)

print("posts:")
print(Jstr)
print(JDict)

print("Mensajes:")
for post in JDict['data']:
   try:
       postsFile.write(json.dumps(post['created_time']) + " " + json.dumps(post['message']) + "\n")
       likes = post['likes']

       for like in json.loads(json.dumps(likes))['data']:
           #print like
           #likesFile.write(json.dumps(like)+"\n")
           likeProfile = graph.get_object(like['id'])
           likesFile.write(json.dumps(likeProfile)+"\n")
           #print json.dumps(likeProfile)
           #break

       comments = post['comments']
       for comment in json.loads(json.dumps(comments))['data']:
           print(comment)
           commentsFile.write(json.dumps(comment)+"\n")
   except :
       print("")
