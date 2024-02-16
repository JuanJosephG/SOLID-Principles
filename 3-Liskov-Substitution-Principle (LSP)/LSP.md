## Definition:
The Liskov Substitution Principle (LSP) states that objects of a superclass should be replaceable with objects of its subclass without affecting the correctness of the program. In other words, a subclass should be substitutable for its superclass without altering the behavior of the program.

## Problem Statement:
Consider a social media application where posts can be of different types, such as text posts and image posts. The Post class defines a method display() to display the post. Later, an ImagePost class is created as a subclass of Post, but it does not override the display() method. This violates the LSP because an ImagePost object cannot be fully substituted for a Post object without altering the behavior of the program.

## Abstraction:
To adhere to LSP, we can create the following abstractions:

1. Post class:  Represent a single post with its content. It defines a method to display the post.

2. ImagePost class:  Extend the Post class to handle image posts specifically. It should override the display() method to provide specific behavior for displaying image posts.

## Why it's bad: 
The bad example violates LSP by not overriding the display() method in the ImagePost subclass. This means that an ImagePost object cannot be substituted for a Post object without affecting the correctness of the program.

## Why it's good: 
In the good example, both the Post and ImagePost classes override the display() method, ensuring that an ImagePost object can be used interchangeably with a Post object without any unexpected behavior.