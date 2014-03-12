import inventory as mysets
class network_subnet(object):
    def __init__(self,quantum):
            self.i=self.j=0;
            self.quantum=quantum
    #creation of pools and pool members
    def Create_network(self):
        mysets.network_id=self.quantum.list_networks()['networks'][0]['id']
        mysets.private_network_id=self.quantum.create_network(mysets.network_json_private)['networks']
        mysets.router_id=self.quantum.list_routers()['routers'][0]['id']
    def Create_subnet(self):
        i=0;
        for subnets in mysets.subnet_json['subnets']:
            subnets['network_id']=mysets.private_network_id[i]['id']
            i=i + 1
        subnet_list=self.quantum.create_subnet(mysets.subnet_json)['subnets']
        for ind_subnets in subnet_list:
            mysets.subnet_mapping[ind_subnets['name']]=ind_subnets['id']
            body={'subnet_id': ind_subnets['id']}
            self.quantum.add_interface_router(mysets.router_id,body)
