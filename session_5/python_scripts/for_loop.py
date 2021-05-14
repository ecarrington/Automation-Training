
#!/usr/bin/python3
for interface in range (1,25):
    print(f'interface g1/0/{interface}')
    print(' description ACCESS PORT')
    print(' switchport mode access')
    print(' switchport access vlan 200')
