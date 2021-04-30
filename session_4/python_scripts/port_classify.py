#!/usr/bin/python3

interfaces = ['GigabitEthernet0/1', 'GigabitEthernet0/2', 'GigabitEthernet0/3', 'GigabitEthernet0/4', 'GigabitEthernet0/5' ]
trunk_ports = ['GigabitEthernet0/1', 'GigabitEthernet0/2']

for interface in interfaces:
    if interface not in trunk_ports:
        print(f'{interface} is an access port.')
    else:
        print(f'{interface} is a trunk port.')