# -*- encoding: utf-8 -*-
"""
This template describes some values that should be installed once 
per bridgebuilder instance.
It will be read and checked for new entries each time a bridgebuilder is started
"""
BASE_DEFAULTS = {
    #name, explanation, default
    'sitesinfo_path' : (
        'sitesinfo path',                 # display
        'path to the folder where sites.py and sites_local.py is found\nThis folder should be maintained by git',    # help
        '%s/sites_list/' % BASE_PATH  # default
    ),
    'sitesinfo_url' : (
        'sitesinfo url',                 # display
        'url to the repository where sites.py and sites_local.py is maintained.\nIf it is localhost it will be created for you but not added to a repo',    # help
        'https://gitlab.redcor.ch/redcor_customers/sites_list.git'   # default
    ),
    'project_path' : (
        'project path',                 # display
        'path to the projects\nHere a structure for each odoo site is created to build and run odoo servers',         # help
        '%s/projects' % user_home  # default
    ),
    'odoo_server_data_path' : (
        'server data path',              # display
        'path to server data. Here for every site a set of folders is created\nthat will contain the servers config filestore, log- and dump-files.',          # help
        '%s/odoo_instances' % user_home  # default
    ),
    #'docker_path_map' : (
        #'docker path map. use , to separate parts',              # display
        #'docker volume mappings when docker is run locally.', # help
        #ACT_USER == 'root' and () or ('%s/' % user_home, '/root/')
    #),
    'docker_dumper_image' : (
        'Image to be used to create a dumper container',              # display
        'When transfering data between sites we need a helper docker container that can access the database and dump the data into a file', # help
        'robertredcor/dumper',
    ),
    'repo_mapper' : (
        'Access Urls to the source code repositories',              # display
        'What is the urls to use when accesing github or gitlab.\n'\
        'provide a comma separated list of repository=url pairs\n'\
        'default "gitlab.redcor.ch=ssh://git@gitlab.redcor.ch:10022/"',
        'gitlab.redcor.ch=ssh://git@gitlab.redcor.ch:10022/',
    ),
    'local_user_mail' : (
        'mail address of the local user',              # display
        'mail address of the local user', # help
        '%s@redo2oo.ch' % ACT_USER,
    )
}
