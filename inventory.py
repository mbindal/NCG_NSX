'''
Created on Mar 7, 2014

@author: mbindal
'''
network_json_private={
   "networks":[
      {
         "name":"sample_network_1"
      },
      {
         "name":"sample_network_2"
      }
   ]
}
router_id='1111111'
subnet_json={
   "subnets":[
      {"name":"web",
         "cidr":"192.168.199.0/24",
         "ip_version":4,
         "network_id":"e6031bc2-901a-4c66-82da-f4c32ed89406"
      },
      {"name":"ssh",
         "cidr":"10.56.4.0/22",
         "ip_version":4,
         "network_id":"64239a54-dcc4-4b39-920b-b37c2144effa"
      }
   ]
}
subnet_mapping={'web':'0000','ssh':'123'}
network_id='66666'
private_network_id='222222'
sec_id={'web':'3333','ssh':'6666'}
pool={"bulk_pool":[{
        "pool": {
            "subnet_id": "web",
            "lb_method": "ROUND_ROBIN",
            "protocol": "HTTP",
            "name": "webpool"
            }}]
                }
pool_member= {"web":[{
        "member": {
            "protocol_port": "80",
            "address": 'web1',
            "pool_id": '0000'
        }}],
              "ssh":[{
        "member": {
            "protocol_port": "80",
            "address": 'ssh1',
            "pool_id": '0000'
        }}]
           }
           
ip_mapping={web1:0.0.0.0, web2:0.0.0.0}

health_monitors={
                 "monitors":[{
        "health_monitor": {
            "delay": "3",
            "max_retries": "3",
            "type": "HTTP",
            "timeout": "3"
            }}]
          }
monitor_pool_assoc={"associations":[{
        "health_monitor": {
            "id": "000"
            }}]
          }
vip={"vip_list":[{
        "vip": {
            "protocol": "HTTP",
            "name": "NewVip",
            "subnet_id": "12345",
            "pool_id": "00000",
            "protocol_port": "80"
            }}]
          }
floating_ip = {
        "floatingip":
        {
            "floating_network_id": "12345",
            "port_id": "12344"
         }
            }
update_sec_port={"security_groupl":[{
           "port":{
              "security_groups":[
                 "web"
              ]   
           }}]
        }
security_groups_json={'security_group':[
                                 {"name":"web","description":"security group for webservers"},
                                 {"name":"ssh","description":"security group for ssh"},
                                 {"name":"database","description":"security group for database"}]}
sec_group_rules={'ssh':{'security_group_rules': [
                         {'direction': 'ingress','port-range-min': 22, 'port-range-max': 22,'protocol': 'TCP',
                         'tenant_id': '111111',
                         'security_group_id': '11111'}]
                        }
                        
                 'web':{'security_group_rules': [
                         {'direction': 'ingress','port-range-min': 80, 'port-range-max': 80,'protocol': 'TCP',
                         'tenant_id': '1222',
                         'security_group_id': '111111'},
                         {'direction': 'ingress','port-range-min': 22, 'port-range-max': 22,'protocol': 'TCP',
                         'tenant_id': '1222',
                         'remote-group-id': 'ssh',
                         'security_group_id': '111111'}]
                        }
                         
                 'database':{'security_group_rules': [
                         {'direction': 'ingress','port-range-min': 3306, 'port-range-max': 3306,'protocol': 'TCP',
                         'tenant_id': '1222',
                         'remote-group-id': 'web',
                         'security_group_id': '111111'},
                         {'direction': 'ingress','port-range-min': 22, 'port-range-max': 22,'protocol': 'TCP',
                         'tenant_id': '1222',
                         'remote-group-id': 'ssh',
                         'security_group_id': '111111'}]
                        }
                 }
