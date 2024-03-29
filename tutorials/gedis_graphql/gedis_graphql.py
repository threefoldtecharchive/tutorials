from Jumpscale import j


JSBASE = j.application.JSBaseClass


class gedis_graphql(j.application.JSBaseClass):
    def __init__(self):

        self.__jslocation__ = "j.tutorials.graphql"
        self.name = "graphql"
        JSBASE.__init__(self)

    ## Entry point
    def run(self):
        """

        """
        # Begining
        j.sal.tutorial.print_headline(
            """In this tutorial we will go through DigitalMe Servers, Gedis, Actors
We will create a simple webserver with graphql
Using sanic with graphene serving Vue.JS page with Apollo"""
        )
        j.sal.tutorial.get_input("Press ENTER to continue... ")

        j.sal.tutorial.print_explain(
            """To do so we will do the following steps:
1- Build and install graphql requirments:
-> ujson
-> graphql_ws
-> sanic>=0.7.0
-> graphene>=2.0
-> sanic-graphql>=1.1.0
"""
        )
        j.sal.tutorial.print_command("j.builders.runtimes.graphql.install()")
        j.sal.tutorial.get_input("Press ENTER to continue... ")
        j.builders.runtimes.graphql.install(reset=True)

        j.sal.tutorial.print_explain(
            """2- Create an instance from sanic server. which will initially create a gedis sever
with executing the following commands
"""
        )
        j.sal.tutorial.print_command('tutorial = j.servers.sanic.get(name="sanic_tutorial")')
        j.sal.tutorial.get_input("Press ENTER to continue... ")
        j.sal.tutorial.print_explain("""It will execute the following""")
        j.sal.tutorial.print_command('server = j.servers.gedis.configure(host="0.0.0.0", port=8888)')
        j.sal.tutorial.get_input("Press ENTER to continue... ")
        j.sal.tutorial.print_explain("""Then we add our actor to this server""")
        j.sal.tutorial.print_command(
            'server.actor_add("/sandbox/code/github/threefoldtech/digitalmeX/DigitalMe/tools/graphql_tutorial/graphql_actor.py")'
        )
        j.sal.tutorial.get_input("Press ENTER to continue... ")
        j.sal.tutorial.print_explain("""Then we save it and start""")
        j.sal.tutorial.print_command("server.save()")
        j.sal.tutorial.print_command("server.start()")
        tutorial = j.servers.sanic.get(name="sanic_tutorial")
        j.sal.tutorial.get_input("Press ENTER to continue (Start Server)... ")
        j.sal.tutorial.print_command("tutorial.start()")
        tutorial.start()
        j.sal.tutorial.print_headline2("Test graphql at: http://172.17.0.2:8001/")
        j.sal.tutorial.print_headline2("Test Vue.JS with apollo at: http://172.17.0.2:8001/posts")
        j.sal.tutorial.print_headline2("Test websockets at: http://172.17.0.2:8001/counter")
        j.sal.tutorial.get_input("Press ENTER to Finish")

    # delete all stuff
    def cleanup(self):
        """
        Cleanup a previous run of the tutorial
        """
        if j.clients.itsyouonline.exists("tutorials"):
            j.clients.itsyouonline.delete("tutorials")

        if j.clients.zhub.exists("tutorials"):
            j.clients.zhub.delete("tutorials")

        j.builders.apps.hub.stop()
        j.builders.apps.hub.reset()

        if j.clients.zos.exists("tutorials"):
            j.clients.zos.get("zhub").containers.get("tutorials").stop()

