# Rick Mur - Juniper - 2015

from jnpr.junos import Device
from jnpr.junos.op.vlan import *
from vlanEls import *
import yaml

mySwitches = yaml.load(open("switchlist.yml").read())

if mySwitches:
    for sw in mySwitches["switches"]:
        dev = Device(sw, user="pytraining", password="Poclab123")
        dev.open()
        print ("Connected to " + dev.hostname)

        swStyle = dev.facts["switch_style"]
        if swStyle == "VLAN_L2NG":
            vlans = ElsVlanTable(dev)
        elif swStyle == "VLAN":
            vlans = VlanTable(dev)
        else:
            print ("This is not a switch")
            break

        vlans.get()

        if len(vlans) != 0:
            for vlan in vlans:
                print (vlan.vlan_name + " has ID " + vlan.tag)
        else:
            print ("No VLANs on this switch")

        dev.close()
