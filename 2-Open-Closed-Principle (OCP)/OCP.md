## Definition:
The Open/Closed Principle (OCP) states that software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. This means that the behavior of a module can be extended without modifying its source code.

## Problem Statement:
Consider a social media application where users can create different types of posts, such as text posts and image posts. Initially, the Post class only handles text posts. However, later on, the requirement arises to support image posts. Instead of extending the behavior of the Post class, the logic for publishing image posts is directly added to the Post class. This violates the OCP because the class is modified instead of being extended.

## Abstraction:
To adhere to OCP, we can create the following abstractions:

1. Post class:  Represent a single post with its content and author. It should be open for extension to support different types of posts.

2. TextPost class:: Extend the Post class to handle text posts specifically.

3. ImagePost class: Extend the Post class to handle image posts specifically.


## Why it's bad: 
The bad example violates OCP by directly modifying the Post class to add new functionality (publishImagePost). This requires changing the existing class, which can lead to unintended consequences and violates the principle of being closed for modification.

## Why it's good: 
In the good example, we extend the Post class to create a new ImagePost class. This adheres to OCP because we're extending functionality without modifying existing code, ensuring that the original Post class remains closed for modification.