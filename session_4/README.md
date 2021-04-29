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

- **Primitive: Explicitly pre-defined and supported by the programming language** 
  - integer
  - boolean
  - string
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

- **Non-Primitive: Data types derived from the primitive data types that offer increased functionality
  - lists (sometimes referred to as arrays)
  - dictionaries
  - tuples
  - sets 

 
