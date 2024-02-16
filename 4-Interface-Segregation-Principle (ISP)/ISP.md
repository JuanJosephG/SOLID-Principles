## Definition:
The Interface Segregation Principle (ISP) states that clients should not be forced to depend on interfaces they do not use. Instead of having one large interface that covers all possible operations, it's preferable to have several smaller, more specific interfaces.

## Problem Statement:
Consider a social media application where posts can be created and displayed. The Post class defines methods for both creating and displaying posts. However, not all clients may need both functionalities. This violates the ISP because clients may be forced to depend on methods they do not use.

## Abstraction:
To adhere to ISP, we can create the following abstractions:

1. PostCreation interface:
- Responsibilities: Define a method for creating a new post.

2. PostDisplay interface:
- Responsibilities: Define a method for displaying a post.


## Why it's bad: 
The bad example violates ISP by having a single interface (Post) that includes methods for both creating and displaying posts. This forces clients to depend on methods they may not use, leading to unnecessary coupling and potential code bloat.

## Why it's good: 
In the good example, we have separate interfaces (PostCreator and PostDisplayer) for creating and displaying posts, respectively. This allows clients to depend only on the interfaces they need, reducing coupling and keeping the codebase more cohesive.
