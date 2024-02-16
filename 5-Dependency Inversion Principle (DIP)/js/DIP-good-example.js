// JavaScript Good Example
class PostManager {
    constructor(postService) {
      this.postService = postService;
    }
  
    createAndDisplayPost(content) {
      const post = this.postService.createPost(content);
      this.postService.displayPost(post);
    }
  }