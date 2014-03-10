import inventory as mysets
class network_subnet(object):
    def __init__(self,quantum):
            self.i=self.j=0;
            self.quantum=quantum
    #creation of pools and pool members
    def Create_network(self):
        mysets.network_id=self.quantum.create_network(mysets.network_json)['network']['id']
        mysets.private_network_id=self.quantum.create_network(mysets.network_json_private)['network']['id']
    def Create_subnet(self):
        for subnets in mysets.subnet_json['subnets']:
            subnets['network_id']=mysets.private_network_id
        subnet_list=self.quantum.create_subnet(mysets.subnet_json)['subnets']
        for ind_subnets in subnet_list:
            mysets.subnet_mapping[ind_subnets['name']]=ind_subnets['id']