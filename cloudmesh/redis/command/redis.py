from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.redis.Redis import Redis



class RedisCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_redis(self, args, arguments):
        """
        ::

          Usage:
                redis start USER HOST PORT [DIR]
                redis stop USER HOST PORT [DIR]


          This command does some useful things.

          Arguments:
              USER  todo
              HOST  todo
              PORT  todo
              DIR   todo

          Description:
              redis start USER HOST PORT [DIR]
                todo

        """


        VERBOSE(arguments)

        redis = Redis(host=arguments.HOST, user=arguments.USER, port=arguments.PORT, dir=arguments.DIR)


        if arguments.start:
            redis.start()

        elif arguments.stop:
            redis.stop()


        return ""
