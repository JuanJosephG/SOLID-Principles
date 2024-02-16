class Post {
    constructor(content) {
      this.content = content;
    }
  
    display() {
      // Logic to display the post
    }
  }
  
  class ImagePost extends Post {
    constructor(content, imageUrl) {
      super(content);
      this.imageUrl = imageUrl;
    }
  
    // No display method overridden here
  }