## Session 4: Introduction to Jinja2 Templating, Data Modeling, and Python

### Mutability in Python
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

### Python Data Types - Primitive

Explicitly pre-defined and supported by the programming language 

#### integer
   - Whole numbers (both positive and negative)
   - Immutable
   - Read more about integers [here](https://www.w3schools.com/python/python_numbers.asp)
  
```console
>>> access_vlan = 200
```
#### boolean
   - It is, or it is not
   - Represents 'truthiness'
   - Immutable
 ```console
 >>> shutdown = true
 ```
  
#### string
   - Words 
   - Immutable
   - Surrounded by a single or double quote
   - List of bytes representing unicode characters 
   - Python does not support a 'character' type. Thus, any single characters in Python are simply strings with a length of 1
   - We can access elements in a string individually
   - Read more about strings [here](https://www.w3schools.com/python/python_strings.asp)
 ```console
 >>> a = 'hello world'
 >>> print(a[1])
 >>> e
```

#### float
   - Non-whole number (decimal)
   - Divides integer into fractional parts 
   - Read more about floats [here](https://www.w3schools.com/python/python_numbers.asp)
```console
>>> interface_bandwidth = 1000.00
```

### Python Data Types - Non-Primitive 

Data types derived from the primitive data types that offer increased functionality

#### lists (sometimes referred to as arrays)
   - Brackets ([])
   - Store multiple items in a single variable
   - Indexed. First item in an index is at index [0]
   - Ordered
      - If we add an item to a list, it will be placed at the end of the list
      - List methods are available to change ordering, but as a rule of thumb, list orders do not change by default
   - Mutable
      - We can change, add, or remove items after the list has been created
      - Thus, lists do not necessarily have a fixed length
   - Allow duplicate values
      - Because lists are indexed, lists can have items with the same value. Python only cares about the index
   - All items in a list must be the same type
      - For example, we cannot mix strings and integers in a list 
   - Read more about lists [here](https://www.w3schools.com/python/python_lists.asp)
```console
>>> vlan_ids = [100, 200, 300, 400, 500]
```
#### dictionaries
   - Curly braces ({})
   - Store multiple items in a single variable
   - key: value pairings
   - Ordered (Python 3.7 and newer, in 3.6 or older, dictionaries are unordered)
      - This means that in an ordered dictionary, we may refer to items using an index. This is not true in unordered dictionaries, and this can affect the way a particular piece of code is written. Be aware of compatibility between these versions! 
   - Mutable
      - We can change, add, or remove keys or values in the dictionary after it has been created 
   - Python does not natively support duplicate keys in dictionaries
   - JSON payloads (REST API) 
   - Python network automation makes extensive use of dictionaries
   - Read more about dictionaries [here](https://www.w3schools.com/python/python_dictionaries.asp)
```console
>>> vlan_100 = {
            "vlan_id": "100",
            "name": "default",
            "shutdown": false,
            "state": "active",
            "interfaces": [
                "GigabitEthernet0/0",
                "GigabitEthernet0/1",
                "GigabitEthernet0/2",
                "GigabitEthernet0/3",
                "GigabitEthernet1/0",
                "GigabitEthernet1/1",
                "GigabitEthernet1/2",
                "GigabitEthernet1/3",
                "GigabitEthernet2/0",
                "GigabitEthernet2/1",
                "GigabitEthernet2/2",
                "GigabitEthernet2/3",
                "GigabitEthernet3/0",
                "GigabitEthernet3/1",
                "GigabitEthernet3/2",
                "GigabitEthernet3/3"
            ],
            "type": "enet",
            "said": 100001,
            "mtu": 1500,
            "trans1": 0,
            "trans2": 0
        }
  ```
#### tuples
   - Parentheses () 
   - Used to store multiple items in a single variable
   - More performant than lists, but ensure the tuple meets your requirements before attempting to use one in place of a list
   - Ordered
      - Indexed, starting at index [0] 
   - Immutable
      - We cannot modify, add, or delete items from a tuple once it has been created 
      - Length is thus fixed, unlike lists
   - Allow duplicate values 
   - Allow multiple different data types
      - For example, we can mix strings and integers into a single tuple
   - Read more about tuples [here](https://www.w3schools.com/python/python_tuples.asp)
 ```console
 >>> interfaces = ('GigabitEthernet0/1', 'GigabitEthernet0/2', 'GigabitEthernet0/3')
 ```
 
#### sets 
   - Curly braces ({}) or defined using the set() function
   - Like tuples, sets store multiple items in a single variable 
   - Unordered
   - Unindexed
   - Immutable
   - Do not allow duplicate values
      - Very useful at de-duplicating data 
      - Also very good at performing basic math operations
   - Commonly used to make scripts declarative when declarative-nature is not natively supported
   - Read more about sets [here](https://www.w3schools.com/python/python_sets.asp)
```console
>>> intended_vlans = set([100,200,300,400,500,600])
>>> desired_vlans = set([101,201,301,401,500,600])
>>> vlans_to_add = desired_vlans - intended_vlans # want - have
>>> vlans_to_remove = intended_vlans - desired_vlans # have - want
>>> print(vlans_to_add)
>>> {201, 401, 301, 101}
>>> print(vlans_to_remove)
>>> {200, 100, 400, 300}
```

### Python Keywords 
- Reserved words that cannot be reused as variable names, function names, or any other identifier
- Commonly used in flow control 
- Read more about keywords [here](https://www.w3schools.com/python/python_ref_keywords.asp)

#### if/elif/else*
  - 'If' - Allows creation of conditional statements, executing certain blocks of code if certain conditions are satisfied
  - 'Elif' - Short for 'else if'. Executes certain blocks of code if a sequential condition is met. (If the preceding 'if' or 'elif' condition was not satisified)
  - 'Else' - Executes code if certain conditions are not satisfied. Acts as a 'catch-all'
  - It is best practice to control flow with an initial 'if' statement, followed by subsequent 'elif' and ending with an 'else' statement. This prevents the code from checking all other conditions once a certain condition has been satisfied. In short, its much more efficient. 
    - Like an ACL. If a condition is satisifed in an ACL, the device stops comparing the packet against the ACL and allows/denies it. First-match logic 

#### for
  - Used in looping (iterating through a sequence, such as a list, tuple, range, or dictionary) 
```console
>>> for interface in range(1,11):
>>>     print(f'GigabitEthernet1/0/{interface}')
GigabitEthernet1/0/1
GigabitEthernet1/0/2
GigabitEthernet1/0/3
GigabitEthernet1/0/4
GigabitEthernet1/0/5
GigabitEthernet1/0/6
GigabitEthernet1/0/7
GigabitEthernet1/0/8
GigabitEthernet1/0/9
GigabitEthernet1/0/10
```

#### or
  - Logical operator (it is used to connect two or more expressions)
  - Returns true if a single condition is satisfied
```console
>>> network_os == 'ios'
>>> if network_os == 'ios' or network_os == 'nxos':
>>>     print('I am a Cisco device.')
```

#### and
  - Logical operator
  - Returns true if all listed conditions are satisfied
```console
>>> switchport = {"operational_status": "up", "administrative_status": "up"}
>>> if switchport["operational_status"] == "up" and switchport["administrative_status"] == "up":
>>>     print("Port is good to go!")
>>> else:
>>>     if switchport["operational_status"] == "down":
>>>         print("Check administrative status and cabling.")
>>>     if switchport["administrative_status"] == "down":
>>>         print("Port needs to be administratively enabled.")
>>> ...
>>> Port is good to go!
```

#### not 
  - Logical operator
  - Returns true if the statement is not True

```console
>>> interfaces = ['GigabitEthernet0/1', 'GigabitEthernet0/2', 'GigabitEthernet0/3', 'GigabitEthernet0/4', 'GigabitEthernet0/5']
>>> trunk_ports = ['GigabitEthernet0/1', 'GigabitEthernet0/2']
>>> for interface in interfaces:
>>>     if interface not in trunk_ports:
>>>         print(f'{interface} is an access port.')
>>>     else:
>>>         print('f{interface} is a trunk port.')
>>> ...
>>> GigabitEthernet0/1 is a trunk port.
>>> GigabitEthernet0/2 is a trunk port.
>>> GigabitEthernet0/3 is an access port.        
>>> GigabitEthernet0/4 is an access port.
>>> GigabitEthernet0/5 is an access port.
```

#### None
  - Defines a null value, or no value at all
  - This is not the same as 0, False, or an empty string
  - Sometimes, we run into values that are not defined or have no value. Using the None type helps handle those cases 
  - This is especially true in templating

### Why do we care? 
- [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) is a templating language that leverages Python under the hood. 
- Along with data models, this is what we use to generate configuration with Ansible
- Recall that Ansible loads variables into memory at playbook runtime and will reference the variables it needs when it needs them
- If we call for variables in a template, Ansible is going to try to 'fill in the blanks' with the information it knows while rendering the templates
- Being Pythonic in nature, we can incorporate its logic into templates to keep configuration files lean and relevant to the device variables we are attempting to use. Variables in data models help keep configuration unique to a device, and templates enforce uniformity across the environment
- Device configuration varies very little between devices in the enterprise, so we target uniqueness in each device, model what could change, and let Ansible consume those models with a generic template repository to quickly render device configuration in meaningful ways. 
- Using Pythonic logic in templates lets us account for subtle differences in syntax or configuration parameters based on device vendor or role in the network

### Ansible template module
- Processes templates using the Jinja2 templating engine and renders output to a target destination 
- Documentation [here](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/template_module.html)
