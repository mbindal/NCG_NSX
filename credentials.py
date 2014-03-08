#!/usr/bin/env python
import os
    
def get_keystone_creds():
    d = {}
    d['username'] = 'demo'
    d['password'] = 'password'
    d['auth_url'] = 'http://10.34.224.126:5000/v2.0'
    d['tenant_name'] = 'demo'
    return d

def get_nova_creds():
    d = {}
    d['username'] = 'admin'
    d['api_key'] = 'password'
    d['auth_url'] = 'http://10.34.224.126:5000/v2.0'
    d['project_id'] = 'demo'
    return d

