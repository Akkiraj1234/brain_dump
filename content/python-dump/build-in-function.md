**[`back`](./_content_.md)**
# All Build-in funtion in python
there are all build in python function and dunder

## Numeric Functions
- `abs()`: Returns the absolute value of a number and magnitude of complex number.
- `complex()`: Creates a complex number.
- `divmod()`: Returns a tuple containing the quotient and remainder when dividing two numbers.
- `float()`: Converts a value to a floating-point number.
- `pow()`: Returns the result of raising a number to a power. *0 (log y)*
- `int()`: Converts a value to an integer.
- `round()`: Rounds a number to the nearest integer or specified number of decimal places.

## Iterable/Collection Functions
- `all()`: Returns True if all elements in an iterable are true.
- `any()`: Returns True if any element in an iterable is true.
- `enumerate()`: Adds a counter to an iterable and returns it as an enumerate object.
- `iter()`: create an iterator by object which object should contain __iter__ dunder. *o(1)*
- `next()`: for accseig the next part of iterator. *o(1)*
- `range()`: Returns a sequence of numbers.
- `filter()`: Constructs an iterator from elements of an iterable for which a function returns true.
- `map()`: Applies a function to every item in an iterable.
- `sorted()`: Returns a sorted list.
- `reversed()`: Returns a reversed iterator.
- `list()`: Creates a list.
- `tuple()`: Creates a tuple.
- `zip()`: Combines multiple iterables.

## Iterable Numeric function
- `slice()`: Returns a slice object.
- `len()`: Returns the number of items in an object. call __len__ method of object
- `sum()`: Returns the sum of an iterable's elements.
- `max()`: Returns the largest of the input values.
- `min()`: Returns the smallest of the input values.
  

## Boolean and Bytes
- `bool()`: return True if an object is Truthy else False.
- `bin()`: Return the binary representation of an integer. as string. time: *o(log n)*
- `bytearray()`: returns a *mutable* sequence of bytes. which stores integers in the range of 0 to 255.
- `bytes()`: returns a *imutable* sequence of bytes. which stores integers in the range of 0 to 255.

  
## String Functions
- `ascii()`: return a string that includes only ASCII characters. other are escaped using \x, \u, or \U escape sequences.
- `hex()`: Converts an integer to a hexadecimal string.
- `chr()`: Returns the character for a specified Unicode code. in range of 0 to 1,114,111 (0 to 0x10FFFF in hexadecimal).
- `oct()`: Converts an integer to an octal string. (base-8) *o(log n)*
- `ord()`: Returns the Unicode code of a single character. *o(1)*
- `str()`: Converts an object to a string. call the __str__ dunder of object.
- `format()`: Formats a specified value. check help('FORMATTING')

## Object and Class-Related Functions
- `classmethod()`: Converts a method to a class method. **decorator**
- `property()`: Returns a property attribute. **decorator**
- `staticmethod()`: Converts a method to a static method. it can be called without instance and class **decorator**
- `delattr()`: Deletes a specified attribute.
- `getattr()`: Returns the value of a specified attribute.
- `setattr()`: Sets the value of a specified attribute.
- `hasattr()`: Checks if an object has a specified attribute.
- `isinstance()`: Checks if an object is an instance of a class.
- `issubclass()`: Checks if a class is a subclass of another class.
- `object()`: Creates a new featureless object.
- [`super()`](#super-in-python-quick-notes): Returns a proxy object for the superclass of a class.
- `type()`: Returns the type of an object. or create new type


## Input/Output Functions
- `input()`: Reads input from the user.
- `open()`: Opens a file and returns a file object.
- `print()`: Prints objects to the text stream or another specified stream.
  
## Utility Functions
- `callable()`: Checks if an object is callable, return bool. *object appears to be callable if their class has a __call__() *dunder*
- [`memoryview()`](#memoryview-in-python-quick-notes): Returns a memory view object.
- `id()`: Returns the identity of an object.
- `vars()`: Shows the __dict__ of the object
- `dir()`: Returns a list of the attributes and methods of an object.
- `hash()`: Returns the hash value of an object.
- `eval()`: Evaluates a string as a Python expression.
- `exec()`: Executes Python code dynamically.
- [`compile()`](#compile-in-python-quick-notes): Compiles source into a code or AST object.
- `globals()`: Returns the current global symbol table as a dictionary.
- `locals()`: Returns the current local symbol table as a dictionary.
- `help()`: Invokes the built-in help system.
- `repr()`: The object for which you want to get the string representation. call __repr__ method of object.
- [`__import__()`]
- `mro()`: a method to get mro hiracy of a class
  (#importname-globalsnone-localsnone-fromlist-level0-in-python-quick-notes): The name of the module you want to import

  
## Set and Frozen Set Functions
- `set()`: Creates a set.
- `frozenset()`: Creates an immutable set.

## Special Methods / Magic Methods (Dunder Methods)

- `__init__(self)`:  It is automatically called when a new instance (object) of a class is created.

- `__str__(self)`: Returns a string representation of the object. by defult: object's type and memory address

- `__repr__(self)`: Returns an official string representation of the object. uses for debuging

- `__len__(self)`: Returns the length of the object.

- `__getitem__(self, key)`: Gets an item from the object using indexing. for creating custom slicing thing and through indexing how it will react key is slice instane

- `__setitem__(self, key, value)`: Sets an item in the object using indexing.

- `__delitem__(self, key)`: Deletes an item from the object using indexing.

- `__iter__(self)`: Returns an iterator object.

- `__next__(self)`: Returns the next item from an iterator.

- `__call__(self, *args, **kwargs)`: Makes an instance callable like a function.

- `__eq__(self, other)`,` __eq__(self, other)`,` __lt__(self, other)`, `__le__(self, other)`, `__gt__(self, other)`, `__ge__(self, other)`: well i know 

- `__add__(self, other)`: Defines the behavior for the addition operator +.

# code example and detail overview

## Memoryview() in Python: Quick Notes
### Overview:
- `memoryview` provides a way to access and manipulate data buffers (like `bytes`, `bytearray`, etc.) without copying the data.
- It allows efficient slicing, viewing, and modifying of large data sets by creating "views" instead of new copies.
###  Key Points:
- Works with Buffer Protocol Objects: bytes, bytearray, array.array, and other objects that support the buffer protocol.
- Memory Efficiency: Avoids data duplication, useful for large binary data operations.
- Supports Slicing: Allows for slicing and modification of data directly through the view.
- Immutable vs. Mutable: Immutable buffers (e.g., bytes) result in read-only memoryview objects, while mutable buffers (e.g., bytearray) allow modifications.
### Example Usage:
```python
Copy code
# Creating a memoryview of a mutable bytearray
data = bytearray(b'hello')
view = memoryview(data)

# Modify the original data via the memoryview
view[0] = ord('H')  # Changes 'hello' to 'Hello'
print(data)  # Output: bytearray(b'Hello')
```
### Use Cases:
- **Efficient Data Handling:** When working with large files (e.g., binary data or images) to avoid memory overhead from data duplication.
- **Buffer Slicing:** Access portions of data without creating new copies.
- **Interfacing with C Extensions:** Useful for efficient memory handling in C/C++ extensions or libraries that require buffer protocol support.
- **Modifying Binary Protocol Data:** For example, working with network protocols or binary file formats.

This makes memoryview ideal for performance-critical applications where minimizing memory usage and avoiding unnecessary data copies is important.

## Super() in python: Quick Notes
### Overview:
The super() function in Python is a built-in function that allows you to call methods from a parent or superclass within a child or subclass. This is particularly useful for extending or modifying the behavior of inherited methods without completely overriding them. It works mainly in the context of classes and inheritance.
### Key Points:
- **Primary Purpose:** super() gives you access to methods and properties of a parent class from within a child class.
- **Common Use:** It is often used in __init__() methods to initialize parent classes or in methods where you want to extend the functionality of the parent class without rewriting its code.
- Works with Multiple Inheritance: super() handles method resolution order (MRO) intelligently when multiple inheritance is used, ensuring that parent classes are called in the correct order.

### Example Usage:
```python 
class Parent:
    def __init__(self):
        print("Parent initialized")
    
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def __init__(self):
        # Call the Parent's __init__ method
        super().__init__()
        print("Child initialized")
    
    def greet(self):
        # Extend Parent's greet method
        super().greet()
        print("Hello from Child")

# Instantiate a Child object
child = Child()
# Output:
# Parent initialized
# Child initialized

child.greet()
# Output:
# Hello from Parent
# Hello from Child
```
### Common Use Cases:
- **Calling Parent Class __init__() Method:**
When creating a child class, you may want to initialize the parent class's attributes before adding new attributes.
- **Method Overriding:**
You can call the parent class's method to retain its behavior and extend or modify it in the child class.
- **Multiple Inheritance:**
In more complex cases where multiple inheritance is involved, super() ensures that the parent classes are called in a consistent order as determined by the MRO.

### `super()` **with No Arguments:**
```python 
class A:
    def process(self):
        print("Processing in A")

class B(A):
    def process(self):
        print("Processing in B")
        super().process()  # Call method from parent class A

class C(B):
    def process(self):
        print("Processing in C")
        super().process()  # Calls B.process(), which then calls A.process()

c = C()
c.process()
# Output:
# Processing in C
# Processing in B
# Processing in A
```
### `super(class, self)` **with Arguments:**

```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        super(A, self).greet()  # Explicitly calling A's greet() method
        print("Hello from B")

class C(B):
    def greet(self):
        super(B, self).greet()  # Calls B's greet method, which calls A's greet

c = C()
c.greet()
```
### Why Use super() with Arguments?
- **Multiple Inheritance:** When using multiple inheritance, calling super() with specific arguments ensures that the method resolution order (MRO) is followed, and the appropriate parent class method is called. Python’s super() allows cooperative inheritance, where every class in the inheritance chain is given a chance to contribute to the result.

- **Method Resolution Order (MRO):** Python uses MRO to determine the order in which classes are searched when a method is called. If super() is used with arguments, it explicitly specifies which class to start from in the MRO. This is essential in diamond inheritance (when two or more classes share a common base class).

In summary, super() is a powerful tool for class inheritance and method chaining, making code modular, maintainable, and consistent.

## __import__(name, globals=None, locals=None, fromlist=(), level=0): in python: Quick Notes
he __import__() function in Python is a built-in function used for importing a module dynamically. It is one of the lowest-level methods of importing modules and provides more flexibility than the import statement or importlib.import_module(). However, in most cases, you do not need to use __import__() directly, as the regular import statement is simpler and more readable.

### Arguments:
- `name`: This is a string representing the module name to be imported.
- `globals`: (Optional) This is the global namespace in which the __import__() function is called. Typically None, but can be set to control how the module is loaded.
- `locals`: (Optional) This is the local namespace. Like globals, it helps in module resolution in some cases.
- `fromlist`: (Optional) This is a tuple of names to be imported from the module. This is used to specify a submodule or attribute from the module. For example, you can use fromlist=['submodule'] if you want to import a specific submodule or class from the module.
- `level`: (Optional) Specifies the level of the import. The default value is 0, meaning a standard absolute import. If you use 1, it will attempt relative imports based on the current module’s position in the package hierarchy.

### Return Value:
- The function returns the imported module, or a reference to the module that was loaded.

### Combining __import__() with other import methods:
Here’s a complete example where __import__() is used alongside regular imports to show how to dynamically import a module and specific components from it.

```python
def dynamic_import_example():
    # 1. Dynamically import a module using __import__()
    math_module = __import__("math")
    print("Math module imported:", math_module)

    # 2. Dynamically import specific function (sqrt) from math using 'fromlist'
    sqrt_function = __import__("math", fromlist=["sqrt"]).sqrt
    print("Square root of 16:", sqrt_function(16))  # Using sqrt function

    # 3. Import another module dynamically (random) and use its function
    random_module = __import__("random")
    print("Random number between 1 and 10:", random_module.randint(1, 10))

    # 4. Import a module relative to the current directory (i.e., using a level 1 import)
    # In this case, we simulate the level import with a package structure
    # Assuming there is a local module called 'my_module' within a subdirectory
    my_module = __import__("my_module", fromlist=["some_function"])
    print("Imported my_module:", my_module)

    # 5. Combine dynamic import with globals and locals
    globals_dict = globals()
    locals_dict = locals()
    math_in_globals = __import__("math", globals=globals_dict, locals=locals_dict)
    print("math module imported again with globals and locals:", math_in_globals)

# Calling the method to demonstrate the dynamic imports
dynamic_import_example()

```
#### Explanation:
- Dynamic Import of a Module (math): Using __import__("math") loads the entire math module.
- Import Specific Functions (sqrt): We use the fromlist=["sqrt"] argument to directly import the sqrt function from the math module.
- Dynamic Import with Random Module: random module is imported dynamically using __import__(), and we use random.randint() to generate a random number.
- Relative Import (Level 1): This part is a hypothetical example where you have a submodule or package and want to import it with level=1. It requires an appropriate directory structure.
- Using globals and locals: __import__() allows passing globals() and locals() to control the namespaces in which the module is imported.

## compile() in python: Quick Notes
The compile() function in Python is a built-in function that compiles the source code into a code object, which can then be executed by Python’s interpreter. This allows you to dynamically compile and execute code at runtime.
#### syntax
```python
compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
```
### Parameters:
- 'source' (str, bytes, or AST object):
This is the source code to be compiled. It can either be a string or bytes representing the code to compile, or an Abstract Syntax Tree (AST) object. The code in this source is what will be compiled into a code object.
- `filename` (str):
This is the name of the file from which the code was read. This parameter is used for error messages and debugging. It is not related to actual file reading but is just a name used for traceback information. A common convention is to use "<string>" for inline source code.
- `mode` (str):
The mode specifies what kind of code to compile. It can have the following values:
    - 'exec': For a module or script that consists of a sequence of statements.
    - 'eval': For a single expression that will return a value (used in expressions like 2 + 2).
    - 'single': For a single interactive statement (for example, a single line in the Python shell).
- `flags` (optional, int):
A bitwise OR of special options (defined in the ast module), which modify how the code is compiled. Generally, this is left at the default value of 0.
- `dont_inherit` (optional, bool):
If set to True, the compiler will not inherit the syntax flags from the current interpreter’s environment. This is useful in specific situations involving the parsing of code in an isolated context.
- `optimize` (optional, int):
Specifies the optimization level of the compilation. It can take the following values:
    - -1: Use the default optimization level (based on PYTHONOPTIMIZE environment variable).
    - 0: No optimization (default when running without any optimization flag).
    - 1: Basic optimizations, removing assert statements.
    - 2: Full optimizations (removes assert statements and docstrings).
### Return Value:
The compile() function returns a code object. This code object can be passed to the exec() or eval() functions for execution, or it can be executed via the exec() function within the program.

### Example Use Cases:
1. Compiling and Executing Dynamic Code: You can use the compile() function to compile Python source code dynamically, which is useful in situations where the code to be executed is not known until runtime.

```python
code = "a = 5\nb = 10\nprint(a + b)"
compiled_code = compile(code, "<string>", "exec")
exec(compiled_code)
```

2. Compiling and Evaluating an Expression: If you have a dynamic expression and want to evaluate it, you can use the eval() function combined with compile().
```python
expr = "3 * (4 + 5)"
compiled_expr = compile(expr, "<string>", "eval")
result = eval(compiled_expr)
print(result)
```

3. Compiling Code for Debugging or Logging: Sometimes, the compile() function is useful when you need to dynamically create code for debugging or logging purposes, such as compiling a string of code entered by a user or a string stored in a configuration file.

```python
user_input = "x = 42"
compiled_user_input = compile(user_input, "<input>", "exec")
exec(compiled_user_input)
print(x)
```