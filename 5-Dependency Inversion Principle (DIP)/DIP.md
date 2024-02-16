## Definition:
The Dependency Inversion Principle (DIP) states that high-level modules should not depend on low-level modules; both should depend on abstractions. This principle encourages the use of abstractions (e.g., interfaces or abstract classes) to decouple high-level modules from specific implementations of low-level modules.

## Problem Statement:
Consider a social media application where a PostManager class is responsible for creating and displaying posts. The PostManager class directly depends on the concrete implementation of the PostService class. This violates the DIP because the high-level PostManager class depends on a low-level PostService class.

## Abstraction:
To adhere to DIP, we can create the following abstractions:

1. PostService interface:
- Responsibilities: Define methods for creating and displaying posts.

2. PostManager class:
- Responsibilities: Use the PostService interface to create and display posts without depending on its concrete implementation.

## Why it's bad: 
The bad example violates DIP by directly instantiating the PostService within the PostManager class. This creates a tight coupling between PostManager and PostService, making it difficult to change or substitute implementations of PostService.

## Why it's good: 

In the good example, we inject the PostService into the PostManager class through dependency injection. This adheres to DIP by allowing PostManager to depend on abstractions rather than concrete implementations, making the code more flexible and easier to maintain.