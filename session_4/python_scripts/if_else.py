#!/usr/bin/python3

interfaces = [
              {"interface": "GigabitEthernet1/0/1", "type": "access"},
              {"interface": "GigabitEthernet1/0/2", "type": "access"},
              {"interface": "GigabitEthernet1/0/3", "type": "access"},
              {"interface": "GigabitEthernet1/0/4", "type": "access"},
              {"interface": "GigabitEthernet1/0/5", "type": "access"},
              {"interface": "GigabitEthernet1/0/6", "type": "unused"},
              {"interface": "GigabitEthernet1/0/23", "type": "trunk"},
              {"interface": "GigabitEthernet1/0/23", "type": "trunk", "allowed-vlans": "100,200,300,400,500"},
              {"interface": "GigabitEthernet1/0/24", "type": "trunk", "allowed-vlans": "100,200,300,400,500"}
              ]


for interface in interfaces:
    print(f'interface {interface["interface"]}')
    if interface['type'] == "access":
        print (' description ACCESS PORT')
        print(' switchport mode access')
    elif interface['type'] == "trunk":
        print(' description TRUNK PORT')
        print(' switchport mode trunk')
        if 'allowed-vlans' in interface:
            print(f' switchport trunk allowed vlan {interface["allowed-vlans"]}')
        else:
            print(' switchport trunk allowed vlan none')
    elif interface['type'] == "unused":
        print(' switchport mode access')
        print(' switchport access vlan 999')
        print(' no cdp run')
        print(' shutdown')
