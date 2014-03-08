import os
import time
import novaclient.v1_1.client as nvclient
from credentials import get_nova_creds

SUCCESS = 0
FAIL = 1

class novaInstance:
    #class to create servers using nova 
    
    def __init__(self):
        self.name = None
        self.image = None
        self.flavor = None
        creds = get_nova_creds()
        self.nova = nvclient.Client(**creds)
            
    def __init__(self, name, image, flavor, create=False):
        self.name = name
        self.image = image
        self.flavor = flavor
        
        creds = get_nova_creds()
        self.nova = nvclient.Client(**creds)
        
        if create:
            self.create_instance()
    
    def create_instance(self):
        if !(self.name or self.image or self.flavor):
            print "Name image and flavour must be set"
            return FAIL
        
        #create instance
        instance = self.nova.servers.create(name, image, flavor)
        status = instance.status
        print "Status: %s" % status,
        while status == 'BUILD':
            # Retrieve the instance again so the status field updates
            instance = nova.servers.get(instance.id)
            status = instance.status
            print ".",
            time.sleep(1)
            
        self.instance =instance
        print status
        
        return SUCCESS
        

    def set_params(self, name, image, flavor):
        if name:
            self.name = name
        if image:
            self.image = image
        if flavor:
            self.flavor = flavor
            
    def show_all_instances(self):
        print nova.servers.list(detailed=True)



