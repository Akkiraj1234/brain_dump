## topics 
1. [oops](#python-oops-consepts)
2. [modules](#python-modules-and-structure)
3. **[go back](./_content_.md)**


---

# Python OOPs Consepts
so in simple work oops is a programing pardigma that uses object and classes in programing which allow inheritance, polymorphsms, encapsulation, abstraction is called oops (object orianted prograimng)

### -> oops concepts in pyton:
  - [class](#class)
  - [objects](#objects)
  - [Encapsulation](#encapsulation)
  - [Inheritance](#inheritance)
  - [Polymorphism in python](#polymorphism-in-python)
  - [Data abstraction](#data-abstraction)
  - [glossary](#glossary)
  
## class 
A class is a blueprint for creating objects that contain attributes (data) and methods (functions). 
- contain **attributes**, **methods**, and **dunder methods**..
- All Python classes implicitly inherit from the built-in object class if no parent class is specified.
- Protects the internal data of a class from being directly accessed or modified.
- `self` Refers to the instance of the class calling the method. pass as first parameter in method.
```python
class Dog:  # Implicitly inherits from 'object'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

# Creating an object
dog1 = Dog("Buddy", 5)
print(dog1.bark())  # Output: Buddy says woof!
```
## objects
An object is an instance of a class in Python, It represents a real-world entity.

- Memory is allocated only when an object is created from that class
- an object is created when u call a class that invoke `__init__` method and create the object
- every object contain unique id, get it by `id()`
- The object exists as long as it is referenced in memory. after its became eligiable for garbage collector
```python
class Car:
    def __init__(self):
        pass

    def display_info(self):
        return f":) i am a car of {id(self)} id"

# Creating objects of the Car class
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2021)

print(car1.display_info())  # i am a car of 1200093 id 
print(car2.display_info())  # i am a car of 1239040 id
```

## Encapsulation
describe the idea of wrapping data and the method that work or data within. 1 unit this restriction or accsessing variable and method directly pervent data modification

### Purpose of Encapsulation
1. **Data Protection**: By limiting direct access to an object's data. This prevents external code from modifying an object's state in unpredictable ways.
2. **Abstraction**: Encapsulation allows an object to expose only what is necessary to the outside world.

### Access Modifiers in Python

Python does not have explicit access modifiers, but it's uses naming conventions to indicate access levels:

1. **Public:** Default access, no prefix (`object.attribute`).
2. **Private:** Double underscore prefix (`__attribute`), accessible only within the class.
3. **Protected:** Single underscore prefix (`_attribute`), intended for internal use but accessible from outside the class.

### Accessing Private Attributes
Private attributes can't be accessed directly. Use getters, setters, or name mangling:

- **Getter Methods:** Retrieve the value.
- **Setter Methods:** Set or modify the value.
- **Name Mangling:** Use `obj._class__fun()` to access `obj.__fun()` without raising an AttributeError.

## Inheritance
it's a mechanisam that allow you to create hierachy of classes that share a set of properties and methods by driving a class from another class, uses mro prinicile. 

```python
#syntax: 
class new_class(parent_class):
```
### `super()` keyword
set a proxy conection inside a class to access parent class artibutes, methods and dunder. helpfull in method overloading
```python
class new_class(parent_class):
    def __init__(*args, **kwargs):
        super().__init__(*args, **kwargs)
```

### Types inheritance:
1. **Single Inheritance**: When a class inherits from one parent class. 
2. **Multiple Inheritance**: When a class inherits from more than one parent class.
3. **Multilevel Inheritance**: When a class inherits from a subclass, forming a chain.
4. **Hierarchical Inheritance**: When multiple classes inherit from the same parent class.
5. **Hybrid Inheritance**: When a class inheriatance is combind of 2 or more differnt type of inheritance.



### Extra Info 
- **python3.x** : Uses a consistent C3 linearization MRO for all classes. `ex: class A == Class A(object)`
- **python2.x** : Must explicitly inherit from object to create new-style classes. `ex: class A != Class A(object)`

## Polymorphism in python
The word is a greek word where polymore means having many faces and morph mean form so its means when a class have more then 1 face is called polymorphism
1. **inheritance :** a child class coude be treated same as parent class 
2. **Duck Typing :** object must have nessessary attributes method to get in a catogery "if it's looks like a duck and quack like a duck, it's muct be a duck"

## Data abstraction
abstraction focuses on hiding the implementation details of a class and exposing only the essential features or functionalities to the user. The goal is hide the complex logic or internal workings hidden.
**we can achive this by implementing `abc` module**

### Implementing Abstraction in Python
Python provides the abc module (Abstract Base Classes) to create abstract classes and methods.

- **Abstract Class**: A class that serves as a blueprint and contains at least one abstract method.
- **Abstract Method**: A method declared in an abstract class but not implemented.

```python
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod # Abstract method
    def area(self):
        pass

    def display(self): # Concrete method
        print("This is a shape")

# Subclass implementing the abstract class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width, self.height = width, height

    # Implementing the abstract method if not implement raise an error
    def area(self):
        return self.width * self.height

# Trying to create an object of the abstract class will raise an error
# shape = Shape()  # TypeError

# Create an object of the subclass
rect = Rectangle(5, 10)
print(rect.area())  # Output: 50
rect.display()  # Output: This is a shape
```
in simple term if u dont write @abstractmethod method in new class that will raise error... 

## glossary
1. **Aggregation:** represents a "has-a" relationship between two classes. It allows a class to use objects of another class as attributes while both can exist independently. The lifecycle of the contained object is not dependent on the containing object.

2. **Composition:** Composition is a strong form of aggregation where the lifecycle of the contained object is tightly bound to the containing object. If the containing object is destroyed, the contained object is also destroyed.

3. **Nested Class:** A nested class is a class defined inside another class. It is used to logically group classes that are only relevant within the context of the outer class and are not meant to be used independently.

4. **Method Overloading:**  Method overloading refers to the ability to define multiple methods with the same name but with different arguments. Python mimics this behavior using default or variable-length arguments.

5. **Method Overriding:** Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its parent class. The subclass version replaces the parent class version for instances of the subclass.

6. **Operator Overloading:** Operator overloading allows customizing the behavior of operators (e.g., +, -, ==, etc.) for user-defined objects by redefining special dunder methods such as `__add__` or `__eq__`.

7. **class_variable**: means shared amoney all instance of a class defined outside the constructor allow `class_variable`

8. **static varaible**: shared to the main python can be asses and call from any class create it as gloable method `static_variable`

9.. **constructor**: means __init__ its call automaticlly when obj is created

---
# python modules and structure.
- A module is a single .py file containing Python definitions and code (e.g., functions, classes, variables) that can be reused in other programs.
- Modules allow code reuse, better organization, and namespace management.

### Why Use Modules?
- **Code Reusability**: Write once, use anywhere.
- **Modularity**: Break down large programs into smaller, manageable parts.
- **Maintainability**: Easier to update or debug parts of a program.
- **Avoid Naming Conflicts**: Each module has its own namespace.

### Creating and Using a Module
1. **Create a Module**: Create a Python file (example.py) with code:
    ```python
    # example.py
    def greet(name):
        return f"Hello, {name}!"
    ```
2. **Import and Use the Module**: In another script or interactive session:
    ```python
    import example
    print(example.greet("Alice"))  # Output: Hello, Alice!
    ```
### Best Practices for Writing Modules
1. **Single Responsibility**: Each module should focus on a specific task or related tasks.

2. **Clear Naming**: Use descriptive names in lowercase, e.g., math_tools.py.

3. **Document Your Module:** Add a module-level docstring at the top

4. Use `if __name__ == "__main__":` to prevent automatic code execution when imported.

5. **Centralized Exports**: Re-export all functions and classes from multiple modules in one place (e.g., **utils.py**) and use them from tere.
    ```python
    from .module_a import function_a
    from .module_b import function_b
    from os import path

    __all__ = ["function_a", "function_b", "path"]
    ```

6. **Modify Module Search Path**: Add directories to sys.path dynamically for better importing.

### Module Attributes
Access special attributes:
- `__name__`: Name of the module.
- `__file__`: Path to the module file.
- `__doc__`: Docstring of the module.

### Differnace between python `fille`, `module` and `package`

1. What Is a Python File?
   - **Definition**: A Python file is any file with the .py extension that contains Python code. It could contain definitions (functions, classes, variables) or just scripts that execute some logic.
   - A Python file is not necessarily reusable unless it's structured as a module.
   - It might serve as an entry point (like main.py) or a utility script.
  
2. What Is a Module?
   - **Definition**: A module is a Python file intended for reusability, containing functions, classes, or variables that can be imported into other scripts or modules.
   - Any Python file (.py) can be treated as a module if it’s imported.
   - A module has its own namespace to prevent naming conflicts.
   - If a file isn’t imported or reused, it’s just a script, not a module.

3. What Is a Package?
   - **Definition**: A package is a directory (folder) containing a special `__init__.py` file, which can contain multiple modules or sub-packages. It provides a way to organize and group related modules hierarchically.
   - A package allows you to structure your project logically, especially when it grows large.
   - **packages can contain**: Modules (.py files) and Sub-packages (folders with their own `__init__.`py).
   - A module is a single file, while a package is a directory.

#### Comparison Table
| **Feature**        | **Python File**                 | **Module**                     | **Package**                       |
|---------------------|---------------------------------|---------------------------------|------------------------------------|
| **Definition**      | Any `.py` file.                | A reusable Python file.        | A folder with an `__init__.py`.   |
| **Key Use**         | Standalone script.             | Reusable code.                 | Group related modules.            |
| **Structure**       | Single `.py` file.             | Single `.py` file.             | Directory with `__init__.py`.     |
| **Imports**         | Cannot be directly imported.   | Can be imported.               | Modules inside can be imported.   |
| **Example Import**  | N/A                            | `import my_module`             | `from my_package import module`   |
| **Contains**        | Code or logic.                 | Definitions (functions, etc.). | Modules and/or sub-packages.      |

### Organizing Modules in Projects
#### Project Structure Example: 
```bash
my_project/
├── __init__.py       # Marks the folder as a package
├── main.py           # Entry point
├── utils/            # Subpackage for utilities
│   ├── __init__.py   # Centralized exports for utils
│   ├── math_tools.py # Math utilities
│   └── string_tools.py # String utilities
```
**tho its part of packaging that u will learn later but just rember for rn you can structure it like that.**

## will write in future 
1. mro future 
2. name mangaging 
3. Thread-safe classes
4. Using threading and multiprocessing with class-based designs
5. Coroutines and asynchronous classes with asyncio
6. advance abstract class

author: @Akkiraj1234