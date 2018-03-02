# -*- encoding: utf-8 -*-
import click
import os
import collections
import getpass
ACT_USER = getpass.getuser()
BB_HOME = os.sep.join( os.path.abspath(__file__).split(os.sep)[:-2])
BD_template = """
# -*- encoding: utf-8 -*-
import collections 
BASE_INFO = collections.OrderedDict(
    %s
)
"""
USER_HOME = os.path.expanduser('~')

class BaseinfoHandler(object):
    """
    Base info is data stores in the config folder, that is individual for each 
    installation of bridgebuilder

    such settings are:
    base_info = {
        # what image to use when creating a dumper
        # see readme in the dumper folder
        'docker_dumper_image': 'robertredcor/dumper',

        # what editor to use when bb needs one
        'editor': 'atom',

        # what mail to use when to send all mails to, when running locally
        # this works in conjunction with red_override_email_recipients
        'local_user_mail': 'robert@redo2oo.ch',

        # where is the data stored on the server
        # this is used in conjunction with the dumper
        # when a server is copied from one place to an other
        'odoo_server_data_path': '/home/robert/odoo_projects_data',

        # where are buildout environments to be created
        'project_path': '/home/robert/projects',

        # from where do we get the gitlab images
        'repo_mapper': 'gitlab.redcor.ch=ssh://git@gitlab.redcor.ch:10022/',

        # where are the siteslists stored
        'sitesinfo_path': '/home/robert/odoo_instances/sites_list',
        'sitesinfo_url': 'localhost'
    }
    """  
    out_file = None # fileobject to write data to
    in_file  = None # fileobject to get data from
    info_dic = collections.OrderedDict()
    base_info_path = ''
    # do we need to writ values out to disk
    dirty = False
    
    def __init__ (self, quiet=False, reset=False, testing = False):
        from config.base_defaults_template import BASE_DEFAULTS as BD

        self.testing = testing
        self.reset = reset
        self.quiet = quiet
        
        import getpass
        ACT_USER = getpass.getuser()        
        self.default_dic = BD

        try:
            from config.base_info import BASE_INFO
        except:
            self._create_base_info()
            # now loading should work
            from config.base_info import BASE_INFO
            
        self.info_dic = BASE_INFO
        # if we need to reset, we get a new set of values from config
        if reset or not BASE_INFO:
            self._create_base_info()   
                
    def _create_base_info(self):
        result = []
        for k,v in self.default_dic.items():
            result.append((k, v['default']))
        open('%s/config/base_info.py' % BB_HOME, 'w').write(BD_template % result)
                
    @property
    # ACT_USER is the logged in user
    def act_user(self):
        return self.ACT_USER
                
    # ----------------------------------
    # get_single_value
    # ask value from user
    # @name         : name of the value
    # ----------------------------------
    def ask_single_value(self, name):
        """
        ask value from user
        @name         : name of the value

        the following is gathered from the actual values or the defaults
        ----------------------------------------------------------------
        @explanation  : explanation of the value
        @default      : default value
        @prompt       : prompt to display
        """

        old_val = self.info_dic.get(name, {})
        # get prompt, help and default value
        dd = self.default_dic.get(name, {})
        display = dd.get('display', '')
        help = dd.get('help', '')
        default = dd.get('default', '')
        prompt='%s [%s]:'

        # get input from user for a single value. present expanation and default value
        testing = self.testing
        result = ''
        if not testing:
            click.echo('*' * 50)
            click.echo(explanation)
            result = click.prompt(prompt % (name, default))
        if not result:
            result = default
        return result
    
    def ask_all_values(self, values=''):
        """
        @values : string with name=value, .. pairs
                  it can also be a comma separated list of names
                  or all for sall values
        """
        # let the user set values
        # 
        if values == 'all':
            for k in self.default_dic.keys():
                self.ask_single_value(k)  
        else:
            parts = values.split(',')
            for part in parts:
                pps = part.split('=')
                pps = pps + ['']
                if pps[1]:
                    self.set_single_value(pps[0], pps[1])
                else:
                    # only name, no value
                    self.ask_single_value(pps[0])

    def set_single_value(self, name, value):
        # set value to be written out the defaults
        if not name in self.info_dic:
            return 
        old_val = self.info_dic.get(name)
        self.info_dic[name] = value
        if old_val != value:
            self.dirty = True
        
    # ----------------------------------
    # update_base_info
    # collects localdata that will be stored in config/base_info.py
    # @base_info_path   : path to config/base_info.pyconfig/base_info.py
    # @default_values   : dictionary with default values
    # ----------------------------------
    def update_base_info(self, return_dic = None):
        """
        collects localdata that will be stored in config/base_info.py
        @return_dic   : if return_dic is a dictionary, we will return it with values, and not update the real file
        """
        
        if isinstance(return_dic, dict):
            for k,v in self.info_dic.items():
                return_dic[k] = v
        else:
            path = self.base_info_path
            p_dir = os.path.dirname(path)
            if os.path.isdir(p_dir):
                template = """import collections
                GLOBALDEFAULTS=collections.OrderedDict(%s)
                """ % self.info_dic.items()               
                open(path, 'w').write(template)
            click.echo('%s created' % self.base_info_path)
            
    def show_base_info(self):
        # list all base info
        gl = globals()
        for k, v in self.default_dic.items():
            click.echo('-' * 80)
            click.echo(v['help'])
            click.echo('value=%s' % (self.info_dic[k] % gl))

    @property
    def editor(self):
        return self.info_dic['editor']
            
    @property        
    def nginx_path(self):

        # try to get also NGINX_PATH
        # if not possible, provide warning and assume standard location
        try:
            from localdata import NGINX_PATH
        except ImportError:
            if not self.quiet:
                print( bcolors.WARNING + '*' * 80)
                print( 'could not read nginx path from config.localdata')
                print( 'assuming it is: /etc/nginx/')
                print( 'you can fix this by executing: bin/e')
                print( "and adding: NGINX_PATH = '/etc/nginx/'")
                print( '*' * 80 + bcolors.ENDC)
            NGINX_PATH = '/etc/nginx/'

    @nginx_path.setter
    def set_nginx_path(self, value):
        self
            
    @property        
    def apache_path(self):

        # try to get also NGINX_PATH
        # if not possible, provide warning and assume standard location
        try:
            from localdata import NGINX_PATH
        except ImportError:
            if not self.quiet:
                print( bcolors.WARNING + '*' * 80)
                print( 'could not read nginx path from config.localdata')
                print( 'assuming it is: /etc/nginx/')
                print( 'you can fix this by executing: bin/e')
                print( "and adding: NGINX_PATH = '/etc/nginx/'")
                print( '*' * 80 + bcolors.ENDC)
            NGINX_PATH = '/etc/nginx/'

    @apache_path.setter
    def set_apache_path(self, value):
        pass
    
    def xxx(self):
        BASEINFO_CHANGED = """
        %s--------------------------------------------------
        The structure of the config files have changed.
        You will be asked to provide some config data again.
        --------------------------------------------------%s
        """ %(bcolors.FAIL, bcolors.ENDC)
        
        # base defaults are the defaults we are using for the base info if they where not set
        user_home = os.path.expanduser('~')
        from . base_defaults_template import BASE_DEFAULTS
        for k, v in BASE_DEFAULTS.items():
            for vv in v:
                vv = vv % globals()
        try:
            from base_info import base_info as BASE_INFO
            NEED_BASEINFO = False
            # check whether BASE_DEFAULTS has new keys
            for k in BASE_DEFAULTS.keys():
                if not BASE_INFO.has_key(k):
                    NEED_BASEINFO = True
                    print( BASEINFO_CHANGED)
        except ImportError:
            NEED_BASEINFO = True
        

