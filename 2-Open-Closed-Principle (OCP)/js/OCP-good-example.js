// JavaScript Good Example
class Post {
    constructor(content) {
      this.content = content;
    }
  
    publish() {
      // Logic to publish the post
    }
  }
  
  class ImagePost extends Post {
    constructor(content, imageUrl) {
      super(content);
      this.imageUrl = imageUrl;
    }
  
    publish() {
      // Logic specific to publishing an image post
    }
  }

  class TextPost extends Post {
      constructor(content, description) {
        super(content);
        this.drescription = description;
      }
    
      publish() {
        // Logic specific to publishing an image post
      }
  }