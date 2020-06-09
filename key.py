

from netmiko import ConnectHandler

cisco_8 = {
    'device_type': 'cisco_ios_telnet',
    'host':   '10.16.96.234',
    'username': 'test',
    'password': 'cisco',
    'port' : 5007,          # optional, defaults to 22
    'secret': 'cisco',     # optional, defaults to ''
}
commands=["ip route 192.168.1.2 255.255.255.0 "
]

net_connect = ConnectHandler(**cisco_8)
#print(net_connect.find_prompt())

output = net_connect.send_command('show ip int brief')

print(output)
output1 = net_connect.send_config_set(commands)
output2 = net_connect.send_command('show ip int brief')
print(output2)


