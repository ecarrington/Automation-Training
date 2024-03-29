## Session 5: Cleansing Inputs and Validating Configuration with Ansible Assert

### Functional Testing
- Did our executed code return expected results as defined by our requirements?
- In network engineering, this boils down to two main things: Did we generate the correct configuration that the device both accepts and does not in turn break other devices on the network?

##### Unit Testing
- Most fundamental building block of functional testing
- Single unit of code is tested and validated
  - Individual tasks are tested as part of a larger playbook
    - Did the task run successfully and produce the expected results?
      - Examples: Configuration subset generation, device modification via   config modules
      - Rendering a piece of configuration from a template

##### Integration Testing
- Individual software modules have passed unit testing and are now tested together as part of a larger group
  - When we stack our configuration modules together, does it produce the intended result?
    - Examples: Configuration generation, phased configuration modification via config modules in a procedural workflow

##### Regression Testing
- Validating whether the things that used to work before the code modifications still work
  - Did the device accept the generated configuration without syntax errors or missing lines?
  - After the configuration was applied, did we break anything on the network that wasn't broken before?

### Unit Testing with Ansible Assert Module
- Documentation for this module is available [here](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/assert_module.html)
- This module accepts a list of statements that must evaluate to true, otherwise, the assertion fails.
- What we do on Assertion failure is up to us
  - Sometimes, it makes sense to stop the entire playbook when an assertion fails. This is especially true in cases of tactical playbooks where we are configuring a device without first rendering an intended configuration for review.
    - Example: If modifying VLANs with the ios_vlans module, we may want to make sure all values are populated and are the correct data types before proceeding to apply the configuration (VLAN ID is an integer, the name is not empty and is a string, etc.)
  - Other times, it makes sense to allow the playbook to run all the way through and simply list the assertion failures at the end of the job run. This is useful when generating a piece of configuration and we are attempting to ensure specific, mission-critical criteria are met.
    - Examples: Network services, such as NTP servers, DNS servers, RADIUS/TACACS, Syslog, and SNMP servers all exist and are the correct IP addresses.
    - If modifying ACLs, it may be a good idea to ensure an access control entry allowing inbound management access from desired subnets will still be present after the modification so we do not lock ourselves out of the box.

### Ansible-Assertive Callback plugin
- The default behavior of the assert plugin is to stop evaluating assertions after detecting the first failure (that is, conditions in your THAT array will only be evaluated until there is a condition that returns false). This is not very useful if we are attempting to ensure all of our conditions are satisfied before deploying a given configuration
- There are ways around this default behavior, such as creating individual tasks for each assertion or looping over the assertion task using a list of assertions as we have demonstrated
- There are also dedicated solutions for handling this limitation using callback plugins such as [ansible-assertive](https://github.com/larsks/ansible-assertive), which replaces and enhances the core library assert action plugin and adds the 'assertive' callback plugin. Callback plugins let us add new behaviors to Ansible when responding to events generated by action plugins. Action plugins are used in conjunction with modules to execute the underlying logic required to make a playbook task work. I should note the last commit on this plugin was early 2020, so if you plan to use this, know that it does not appear to be supported any longer. 
- We could also live with this default behavior and continue running/making modifications until all assertions pass. That way, we know our intended configuration has met all of our success criteria and is safe to deploy.
