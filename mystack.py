import argparse
from neutronclient.v2_0 import client
import novaclient.v1_1.client as nvclient
from credentials import get_nova_creds

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--tenant", required=True)
    parser.add_argument("--url", required=True)
    args = parser.parse_args()

    quantum = client.Client(username=args.username,
                            password=args.password,
                            tenant_name=args.tenant,
                            auth_url=args.url)

    security_groups = quantum.list_security_groups()['security_groups']
    '''
    security_groups_json={'security_group':[
                                 {"name":"web","description":"security group for webservers"},
                                 {"name":"ssh","description":"security group for ssh"},
                                 {"name":"database","description":"security group for database"}]}
    
    quantum.create_security_group(security_groups_json);
    for security_group in security_groups:
            print ("Creating rules for tenant:  %s group: %s" %
                    (security_group['tenant_id'], security_group['name']))
            # The security group doesn't have any egress rules so we
            # need to add them. Bulk add
            if security_group['name'] == 'web':
                body = {'security_group_rules': [
                        {'direction': 'ingress','port-range-min': 80, 'port-range-max': 80,'protocol': 'TCP',
                         'tenant_id': security_group['tenant_id'],
                         'security_group_id': security_group['id']},
                        {'direction': 'ingress','port-range-min': 22, 'port-range-max': 22,'protocol': 'TCP',
                         'tenant_id': security_group['tenant_id'],
                         'remote-group-id': 'web',
                         'security_group_id': security_group['id']}]}
                web_sec_id=quantum.create_security_group_rule(body)['security_group']['id']
            if security_group['name'] == 'ssh':
                body = {'security_group_rules': 
                        {'direction': 'ingress','port-range-min': 22, 'port-range-max': 22,'protocol': 'TCP',
                         'tenant_id': security_group['tenant_id'],
                         'security_group_id': security_group['id']}}
                quantum.create_security_group_rule(body)
            if security_group['name'] == 'database':
                body = {'security_group_rules': [
                        {'direction': 'ingress','port-range-min': 3306, 'port-range-max': 3306,'protocol': 'TCP',
                         'remote-group-id': 'web',
                         'tenant_id': security_group['tenant_id'],
                         'security_group_id': security_group['id']},
                        {'direction': 'ingress','port-range-min': 22, 'port-range-max': 22,'protocol': 'TCP',
                         'remote-group-id': 'ssh',
                         'tenant_id': security_group['tenant_id'],
                         'security_group_id': security_group['id']}]}
                quantum.create_security_group_rule(body)
    creds = get_nova_creds()
    nova = nvclient.Client(**creds)
    if not nova.keypairs.findall(name="mykey1"):
        with open(os.path.expanduser('~/.ssh/id_rsa.pub')) as fpubkey:
            nova.keypairs.create(name="mykey1", public_key=fpubkey.read())
    if not nova.keypairs.findall(name="mykey2"):
        with open(os.path.expanduser('~/.ssh/id_rsa.pub')) as fpubkey:
            nova.keypairs.create(name="mykey2", public_key=fpubkey.read())
    if not nova.keypairs.findall(name="mykey3"):
        with open(os.path.expanduser('~/.ssh/id_rsa.pub')) as fpubkey:
            nova.keypairs.create(name="mykey3", public_key=fpubkey.read())
    if not nova.keypairs.findall(name="mykey4"):
        with open(os.path.expanduser('~/.ssh/id_rsa.pub')) as fpubkey:
            nova.keypairs.create(name="mykey4", public_key=fpubkey.read())
    if not nova.keypairs.findall(name="mykey4"):
        with open(os.path.expanduser('~/.ssh/id_rsa.pub')) as fpubkey:
            nova.keypairs.create(name="mykey4", public_key=fpubkey.read())
    instance=nova.servers.create(name="web-server1", image="cirros-0.3.1-x86_64-uec", flavor=1, key_name="mykey1",security_groups="web")
    status = instance.status
    while status == 'BUILD':
        time.sleep(5)
        # Retrieve the instance again so the status field updates
        instance = nova.servers.get(instance.id)
        status = instance.status
    instance=nova.servers.create(name="web-server2", image="cirros-0.3.1-x86_64-uec", flavor=1, key_name="mykey2",security_groups="web")
    status = instance.status
    while status == 'BUILD':
        time.sleep(5)
        # Retrieve the instance again so the status field updates
        instance = nova.servers.get(instance.id)
        status = instance.status
    instance=nova.servers.create(name="database_server", image="cirros-0.3.1-x86_64-uec", flavor=1, key_name="mykey3",security_groups="database")
    status = instance.status
    while status == 'BUILD':
        time.sleep(5)
        # Retrieve the instance again so the status field updates
        instance = nova.servers.get(instance.id)
        status = instance.status
    instance=nova.servers.create(name="jumpbox", image="cirros-0.3.1-x86_64-uec", flavor=1, key_name="mykey4",security_groups="ssh")
    status = instance.status
    while status == 'BUILD':
        time.sleep(5)
        # Retrieve the instance again so the status field updates
        instance = nova.servers.get(instance.id)
        status = instance.status
    instance=nova.servers.create(name="client", image="cirros-0.3.1-x86_64-uec", flavor=1, key_name="mykey5")
    status = instance.status
    while status == 'BUILD':
        time.sleep(5)
        # Retrieve the instance again so the status field updates
        instance = nova.servers.get(instance.id)
        status = instance.status
    floating_ip = nova.floating_ips.create()
    instance=nova.servers.find(name= 'jumpbox')
    instance.add_floating_ip(floating_ip)
    instance=nova.servers.find(name= 'web-server1')
    web1 = instance.interface_list()['interfaceAttachments']
    web1=web1[0]['fixed_ips']
    web1=web1[0]['ip_address']
    subnet_id=quantum.list_subnets()['subnets'];
    subnet_id=subnet_id[0];
    body = {
        "pool": {
            "subnet_id": subnet_id['id'],
            "lb_method": "ROUND_ROBIN",
            "protocol": "HTTP",
            "name": "NewPool"
            }
                }
    poolid=quantum.create_pool(body)['pool']['id']
    body= {
        "member": {
            "protocol_port": "80",
            "address": web1,
            "pool_id": poolid
        }
           }
    quantum.create_member(body)
    instance=nova.servers.find(name= 'web-server2')
    web2 = instance.interface_list()['interfaceAttachments']
    web2=web2[0]['fixed_ips']
    web2=web2[0]['ip_address']
    body= {
        "member": {
            "protocol_port": "80",
            "address": web2,
            "pool_id": poolid
        }
           }
    quantum.create_member(body)
    body={
        "health_monitor": {
            "delay": "3",
            "max_retries": "3",
            "type": "HTTP",
            "timeout": "3"
            }
          }
    health_monitor_id=quantum.create_health_monitor(body)['health_monitor']['id']
    body={
        "health_monitor": {
            "id": health_monitor_id
            }
          }
    quantum.associate_health_monitor(poolid,body)
    body={
        "vip": {
            "protocol": "HTTP",
            "name": "NewVip",
            "subnet_id": subnet_id['id'],
            "pool_id": poolid,
            "protocol_port": "80"
            }
          }
    vip_portid=quantum.create_vip(body)['vip']['port_id']
    network_id=quantum.list_networks()['networks'][0]['id']
    body = {
        "floatingip":
        {
            "floating_network_id": network_id,
            "port_id": vip_portid
         }
            }
    body={
           "port":{
              "security_groups":[
                 "85cc3048-abc3-43cc-89b3-377341426ac5"
              ],
                "device_id": vip_portid   
           }
        }
    quantum.create_floatingip(body)
    quantum.update_port(vip_portid,body);
    '''
if __name__ == "__main__":
    main()