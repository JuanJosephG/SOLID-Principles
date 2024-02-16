# Python Good Example
class Post: ## Father
    def __init__(self, content):
        self.content = content

    def display(self):
        # Logic to display the post
        pass

class ImagePost(Post): #child
    def __init__(self, content, image_url):
        super().__init__(content)
        self.image_url = image_url

    def display(self):
        # Logic specific to displaying an image post
        pass

    def get_image_url_using_db(self):
        pass