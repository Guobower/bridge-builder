# -*- encoding: utf-8 -*-
import click
class BaseinfoHandler(object):
    out_file = None # fileobject to write data to
    in_file  = None # fileobject to get data from
    info_dic = {}

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

    def __init__ (self, in_file, out_file, reset=False, testing = False):
        self.testing = testing
        self.reset = reset

        self.in_file = in_file # we can pass a fileobject when testing
        if isinstance(in_file, str):
            self.in_file = open(in_file, 'r')
        self.out_file = out_file # we can pass a fileobject when testing
        if isinstance(out_file, str):
            self.out_file = open(out_file,'w')


        # if we need to reset, we get a new set of values from config
        if reset:
            from config import BASE_DEFAULTS
            self.info_dic = BASE_DEFAULTS
        else:
            from config import BASE_INFO
            self.info_dic = BASE_INFO

    # ----------------------------------
    # get_single_value
    # ask value from user
    # @name         : name of the value
    # @explanation  : explanation of the value
    # @default      : default value
    # @prompt       : prompt to display
    # ----------------------------------
    def get_single_value(self, name):
        """
        ask value from user
        @name         : name of the value

        the following is gathered from the actual values or the defaults
        ----------------------------------------------------------------
        @explanation  : explanation of the value
        @default      : default value
        @prompt       : prompt to display
        """

        info = self.info_dic.get(name, {})
        if info:
            v_name, explanation, default = info
        else:
            return ''
        prompt='%s [%s]:'

        # get input from user for a single value. present expanation and default value
        testing = self.testing
        if not testing:
            click.echo('*' * 50)
            click.echo(explanation)
            result = click.prompt(prompt % (name, default))
        if not result:
            result = default
        return result

    def set_base_info(self):
        "write base info back to the config folder"
        info = 'base_info = %s' % self.info_dic
        open(self.outfile, 'w').write(info)

    def get_base_info(self, base_info, base_defaults):
        "collect base info from user, update base_info"
        for k, v in base_defaults.items():
            name, explanation, default = v
            # use value as stored, default otherwise
            default = BASE_INFO.get(k, default)
            base_info[k] = get_single_value(name, explanation, default)

    # ----------------------------------
    # update_base_info
    # collects localdata that will be stored in config/base_info.py
    # @base_info_path   : path to config/base_info.pyconfig/base_info.py
    # @default_values   : dictionary with default values
    # ----------------------------------
    def update_base_info(self, base_info_path, defaults):
        """
        collects localdata that will be stored in config/base_info.py
        @base_info_path   : path to config/base_info.pyconfig/base_info.py
        @default_values   : dictionary with default values
        """
        base_info = {}
        self.get_base_info(base_info, defaults)
        self.set_base_info(base_info, base_info_path)
        click.echo('%s created' % base_info_path)

from io import StringIO
output = StringIO()
input = StringIO()
BaseinfoHandler(output,output)