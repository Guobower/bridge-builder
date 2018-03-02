# -*- encoding: utf-8 -*-
import os
import sys

# BB_HOME points to the installations folder of bridge builder
BB_HOME = os.sep.join( os.path.abspath(__file__).split(os.sep)[:-2])


BASE_INFO = {}

# some formatting colors
class bcolors:
    """
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
# create a bas_info_handler that deals with all geting and setting of base info
from scripts.base_info_handler import BaseinfoHandler
base_info_handler = BaseinfoHandler()

# what folders do we need to create in odoo_sites for a new site
FOLDERNAMES = ['addons','dump','etc','filestore', 'log', 'ssl']


# sites is a combination created from "regular" sites listed in sites.py
# an a list of localsites listed in local_sites.py
#from sites import SITES, SITES_L as SITES_LOCAL
# start with checking whether installation is finished
try:
    pwd = os.getcwd()
    from scripts.sites_handler import SitesHandler
    sites_handler = SitesHandler(BB_HOME) # will exit when installation not yet finished
    SITES, SITES_LOCAL = sites_handler.get_sites()
    # MARKER is used to mark the position in sites.py to add a new site description
    MARKER = sites_handler.marker # from messages.py
    try:
        from localdata import REMOTE_USER_DIC, APACHE_PATH, DB_USER, DB_PASSWORD
    except ImportError:
        print( 'please create config/localdata.py')
        print( 'it must have values for REMOTE_USER_DIC, APACHE_PATH, DB_USER, DB_PASSWORD, DB_PASSWORD_LOCAL')
        print( 'use template/localdata.py as template')
        sys.exit()
    except SyntaxError:
        print( 'please edit config/localdata.py')
    os.chdir(pwd)
except ImportError:
    sites_handler = None
except OSError:
    # we probably runing from within docker
    BASE_INFO['odoo_server_data_path'] = '/mnt/sites'
    if os.getcwd() == '/mnt/sites':
        print( '------------------------------')
        raise ImportError()

# make sure we have the sites-list updated
if sites_handler:
    # automatically update sites list only, when BASE_INFO[''] is set
    sites_handler.pull()

# file to which site configuration will be written
LOGIN_INFO_FILE_TEMPLATE = '%s/login_info.cfg.in'

# file to which pip requirements will be written
REQUIREMENTS_FILE_TEMPLATE = '%s/install/requirements.txt'

SITES_HOME =  os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

try:
    from version_info import VERSION
except:
    VERSION = None

p =  os.path.split(os.path.realpath(__file__))[0]
if not os.path.exists('%s/globaldefaults.py' % p):
    ## silently copy the defualts file
    #act = os.getcwd()
    #os.chdir(p)
    open('%s/globaldefaults.py' % p, 'w').write('import collections\nGLOBALDEFAULTS=collections.OrderedDict()')
    #os.chdir(act)
from . import globaldefaults
GLOBALDEFAULTS = globaldefaults.GLOBALDEFAULTS

