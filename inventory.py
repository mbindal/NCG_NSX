
subnet_mapping={'web':'0000','ssh':'123'}
network_id='66666'
sec_id={'web':'3333','ssh':'6666'}
pool={"bulk_pool":[{
        "pool": {
            "subnet_id": "web",
            "lb_method": "ROUND_ROBIN",
            "protocol": "HTTP",
            "name": "webpool"
            }}]
                }
pool_member= {"webpool":[{
        "member": {
            "protocol_port": "80",
            "address": '0.0.0.0',
            "pool_id": '0000'
        }}],
              "ssh":[{
        "member": {
            "protocol_port": "80",
            "address": '0.0.0.0',
            "pool_id": '0000'
        }}]
           }
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
