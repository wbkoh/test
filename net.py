from netaddr import IPNetwork

net = IPNetwork('17.0.0.0/8')

subnets = net.subnet(24)
for subnet in subnets:
    print subnet
