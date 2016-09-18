from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.shell.core.driver_context import InitCommandContext, ResourceCommandContext, AutoLoadResource, \
    AutoLoadAttribute, AutoLoadDetails, AutoLoadCommandContext


class {{cookiecutter.driver_name}} (ResourceDriverInterface):

    def cleanup(self):
        pass

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

    def get_inventory(self, context):
        """
        Queries the device and returns a list of sub-resources and attribute values to CloudShell
        :type context: AutoLoadCommandContext
        :rtype AutoLoadDetails
        """
        # run 'shellfoundry generate' in order to create classes that represent your data model
        resource = {{cookiecutter.model_name}}.create_from_context(context)
        resource.name = 'fill the name'

        # Add sub resources if needed
        # resource.add_sub_resource('1', sub resource)

        return resource.create_autoload_details()

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
