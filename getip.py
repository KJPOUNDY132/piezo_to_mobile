import commands

ip_addr = commands.getoutput('hostname -I')
print(ip_addr)
print(type(ip_addr))
