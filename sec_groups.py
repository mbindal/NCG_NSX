import inventory as config

class security_groups(object):
    def __init__(self, neutron):
        self.neutron = neutron
        
    def create_security_groups(self):
        for security_group in config.security_groups['security_groups']:
            self.neutron.create_security_group(security_group);
        security_group_list = self.neutron.list_security_groups()['security_groups'];
        for security_group in security_group_list:
            if security_group['name'] in config.security_group_ids.keys():
                config.security_group_ids[security_group['name']] = security_group['id']

    def create_security_group_rule(self):
        security_group_list = self.neutron.list_security_groups()['security_groups'];
        for security_group in security_group_list:
            if security_group['name'] in config.security_group_rules.keys():
            	print ("Creating rules for tenant:  %s group: %s" % (security_group['tenant_id'], security_group['name']))
		for rule in config.security_group_rules[security_group['name']]:
            if 'remote_group_id' in rule['security_group_rule'].keys():
			    rmt_grp_id = config.security_group_ids[rule['security_group_rule']['remote_group_id']]
                rule['security_group_rule']['remote_group_id'] = rmt_grp_id
            rule['security_group_rule']['security_group_id'] = security_group['id']
            self.neutron.create_security_group_rule(rule)
