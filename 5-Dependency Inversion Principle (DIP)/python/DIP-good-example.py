# Python Good Example
class PostManager:
    def __init__(self, post_service):
        self.post_service = post_service

    def create_and_display_post(self, content):
        post = self.post_service.create_post(content)
        self.post_service.display_post(post)