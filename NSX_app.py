import inventory as mysets
from neutronclient.v2_0 import client
import novaclient.v1_1.client as nvclient
from credentials import get_keystone_creds,get_nova_creds
from security_groups import security_groups
from network_subnet import network_subnet
from Load_Balancer_floating_ip import  Load_Balancer_floating_ip

def create_topology():
    quantum_creds= get_keystone_creds()
    quantum = client.Client(**quantum_creds)
    nova_creds = get_nova_creds()
    nova = nvclient.Client(**nova_creds)
    network_object=network_subnet(quantum)
    network_object.Create_network()
    network_object.Create_subnet()
    #enter the nova code to boot instances
    security_grp_object=security_groups(quantum)
    security_grp_object.create_security_groups()
    security_grp_object.create_security_group_rules()
    load_balancer=Load_Balancer_floating_ip(mysets.network_id,mysets.subnet_mapping, mysets.ip_mapping, mysets.sec_id,quantum);
    load_balancer.Create_Loadbalancers()
    
    
    
if __name__ == "__main__":
    create_topology()
