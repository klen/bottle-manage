Bottle Manage
#############

.. _description:

Bottle Manage -- Short description.

.. _badges:

.. image:: http://img.shields.io/travis/klen/bottle-manage.svg?style=flat-square
    :target: http://travis-ci.org/klen/bottle-manage
    :alt: Build Status

.. image:: http://img.shields.io/coveralls/klen/bottle-manage.svg?style=flat-square
    :target: https://coveralls.io/r/klen/bottle-manage
    :alt: Coverals

.. image:: http://img.shields.io/pypi/v/bottle-manage.svg?style=flat-square
    :target: https://pypi.python.org/pypi/bottle-manage

.. image:: http://img.shields.io/pypi/dm/bottle-manage.svg?style=flat-square
    :target: https://pypi.python.org/pypi/bottle-manage

.. image:: http://img.shields.io/gratipay/klen.svg?style=flat-square
    :target: https://www.gratipay.com/klen/
    :alt: Donate

.. _contents:

.. contents::

.. _requirements:

Requirements
=============

- python >= 2.6

.. _installation:

Installation
=============

**Bottle Manage** should be installed using pip: ::

    pip install bottle-manage

.. _usage:

Usage
=====

`manage.py`: ::

    from bottle import Bottle
    from bottle_manage import Manage

    app = Bottle()
    manage = Manage(app)

    @manage.shell
    def context():
        from .models import Partner, Record, db # noqa
        ctx = locals()
        ctx['app'] = app
        ctx['db'] = db.database
        return ctx


    @manage.command
    def db():
        """ Initialize the database."""
        from peewee_migrate.core import Router
        router = Router(
            os.path.join(app.config['ROOT_DIR'], 'migrations'), DATABASE=app.config['DATABASE_URI'])
        router.run()


    @manage.command
    def runserver(reloader=False, debug=False, port=5000):
        """ Run the application. """
        app.run(reloader=reloader, debug=debug, port=port)


    if __name__ == '__main__':
        manage()

::

    $ ./manage.py --help

.. _bugtracker:

Bug tracker
===========

If you have any suggestions, bug reports or
annoyances please report them to the issue tracker
at https://github.com/klen/bottle-manage/issues

.. _contributing:

Contributing
============

Development of Bottle Manage happens at: https://github.com/klen/bottle-manage


Contributors
=============

* klen_ (Kirill Klenov)

.. _license:

License
=======

Licensed under a `BSD license`_.

.. _links:

.. _BSD license: http://www.linfo.org/bsdlicense.html
.. _klen: https://github.com/klen
