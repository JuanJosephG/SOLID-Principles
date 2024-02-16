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
  
    display() {
      // Logic specific to displaying an image post
    }
  }