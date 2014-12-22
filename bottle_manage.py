"""
    bottle-manage description.

"""

# Package information
# ===================

__version__ = "0.1.0"
__project__ = "bottle-manage"
__author__ = "Kirill Klenov <horneds@gmail.com>"
__license__ = "MIT"

import click


class Manage(object):

    def __init__(self, app, port=5000, host='127.0.0.1', context=None):
        self.cli = click.group()(lambda: None)
        self.app = app

        app.config.setdefault('MANAGE_SHELL', context or {'app': app})

        @self.command()
        def shell():
            """ Run the application shell. """
            from werkzeug import script

            ctx = app.config['MANAGE_SHELL']
            if callable(ctx):
                ctx = ctx()

            return script.make_shell(lambda: ctx, "Loaded objects: " + ", ".join(ctx.keys()))()

        @self.command()
        @self.option('--reload/--no-reload', default=False)
        @self.option('--debug/--no-debug', default=False)
        @self.option('--port', default=5000)
        def runserver(**kwargs):
            """ Run the application. """
            app.run(**kwargs)

    @staticmethod
    def option(*args, **kwargs):
        return click.option(*args, **kwargs)

    def command(self, *args, **kwargs):
        return self.cli.command(*args, **kwargs)

    def shell(self, func):
        self.app.config['MANAGE_SHELL'] = func

    def __call__(self, *args, **kwargs):
        return self.cli(*args, **kwargs) # noqa

# pylama:ignore=E1103,W0612
