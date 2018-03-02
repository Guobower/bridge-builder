# -*- encoding: utf-8 -*-
import collections 
"""
This template describes some values that should be installed once 
per bridgebuilder instance.
It will be read and checked for new entries each time a bridgebuilder is started
It is an ordered dict, so we get questions to set values in a predefined sequence
"""
BASE_DEFAULTS = collections.OrderedDict({
    
    'erp_system' : {
        'display' : 'Erp-System',                 # display
        'help' : 'what Erp System to use by default. Possible values are odoo, flectra, cubicerp',    # help
        'default' : 'flectra'       # default
    },
    'erp_system_version' : {
        'display' : 'Erp-System-version',                 # display
        'help' : 'what what version of the erp system to use. possible values depend on the used erp',    # help
        'default' : '1.0'       # default
        
    },
    'editor' : {
        'display' : 'editor',                 # display
        'help' : 'what editor to use when editing a server or site description',    # help
        'default' : 'pico'       # default
    },
    'sitesinfo_path' : {
        'display' : 'sitesinfo path',                 # display
        'help' : 'path to the folder where sites.py and sites_local.py is found\nThis folder should be maintained by git',    # help
        'default' : '%(BB_HOME)s/sites_list/'       # default
    },
    'sitesinfo_url' : {
        'display' : 'sitesinfo url',                 # display
        'help' : 'url to the repository where sites.py and sites_local.py is maintained.\nIf it is localhost it will be created for you but not added to a repo',    # help
        'default' : 'https://gitlab.redcor.ch/redcor_customers/sites_list.git'   # default
    },
    'project_path' : {
        'display' : 'project path',                 # display
        'help' : 'path to the projects\nHere a structure for each odoo site is created to build and run odoo servers',         # help
        'default' : '%(USER_HOME)s/projects'        # default
    },
    'odoo_server_data_path' : {
        'display' : 'server data path',              # display
        'help' : """path to server data. Here for every site a set of folders is created
                    that will contain the servers config filestore, log- and dump-files.""", 
        'default' : '%(USER_HOME)s/odoo_instances'   # default
    },
    'docker_dumper_image' : {
        'display' : 'Image to be used to create a dumper container',              # display
        'help' : """
        When transfering data between sites we need a helper docker container 
        that can access the database and dump the data into a file""",
        'default' : 'robertredcor/dumper',
    },
    'repo_mapper' : {
        'display' : 'Access Urls to the source code repositories',              # display
        'help' : """What is the urls to use when accesing github or gitlab.
                    provide a comma separated list of repository=url pairs\n
                    default "gitlab.redcor.ch=ssh://git@gitlab.redcor.ch:10022/""",
        'default' : 'gitlab.redcor.ch=ssh://git@gitlab.redcor.ch:10022/',
    },
    'local_user_mail' : {
        'display' : 'mail address of the local user',              # display
        'help' : 'mail address of the local user', # help
        'default' : '%(ACT_USER)s@redo2oo.ch',
    },
    'db_password' : {
        'display' : 'DB Password',              # display
        'help' : 'default password to access the database',          # help
        'default' : 'admin'   # default
    },
})
