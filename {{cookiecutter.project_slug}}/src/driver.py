from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.shell.core.driver_context import InitCommandContext, ResourceCommandContext, AutoLoadResource, \
    AutoLoadAttribute, AutoLoadDetails, AutoLoadCommandContext
# run 'shellfoundry generate' to generate data model classes
from data_model import *


class {{cookiecutter.driver_name}} (ResourceDriverInterface):

    def __init__(self):
        """
        ctor must be without arguments, it is created with reflection at run time
        """
        pass

    def initialize(self, context):
        """
        Called upon driver initialization
        :type context: InitCommandContext
        :return:
        """
        pass

    def cleanup(self):
        pass


    def get_inventory(self, context):
        """
        Auto discovery - This function queries the device, discovers it's specification and structure and autoloads it into CloudShell
        :type context: AutoLoadCommandContext
        :rtype AutoLoadDetails
        """

        # run 'shellfoundry generate' in order to create classes that represent your data model
        resource = {{cookiecutter.model_name}}.create_from_context(context)
        resource.vendor = 'specify the shell vendor'
        resource.model = 'specify the shell model'


        # Example of a shell with chassis->module->port
        chassis1 = GenericChassis()
        chassis1.name = 'Chassis 1'
        chassis1.model = 'WS-X4232-GB-RJ'
        chassis1.serial_number = 'JAE053002JD'
        resource.add_sub_resource('1', chassis1)

        module1 = GenericModule()
        module1.name = 'Module 1'
        module1.model = 'WS-X5561-GB-AB'
        module1.serial_number = 'TGA053972JD'
        chassis1.add_sub_resource('1', module1)

        port1 = GenericPort()
        port1.name = 'Port 1'
        port1.mac_address = 'fe80::e10c:f055:f7f1:bb7t16'
        port1.ipv4_address = '192.168.10.7'
        module1.add_sub_resource('1', port1)

        return resource.create_autoload_details()
        ##

    def method_one(self, context,):
        """
        A simple driver command
        :type context: ResourceCommandContext
        :param context: the context the command runs on
        :return:
        """
        # run 'shellfoundry generate' in order to create classes that represent your data model
        resource = {{cookiecutter.model_name}}.create_from_context(context)
        pass
