__author__ = "rickmur"

# import stuff
from jnpr.junos import Device
from jnpr.junos.version import VERSION
from jnpr.junos.utils.config import Config
import yaml
import sys
#temp
from getpass import getpass
from pprint import pprint


print('This is PyEZ version %s' % (VERSION))



# ask for inputs
uid = raw_input("Username? ")
pwd = getpass("Password? ")


# start setting it up
dev = Device('172.22.1.3', user = uid, password = pwd)
dev.open()
#pprint(dev.facts)
print('the JUNOS version of this device is %s' % (dev.facts["version"]))




#load config change

try:

  con = Config(dev)

  # load YML variables
  myFile = open('data.yml')
  data = yaml.load(myFile.read())

  con.load(template_path='template.conf', template_vars=data)
  if (con.commit()):
    print 'SUCCESSSS'
  else:
    print 'whoops'

except Exception as e:
  print 'Exception caught you: ', e
except:
  print 'something went wrong: ', sys.exc_info()[0]





dev.close()
