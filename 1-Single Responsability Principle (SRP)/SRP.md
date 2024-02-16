## Definition:
The Single Responsibility Principle (SRP) states that a class should have only one reason to change, meaning it should have only one responsibility in the system. High-level modules should not depend on low-level modules; both should depend on abstractions.

## Problem Statement:
Consider a social media application where users can create posts, and the application displays those posts. The problem arises when the class responsible for managing posts is also responsible for displaying them. This violates SRP because the class has multiple reasons to change: managing posts and displaying them.


## Why it's bad: 
In the bad example, the Post class has both the responsibility of creating a post and displaying it. This violates SRP because a class should have only one reason to change, but here it would need modification if the logic for creating or displaying posts changes.

## Good Example:
In the good example, we have separate classes for creating posts (PostCreator) and displaying posts (PostDisplayer). Each class has a single responsibility, making the code more maintainable and less prone to modification.