import inventory as mysets
class sec_groups(object):
    def __init__(self,quantum):
            self.i=self.j=0;
            self.quantum=quantum
    #creation of pools and pool members
    def Create_securitygroup(self):
        sec_group_list=self.quantum.create_security_group(mysets.security_groups_json)['security_group'];
        for groups in sec_group_list:
            mysets.sec_id[groups['name']]=groups['id']
    def Create_securitygroupules(self):
        security_groups = self.quantum.list_security_groups()['security_groups']
        for security_group in security_groups:
            print ("Creating rules for tenant:  %s group: %s" %
                    (security_group['tenant_id'], security_group['name']))
            for rules in mysets.sec_group_rules[security_group['name']]['security_group_rules']:
                rules['tenant_id']=security_group['tenant_id']
                rules['security_group_id']=security_group['id']
            self.quantum.create_security_group_rule(mysets.sec_group_rules[security_group['name']])