# Bad Example
class Post:
    def __init__(self, content):
        self.content = content

    def publish(self):
        # Logic to publish the post
        pass

    # Later, adding a new type of post directly in Post class
    def publish_image_post(self, image_url):
        # Logic specific to publishing an image post
        pass