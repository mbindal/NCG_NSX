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
subnet_mapping={'web':'0000','ssh':'123','database':'234'}
network_id='66666'
private_network_id='222222'
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
            "pool_id": '0000'},
          {
            "protocol_port": "80",
            "address": 'web2',
            "pool_id": '0000'},
          {
            "protocol_port": "80",
            "address": 'web3',
            "pool_id": '0000'}
        }]
           }
           
ip_mapping={web1:0.0.0.0, web2:0.0.0.0, web3:0.0.0.0, jumpbox:0.0.0.0, db1:0.0.0.0}

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

servers = [{'name' : 'Web1',
            'image' : 'cirros-0.3.1-x86_64-uec',
            'flavor' : 'm1.tiny'
           },
           {'name' : 'Web2',
            'image' : 'cirros-0.3.1-x86_64-uec',
            'flavor' : 'm1.tiny'
           },
           {'name' : 'Web3',
            'image' : 'cirros-0.3.1-x86_64-uec',
            'flavor' : 'm1.tiny'
           },
           {'name' : 'JumpBox',
            'image' : 'cirros-0.3.1-x86_64-uec',
            'flavor' : 'm1.tiny'
           },
           {'name' : 'DB1',
            'image' : 'cirros-0.3.1-x86_64-uec',
            'flavor' : 'm1.tiny'
           }]

security_groups={
   'security_groups':
   [
      {'security_group':{"name":"web", "description":"security group for webservers"}},
      {'security_group':{"name":"ssh", "description":"security group for ssh"}},
      {'security_group':{"name":"db", "description":"security group for database"}}            
   ]
}

security_group_ids={'web':'','ssh':'','db':''}

security_group_rules={  
   'ssh':
   [
      {
         'security_group_rule':
         {
            'direction': 'ingress', 
            'port_range_min': 22, 
            'port_range_max': 22, 
            'ethertype':'IPv4', 
            'protocol': 'TCP',
            'security_group_id': 'ssh'
         }
      }
   ],
   'web':
   [
      {
         'security_group_rule':
         {
            'direction': 'ingress', 
            'port_range_min': 80, 
            'port_range_max': 80,
            'ethertype':'IPv4', 
            'protocol': 'TCP',
            'security_group_id': 'web'
         }
      },
      {
         'security_group_rule':
         {
            'direction': 'ingress',
            'port_range_min': 22, 
            'port_range_max': 22,
            'ethertype':'IPv4', 
            'protocol': 'TCP',
            'remote_group_id': 'ssh', 
            'security_group_id': 'web'
         },
      }
   ],
   'db':
   [
      {
         'security_group_rule':
         {
            'direction': 'ingress',
            'port_range_min': 3306, 
            'port_range_max': 3306,
            'ethertype':'IPv4', 
            'protocol': 'TCP',
            'remote_group_id': 'web', 
            'security_group_id': 'db'
         }
      },
      {
         'security_group_rule':
         {
            'direction': 'ingress',
            'port_range_min': 22, 
            'port_range_max': 22,
            'ethertype':'IPv4', 
            'protocol': 'TCP',
            'remote_group_id': 'ssh', 
            'security_group_id': 'db'
         }
      }
   ]
}
