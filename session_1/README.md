### Session 1: Environment Overview, Ansible Setup/Operation, and Inventory

#### What is Ansible?
- Infrastructure automation framework used for configuration management and orchestration
- Leverages python under the hood
- Easy to use, reliable
- A means to an end. Not the full picture of infrastructure automation
- A single tool in a chain of many that comprise holistic enterprise infrastructure automation
- Easy to integrate with other automation tools through APIs or Software Development Toolkits (SDKs)
- Large community support
- Open-source


#### What Ansible is Not
- Not specifically a network automation tool
- Not fast, but that is not necessarily important

#### How Ansible Works
- Ansible is agentless, meaning we do not have to install or maintain anything on the remote targets we execute the automation task against (unlike Chef, Puppet, or Salt), making it vendor-agnostic and thus highly scalable and relatively simple to integrate with existing platforms
- Ansible works by connecting to targeted nodes and pushing small 'programs' called 'modules' to them. These serve as the resource models that represent the **desired** state of the system. Ansible executes these programs over a selected transport protocol (SSH, REST, NETCONF, GPC, etc) and removes the programs when finished.
- Ansible is **stateless**, meaning it does not pay attention to the state of the entire device it is connecting to, and is thus unaware of any existing state at playbook runtime. It needs to determine the current state of the device configuration, so that it may execute the appropriate sequence of commands to bring the current state to the desired state defined in the module.
- State is not saved for a subsequent playbook or task, so state is always determined at the module level for each playbook run. There are some exceptions to this, and we can store state in variables and pass them between pieces of the playbook.
- Ansible is **idempotent**, meaning it only attempts to transform a device to a defined desired state if necessary, and uses the minimum amount of configuration to get there. Because Ansible collects the configuration state relevant to the module it is pushing out before making any changes, it determines whether or not it will execute any commands on the target system for the particular configuration resource it is targeting. If Ansible finds a mismatch in desired vs running state, Ansible will apply the necessary commands to make the states equal. If no differences are detected, Ansible will not attempt to execute any configuration changes on the device.
- Ansible is **not fully declarative** on its own, but modules can be manipulated to make it so. Declarative programming in this context refers to a paradigm by which a program attempts to conform to a supplied model (desired state) by performing both additive (adding configuration) or destructive changes (remove configuration), and knows exactly how to get there.
- Ansible is **procedural**, meaning it is capable of performing ad-hoc commands in a particular sequence within a defined environment, and does so very well, because we must define the procedure and environment precisely.

#### Playbooks
- The blueprint of an automation task. AKA 'The Script'
- Playbooks are comprised of plays. We break playbooks into plays to target specific devices or groups as needed.
- Plays are comprised of tasks, which are the procedural steps we must define to arrive from one configuration state to another.
- Tasks are comprised of modules, which are the modular code blocks designed to perform a specific range of functions and may accept different arguments.
- We pass templates and variables to modules as required to make a module function.
  - Variables provide a level of abstraction and help identify differences between target devices. We variablize differences to make templates and playbooks reusable. (DRY-Don't Repeat Yourself)

- We can find module documentation [here](https://docs.ansible.com/ansible/2.9/modules/modules_by_category.html)


```cli
---


- name: Name of Play
  hosts: targeted hosts from inventory
  connection: how ansible will connect and push modules to target hosts

  tasks:
    - name: Name of first task
      module:
        arguments:

    - name: Name of second task
      module:
        arguments:

...
```

#### YAML (Yaml Ain't Markup Language
- Human-readable data **serialization** (aka not used for markup) language commonly used for configuration files or applications where data is stored or transmitted.
- Domain-Specific Language of Ansible (DSL). Used to abstract pythonic complexity away from the underlying framework to solve a certain class of problems.
- In Ansible, nearly all YAML files start with a list, and each item in the list is another list of key/value pairs referred to as a dictionary or hash
- See examples [here](./yaml_examples/)
- Ansible YAML syntax documentation can be found [here](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html)

#### Inventory
- Ansible works against multiple managed nodes or hosts at the same time using a list or group called an 'inventory'
- Once this file is defined, we can use patterns to select hosts or groups we want to run playbooks against
- Default location for inventory is  /etc/ansible/hosts/ but we can override this in ansible.cfg or via the command line with the '-i' flag
- We can also pull inventory from different sources and in different formats using 'dynamic inventory'
- Common formats for inventory files are '.ini' and '.yml'. YAML files allow for more granular control over encryption and variable assignments, and it is recommended to use this format
- Two default groups: all (all hosts), and ungrouped (hosts that do not have a specific group). Each host will belong to two groups minimum, either all and some other group, or ungrouped and some other group
- At runtime, ansible will look for variables in the host_vars and group_vars folders and load them into memory for use as needed into the playbook. Precedence: host_vars > group_vars by group > all group_vars
- Inventory information can be found [here](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html)
