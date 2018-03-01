# -*- encoding: utf-8 -*-
import click
import os
import collections
class BaseinfoHandler(object):
    out_file = None # fileobject to write data to
    in_file  = None # fileobject to get data from
    info_dic = collections.OrderedDict()

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

    def __init__ (self, reset=False, testing = False):
        self.testing = testing
        self.reset = reset

        from config import BASE_INFO
        self.info_dic = BASE_INFO
        # if we need to reset, we get a new set of values from config
        if reset or not BASE_INFO:
            from config import base_defaults_template
            info = base_defaults_template.BASE_DEFAULTS
            for k,v in info.items():
                self.info_dic[k] = v

    # ----------------------------------
    # get_single_value
    # ask value from user
    # @name         : name of the value
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
        result = ''
        if not testing:
            click.echo('*' * 50)
            click.echo(explanation)
            result = click.prompt(prompt % (name, default))
        if not result:
            result = default
        return result

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
            click.echo('%s created' % base_info_path)

