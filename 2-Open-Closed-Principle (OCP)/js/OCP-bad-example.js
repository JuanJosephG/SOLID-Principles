// Bad Example
class Post {
  constructor(content) {
    this.content = content;
  }

  publish() {
    // Logic to publish the post
  }
}

// Later, adding a new type of post directly in Post class
Post.prototype.publishImagePost = function(imageUrl) {
  // Logic specific to publishing an image post
};