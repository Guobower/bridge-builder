# README
## what user servieable data is store in the config folder
Base info is data stores in the config folder, that is individual for each 
installation of bridgebuilder

such settings are:  

`
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
    'sitesinfo_url': 'localhost'}
`