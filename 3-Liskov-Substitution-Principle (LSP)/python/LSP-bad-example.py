class Post:
    def __init__(self, content):
        self.content = content

    def display(self):
        # Logic to display the post
        pass

class ImagePost(Post):
    def __init__(self, content, image_url):
        super().__init__(content)
        self.image_url = image_url