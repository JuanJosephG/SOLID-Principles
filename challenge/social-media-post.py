## Description: 

class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author

class SocialMediaApp:
    def __init__(self):
        self.posts = []

    def create_post(self, content, author):
        post = Post(content, author)
        self.posts.append(post)

    def display_posts(self):
        for post in self.posts:
            print(f"{post.author}: {post.content}")

class User:
    def __init__(self, name):
        self.name = name

    def create_post(self, app, content):
        app.create_post(content, self.name)

    def view_posts(self, app):
        app.display_posts()