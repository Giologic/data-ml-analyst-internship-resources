from posts import PostsModel

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