class PostManager {
    constructor() {
      this.postService = new PostService();
    }
  
    createAndDisplayPost(content) {
      const post = this.postService.createPost(content);
      this.postService.displayPost(post);
    }
  }