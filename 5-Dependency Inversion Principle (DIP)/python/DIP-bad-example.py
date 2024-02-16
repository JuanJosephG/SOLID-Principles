class PostManager:
    def __init__(self):
        self.post_service = PostService()

    def create_and_display_post(self, content):
        post = self.post_service.create_post(content)
        self.post_service.display_post(post)