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
            
    def __init__(self, name, image, flavor, nova, create=False):
        print ">>>>>>"
        print name
        print image
        print flavor
        self.nova = nova
        self.name = name
        self.image = self.nova.images.find(name = image)
        self.flavor = self.nova.flavors.find(name = flavor)
        
        if create:
            self.nova.create_instance()
    
    def create_instance(self):
        if not (self.name or self.image or self.flavor):
            print "Name image and flavour must be set"
            return FAIL
        
        #create instance
        instance = self.nova.servers.create(self.name, self.image, self.flavor)
        status = instance.status
        print "Status: %s" % status,
        while status == 'BUILD':
            # Retrieve the instance again so the status field updates
            instance = self.nova.servers.get(instance.id)
            status = instance.status
            print ".",
            time.sleep(1)
            
        self.instance =instance
        print status
        print self.instance
        
        return SUCCESS
        

    def set_params(self, name, image, flavor,nova):
        if nova:
            self.nova = nova    
        if name:
            self.name = name
        if image:
            self.image = self.nova.images.find(image)
        if flavor:
            self.flavor = self.nova.flavors.find(flavor)
            
    def show_all_instances(self):
        print self.nova.servers.list(detailed=True)

    def set_floating_ip(self):
        floating_ip = self.nova.floating_ips.create()
        self.instance = self.nova.servers.get(self.instance.id)
        print "Floating IP: %s" % floating_ip
        self.instance.add_floating_ip(floating_ip)













