# Python Good Example
class Post:
    def __init__(self, content):
        self.content = content

    def publish(self):
        # Logic to publish the post
        pass

class ImagePost(Post):
    def __init__(self, content, image_url):
        super().__init__(content)
        self.image_url = image_url

    def publish(self):
        # Logic specific to publishing an image post
        pass