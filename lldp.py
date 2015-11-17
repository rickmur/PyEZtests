# Rick Mur - Juniper - 2015

from jnpr.junos import Device
from jnpr.junos.op.lldp import LLDPNeighborTable
import yaml
from pprint import pprint as pp

myVars = yaml.load(open("switchlist.yml").read())

for switch in myVars["switches"]:
    dev = Device(switch, user="pytraining", password="Poclab123")
    dev.open()

    neighbors = LLDPNeighborTable(dev)
    neighbors.get()

    print ("Connected to " + dev.hostname)
    if len(neighbors) != 0:
        for neighbor in neighbors:
            print ("Interface " + neighbor.local_int + " is connecting to " + neighbor.remote_sysname)
    else:
        print ("No neighbors")


