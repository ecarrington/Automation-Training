### Session 2: First Playbook, Fact Gathering, and Parsing Data from IOS Devices

#### Relevant Ansible Modules
- All module documentation can be found in the ![ansible docs(https://docs.ansible.com/ansible/2.9/modules_by_category.html)
- In the docs, simply search by keyword (ios, asa, eos, etc.)
- Often, its easier to simply google for the module in question, such as 'ansible ios configuration'. This usually returns the modules you're looking for.

#### Parsing and Semi Structured Data
- Parsing returns semi-structured data from otherwise unstructred data. All this means is the data is structured, but not necessarily predictable. Data does not reside in fixed fields like that of structured data. Rather, the fields are made up as parsing executes.
- Parsing show command output will result in a JSON or YAML modeling of the information, but the parser defines the fields the data resides in (the keys and values) instead of pre-defining those fields.
- An example of structured data would be Structured Query Language. We define the database, tables, fields, and what the fields will accept before loading data into it.

##### ios_command module
- Executes arbitrary commands on IOS devices that do not require privilege escalation
- Most commonly used for 'show' commands
- documentation ![here](https://docs.ansible.com/ansible/latest/collections/cisco/ios/ios_command_module.html)
- Most simply, we pass a command to this module, and Ansible will return the raw CLI output. We'd need to debug this output or write it to a file to see what it returns
  - ```console
    - name: Execute 'show interfaces switchport' command on devices
      ios_command:
        commands: "show interfaces switchport"
      register: "cli_output"

    - name: Debug cli_output from previous command
      debug:
        msg: "{{ cli_output }}"
    ```

- While we can pull this data into a semi-structured format in some cases, most of the time it will return a blob of raw cli output, which is not fun to try and manipulate programmatically

##### ios_facts module
- Native Ansible module that gathers facts about IOS devices
- documentation ![here](https://docs.ansible.com/ansible/latest/collections/cisco/ios/ios_facts_module.html)
- Looking at the documentation, return values marked with 'always' will always be returned, along with their data types
- We don't always want all this information, and we can filter with the 'gather_subset' function, which supports pythonic logic.
  - If we wanted to gather only facts about hardware, we could specify the 'hardware'
  ```console
  - name: Gather IOS hardware facts
    ios_facts:
      gather_subset: hardware
  ```
  - If we wanted to gather facts about everything except interface parameters, we could pass the '!interfaces' argument to the function.
  ```console
  - name: Gather all IOS facts except interface-related
    ios_facts:
      gather_subset: !interfaces
  ```

##### cli_parse module
- Ansible module that allows us to integrate third-party parsers with Ansible to enhance parsing capability
- Network to Code parsers (TextFSM) and Cisco pyATS/Genie are examples of what we may integrate with Ansible via cli_parse, but there are many others. (NOTE: TextFSM and pyATS parsers require additional configuration on the Ansible control node to function properly)
- We are not limited to Cisco devices for parsing. Many third parties (including Network to Code parsers) support platforms such as ASA, Arista EOS, Palo Alto, F5, Aruba, etc.  
- It is also fairly simple to extend the functionality of these parsers if you are familiar with Python or TextFSM. If a parser you need is not available, you can always write it yourself!  
- Documentation ![here](https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/cli_parse_module.html)
- We can use a combination of show commands with the ios_command module and these parsers to create semi-structured data we can easily manipulate programmatically.
- My favorite TextFSM parsers can be found ![here](https://github.com/networktocode/ntc-templates)
- Again, all parsed output will need to be either debugged or written to a file if we need to see it.
- Sample
```console
---
- name: PLAY 1 - Gather Interface Statistics with TextFSM templates
  hosts: all
  connection: network_cli

  tasks:
    - name: Run show command
      ios_command: # runs a 'show' command
        commands: "show interfaces switchport"
      register: cli_output

    - name: Parse show command output
      set_fact:
        parsed_interfaces: "{{ cli_output.stdout[0] | parse_cli_textfsm('/home/adam/ntc-templates/templates/cisco_ios_show_interfaces_switchport.textfsm') }}"

    - name: Debug parsed show command output
      debug:
        msg: "{{ parsed_interfaces }}"
```

#### Why we care about Parsing
- Computers and APIs deal with structured data. They need some guardrails for how they are able to handle inputs, and structuring the data is typically how we accomplish that. It allows all machines to agree on how data will be exchanged between systems.
- Critical for interoperability
- Formatted data lets us interact with it programmatically.
- Rather than having to write complex regex patterns that may or may not work for different data output, we format data into some type of consistent model we can interact with.
- Example: Finding all access interfaces and returning a list. If we format the way an interface should 'look', we can reference specific key:value pairs with simple expressions and return data consistently regardless of where we pulled it from. This is also called data normalization.

#### Inventory
- Defines a list of hosts we want to target plays against
- Hierarchical, use group and host variables to keep inventory lean

#### Special Variables
- Variables well-known to Ansible. They mean something to Ansible and cannot be substituted to mean something else.
- The variables below are a type of special variable known as connection variables. These simply dictate specifics on how to execute actions on a particular target.
- Documentation can be found ![here](https://docs.ansible.com/ansible/latest/reference_aapendices/special_variables.html)

##### ansible_connection
- Connection plugin actually used to execute a task on a target host. For IOS, we commonly use 'network_cli'
- Supplies abstracted pythonic logic using different libraries such as Paramiko, so we don't have to worry about writing it ourselves
- Default connection parameter is SSH, which also tells Ansible to execute all scripts using the remote node Python interpreter, which most network devices do not have, so we override this with something that tells Ansible to send commands to the target device.
  - Other commonly used options in network automation include httpapi (REST-Based, used with Arista devices), NETCONF, RESTCONF, local
- Basically tells Ansible what channel to send commands over

##### ansible_network_os
- Supplements connection option above
- Lets Ansible konw what platform the host sits on and helps ensure the appropriate configuration syntax is applied to the device
- If the ansible_connection variable is the channel, ansible_network_os is what to send through the channel
- Common options in network automation include ios, nxos, eos, and asa.
- Modules often correlate to OS (ios_command for ios devices, nxos_command for nexus, eos_command for Arista EOS)

##### ansible_host

##### ansible_user

##### ansible_password

##### ansible_become_pass