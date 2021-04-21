### Session 3: Configuring IOS Devices with Ansible ios_config module

#### ios_config module
- if using ansible 3.x and up, install this module with ansible-galaxy (part of cisco.ios collection)
```console
ansible-galaxy collection install cisco.ios
```
- Primary module for sending configuration commands to an IOS device.
- Idempotent, but you must use configuration syntax as it appears in the running configuration of the device (no abbreviations)
  - this is especially important when using the diff capabilities of Ansible
- Module documentation can be found [here](https://docs.ansible.com/ansible/latest/collections/cisco/ios/ios_config_module.html)
- Can also be used to save configuration locally to device, or to back up the configuration to a remote device prior to performing any configuration modification 
