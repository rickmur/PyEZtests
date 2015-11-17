# Rick Mur - Juniper - 2015

from jnpr.junos import Device
from jnpr.junos.op.bgp import BGPNeighborTable as BGPtable


import yaml
from pprint import pprint as pp



myVars = yaml.load(open("switchlist.yml").read())

for switch in myVars["switches"]:
    dev = Device(switch, user="pytraining", password="Poclab123")
    dev.open()

    neighbors = BGPtable(dev)
    neighbors.get()

    print ("Connected to " + dev.hostname)
    if len(neighbors) != 0:
        for neighbor in neighbors:
            peer = neighbor.neighbor.split("+")
            initiate = "locally"
            if peer[1] != "179":
                initiate = "by peer"
            print ("Neighbor " + peer[0] + " is AS " + neighbor.peer_as + " state is: " + neighbor.state + " session was initiated " + initiate)
    else:
        print ("No neighbors")

