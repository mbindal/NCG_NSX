import os
import time
import novaclient.v1_1.client as nvclient

SUCCESS = 0
FAIL = 1

class novaInstance:
    #class to create servers using nova 
    
    def __init__(self,nova):
        self.name = None
        self.image = None
        self.flavor = None
        self.nova = nova
            
    def __init__(self, name, image, flavor, create=False,nova):
        self.name = name
        self.image = image
        self.flavor = flavor
        self.nova = nova
        
        if create:
            self.nova.create_instance()
    
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
        

    def set_params(self, name, image, flavor,nova):
        if name:
            self.name = name
        if image:
            self.image = image
        if flavor:
            self.flavor = flavor
        if nova:
            self.nova = nova    
            
    def show_all_instances(self):
        print nova.servers.list(detailed=True)