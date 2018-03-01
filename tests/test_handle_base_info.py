import unittest
from scripts.base_info_handler import BaseinfoHandler

import os
import sys
from io import StringIO

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
    'sitesinfo_url': 'localhost'}
      
"""



class HandeleBaseInfo(unittest.TestCase):
    def test_load_need_base_info_settings(self):
        """
        make sure we can change the path to the file of personal aliases
        """
        handler = BaseinfoHandler(testing=True)

        
        result = handler.get_single_value('sitesinfo_path')
        self.assertEqual(result, '%(BB_HOME)s/sites_list/')
        print('--------------->',handler )

if __name__ == '__main__':
    unittest.main()