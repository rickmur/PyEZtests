__author__ = 'rickmur'

# import stuff
from jnpr.junos import Device
from jnpr.junos.version import VERSION
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import CommitError
from jnpr.junos.exception import ConfigLoadError
from jnpr.junos.exception import ConnectAuthError
from jnpr.junos.exception import RpcTimeoutError
import yaml

#temp
from getpass import getpass



#load config change

try:

    print('This is PyEZ version %s' % (VERSION))

    # ask for inputs
    uid = raw_input("Username? ")
    pwd = getpass("Password? ")


    # start setting it up
    dev = Device('172.22.1.3', user = uid, password = pwd)
    dev.open()
    #pprint(dev.facts)
    print('the JUNOS version of this device is %s' % (dev.facts["version"]))

    con = Config(dev)

    # load YML variables
    myFile = open('data.yml')
    data = yaml.load(myFile.read())

    con.load(template_path='template.conf', template_vars=data)
    if (con.commit()):
        print 'SUCCESSSS'
    else:
        print 'whoops'

    dev.close()


except ConnectAuthError:
    print 'Credentials invalid!'
except ConfigLoadError as e:
    print 'Config template not correct!!!: ', e
except CommitError as e:
    print 'Config could not commit: ', e
except RpcTimeoutError as e:
    print 'Config committed, but RPC timed out: ', e
except Exception as e:
    print 'something went wrong: ', e