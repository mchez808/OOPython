# Object Oriented Python
to demonstrate fundamentals of Object Oriented Design: inheritance, encapsulation, polymorphism, and abstraction

## Why OOP?
As programs become more complex, it becomes increasingly more difficult to keep details organized,
as well as ensuring that changes in one place do not have unintended side effects on another part of the software.
This OO structured approach improves planning and maintainability, and reduces bugs,
by grouping data and behavior together in one place. 

OO Design promotes **modular** programming, so that one module only interacts with the information on a *need to know* basis.
This way, one module can be modified later with minimal disturbances to the rest of the code base.

### Composition
An important OOP term, *Composition* refers to building complex objects out of other objects.

# Polymorphism
* relies on inheritance
* allows child classes to be instantiated and treated as the same type as its parent
* * i.e., it enables a parent class to be manifested into any of its child classes.
* * e.g., if I use a pet class, and I don't need to know 
if the pet object is a dog or cat until the runtime.
* * This is because the true nature of the object is hidden, until its `speak()` method is invoked.

From the course: *Python: Design Patterns*
Lesson: *Working with inheritance and polymorphism*
by Jungwoo Ryoo