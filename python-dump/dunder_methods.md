List of Common Dunder Methods and Their Purposes:
Object Initialization and Representation

    __init__(self, ...): Initializes an object when it is created (like a constructor).

class MyClass:
    def __init__(self, value):
        self.value = value

__new__(cls, ...): Creates and returns a new instance of a class; used for object creation.
__del__(self): Defines behavior for when an object is destroyed (destructor).
__repr__(self): Provides an official string representation of an object, useful for debugging.

    def __repr__(self):
        return f"MyClass({self.value})"

    __str__(self): Defines a user-friendly string representation of an object (used by print()).
    __bytes__(self): Returns the byte representation of an object.
    __format__(self, format_spec): Defines behavior for string formatting (e.g., format(obj, 'spec')).

Conversion Dunder Methods

    __int__(self): Converts an object to an integer using int(obj).
    __float__(self): Converts an object to a float using float(obj).
    __complex__(self): Converts an object to a complex number using complex(obj).
    __bool__(self): Converts an object to a boolean using bool(obj).
    __str__(self): Converts an object to a string using str(obj).
    __bytes__(self): Converts an object to bytes using bytes(obj).
    __index__(self): Returns an integer representation for an object, used for slicing and indexing.

Mathematical Operations

    __add__(self, other): Implements addition (+).
    __sub__(self, other): Implements subtraction (-).
    __mul__(self, other): Implements multiplication (*).
    __truediv__(self, other): Implements division (/).
    __floordiv__(self, other): Implements floor division (//).
    __mod__(self, other): Implements modulus (%).
    __pow__(self, other[, modulo]): Implements exponentiation (**).
    __radd__(self, other), __rsub__(self, other), etc.: Implements reverse arithmetic operations (when the left operand does not support the operation).
    __iadd__(self, other), __isub__(self, other), etc.: Implements in-place arithmetic operations (+=, -=, etc.).

Comparison Operations

    __lt__(self, other): Less than (<).
    __le__(self, other): Less than or equal (<=).
    __eq__(self, other): Equal (==).
    __ne__(self, other): Not equal (!=).
    __gt__(self, other): Greater than (>).
    __ge__(self, other): Greater than or equal (>=).

Attribute Access and Management

    __getattr__(self, name): Called when an attribute is accessed that doesn't exist.
    __getattribute__(self, name): Called for every attribute access.
    __setattr__(self, name, value): Called when an attribute is set.
    __delattr__(self, name): Called when an attribute is deleted.
    __dir__(self): Called by dir() to list attributes of the object.

Container and Sequence Operations

    __len__(self): Returns the length using len().
    __getitem__(self, key): Defines behavior for indexing (e.g., obj[key]).
    __setitem__(self, key, value): Defines behavior for assigning to an index (e.g., obj[key] = value).
    __delitem__(self, key): Defines behavior for deleting an index (e.g., del obj[key]).
    __iter__(self): Returns an iterator for the object.
    __next__(self): Returns the next item from an iterator.
    __contains__(self, item): Implements membership test using in.

Callable Objects

    __call__(self, ...): Makes an instance callable like a function.

Context Managers

    __enter__(self): Called when entering a context (with statement).
    __exit__(self, exc_type, exc_value, traceback): Called when exiting a context.

Miscellaneous

    __hash__(self): Returns an integer hash value, used by hash().
    __eq__(self, other): Needed for an object to be hashable (in conjunction with __hash__).
    __copy__(self), __deepcopy__(self, memo): Defines behavior for the copy and deepcopy operations.
    __sizeof__(self): Returns the size of the object in memory.
    __repr__() and __str__(): For object representation.