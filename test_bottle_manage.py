""" Tests for `bottle-manage` module. """
from __future__ import print_function

import bottle
import pytest



def test_bottle_manage(capsys):
    from bottle_manage import Manage
    from click import _compat
    _compat.is_ascii_encoding = lambda e: True

    app = bottle.Bottle()
    manage = Manage(app)

    @manage.command()
    @manage.option("--name", default='Bob')
    def hello(name):
        print("Hello " + name)

    with pytest.raises(SystemExit):
        manage()
    out, err = capsys.readouterr()
    assert 'Usage in out'

    with pytest.raises(SystemExit):
        manage(["hello"])
    out, err = capsys.readouterr()
    assert "Hello Bob" in out

    with pytest.raises(SystemExit):
        manage("hello --name Mike".split())
    out, err = capsys.readouterr()
    assert "Hello Mike" in out
