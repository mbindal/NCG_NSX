'''
Created on Mar 7, 2014

@author: mbindal

'''
import inventory as mysets
class Load_Balancer_floating_ip(object):
    def __init__(self, network_id, subnet_mapping, ip_mapping, sec_id, quantum):
            self.i=self.j=0;
            self.network_id=network_id
            self.subnet_mapping=subnet_mapping
            self.ip_mapping=ip_mapping
            self.sec_id=sec_id
            self.quantum=quantum
    #creation of pools and pool members
    def Create_Loadbalancers(self):
        for individual_pools in mysets.pool['bulk_pool']:
            subnet_id=mysets.subnet_mapping[individual_pools['pool']['subnet_id']]
            individual_pools['pool']['subnet_id']=subnet_id
            pool=self.quantum.create_pool(individual_pools)['pool']
            for pools in self.pool_member[pool['name']]:
                pools['member']['pool_id']=pool['id']
                pools['member']['address']=self.ip_mapping[pools['member']['address']]
                self.quantum.create_member(pools)
            #creating health monitor and associating with pools
            monitor_id=self.quantum.create_health_monitor(mysets.health_monitors['monitors'][self.i])['health_monitor']['id']
            mysets.monitor_pool_assoc['associations'][self.i]['health_monitor']['id']=monitor_id
            self.quantum.associate_health_monitor(pool['id'],mysets.monitor_pool_assoc['associations'][self.i])
            mysets.vip['vip_list'][self.i]['vip']['pool_id']=pool['id']
            mysets.vip['vip_list'][self.i]['vip']['subnet_id']=subnet_id
            vip_portid=self.quantum.create_vip(mysets.vip['vip_list'][self.i])['vip']['port_id']
            mysets.floating_ip['floating_ip']['port_id']=vip_portid
            mysets.floating_ip['floating_ip']['floating_network_id']=self.network_id
            self.quantum.create_floatingip(mysets.floating_ip)
            for sec_grp in mysets.update_sec_port['security_groupl'][self.i]['port']['security_groups']:
                mysets.update_sec_port['security_groupl'][self.i]['port']['security_groups'][self.j]=self.sec_id[sec_grp]
            self.quantum.update_port(vip_portid,mysets.update_sec_port['security_groupl'][self.i]);
            self.i=self.i + 1;
    
    def Create_Floatingip(self,port_id):
        mysets.floating_ip['floating_ip']['port_id']=port_id
        mysets.floating_ip['floating_ip']['floating_network_id']=self.network_id
        self.quantum.create_floatingip(mysets.floating_ip)
