import json


def removekey(d, key):
  r = dict(d)
  del r[key]
  return r

class PostsModel:

  def __init__(self):

    # Extract data from JSON file
    self.posts = {}
    self.initializePostsModelData()

  def initializePostsModelData(self):
    # Load json data to Posts Model
    json_data = []
    with open('data.json') as json_file:
      json_data = json.load(json_file)
    
    for obj in json_data:
      self.posts[obj.get('id')] = obj

  def getHighestKey(self):
    # Retrieve the highest key value
    hightestNum = None
    if(len(self.posts) > 0):
      for k,v in self.posts.items():
        if hightestNum == None:
          hightestNum = k
        elif hightestNum < k:
          hightestNum = k
    
    return hightestNum

  def generateNextKey(self):
    # Generate a key iterated from the value of the highest key
    return self.getHighestKey() + 1

  def getPosts(self):
    # Return all posts
    return self.posts

  def getPost(self, id):
    # Returns a post given its ID
    post = None
    try:
      self.posts[id]
    except:
      print("Post does not exist!") 
  

  def createPost(self, params):
    # Creates a new post and returns the created post
    newId = self.generateNextKey()
    params.update({'id': newId })
    self.posts[newId] = params
    return self.posts[newId]

  def updatePost(self, id, params):
    # Update the post given its id and returns the updated post
    for key,value in params.items():
      try:
        self.posts[id].update({key: value})
      except KeyError:
        print("Post does not exist")
      except Exception:
        print("Wrong parameters. Please check the format of your dictionary")

      return self.posts[id]

  def deletePost(self, id):
    # Deletes a post given its id
    del(self.posts[id])

      
# INSTANTIATE
postsModel = PostsModel()

# GET ALL
print(postsModel.getPosts())

# GET SPECIFIC
print(postsModel.getPost(id=1))

# POST
print(postsModel.createPost({'userId': 10, 'title': 'quas fugiat ut perspiciatis vero provident', 'body': 'eum non blanditiis soluta porro quibusdam voluptas\nvel voluptatem qui placeat dolores qui velit aut\nvel inventore aut cumque culpa explicabo aliquid at\nperspiciatis est et voluptatem dignissimos dolor itaque sit nam'}))

# PUT/PATCH
postsModel.updatePost(1, params={'userId': 10})

# DELETE
postsModel.deletePost(1)

# CHECK IF DELETED
print(postsModel.getPost(1))


  