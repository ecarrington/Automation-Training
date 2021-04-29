### Session 3: Introduction to Jinja2 Templating, Data Modeling, and Python

#### Mutability in Python
- Programs store data in variables that represent storage locations in a computer's memory
- The contents of the memory locations at any given point in a program's execution is called **state**
- Python works a bit differently than C-based languages. Rather than variables, Python uses names. When we assign a value to a name (variable), the name references the object (value) location in memory
- Moreover, unlike C-based languages, the data type is set when we assign a value to the name (variable), making python a strongly typed, dynamic language
  - **Strongly Typed: The type of the value does not change without specific conversion. We have to tell the value to change**
  - **Dynamic: Runtime objects (values in memory) themselves have a type, which we define at the time they are created**
    - C-based languages are typically statically typed, where variables themselves have a type that is declared at the time they are initialized, before values are assigned to it
 
 *Declaring an integer in Java. Notice the type is defined before a value is assigned to it*
 ```console
 int vlan;
 vlan = 100;
 ```
 
 *Declaring an integer in Python. Notice we do not need to define a type before assigning a value to this name (variable)*
 ```console
 vlan = 100
 ```
  - Location of the contents in memory does not change, but the contents in that location may depending on program design and need, and for this reason it is important we know what we can and cannot change
    - **Mutable: Changeable. State can be altered or modified after the object or variable is created**
    - **Immutable: Not changeable. State cannot be altered or modified after the object or variable is created**

#### Python Data Types 

This is not an exhaustive list, but these are the data types we will most commonly work with on our automation journey. 

- **Primitive: Explicitly pre-defined and supported by the programming language** 
  - integer
    - Whole numbers (both positive and negative)
    - Immutable
```console
>>> access_vlan = 200
```
  - boolean
    - It is, or it is not
    - Represents 'truthiness'
    - Immutable
 ```console
 >>> shutdown = true
 ```
  - string
    - Words 
    - Immutable
    - Surrounded by a single or double quote
    - List of bytes representing unicode characters 
    - Python does not support a 'character' type. Thus, any single characters in Python are simply strings with a length of 1
    - We can access elements in a string individually
 ```console
 >>> a = 'hello world'
 >>> print(a[1])
 >>> e
```
- float
  - Non-whole number (decimal)
  - Divides integer into fractional parts 
```console
>>> interface_bandwidth = 1000.00
```

- **Non-Primitive: Data types derived from the primitive data types that offer increased functionality**
  - lists (sometimes referred to as arrays)
    - Brackets
    - Indexed. First item in an index is at index [0]
    - Ordered
      - If we add an item to a list, it will be placed at the end of the list
      - List methods are available to change ordering, but as a rule of thumb, list orders do not change by default
    - Mutable
      - We can change, add, or remove items after the list has been created
    - Allow duplicate values
      - Because lists are indexed, lists can have items with the same value. Python only cares about the index
  - dictionaries
    - Curly braces 
    - key: value pairings
    - JSON payloads (REST API) 
    - Python network automation makes extensive use of dictionaries
  - tuples
  - sets 

 
