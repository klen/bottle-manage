""" Tests for `bottle-manage` module. """
from __future__ import print_function

import bottle
import pytest


def test_bottle_manage(capsys):
    from bottle_manage import Manage

    app = bottle.Bottle()
    manage = Manage(app)

    @manage.command
    def hello(name='Bob'):  ## noqa
        """ Say hello. """
        print("Hello " + name)

    with pytest.raises(SystemExit):
        manage([])
    out, err = capsys.readouterr()
    assert 'usage' in err + out

    with pytest.raises(SystemExit):
        manage(["hello"])
    out, err = capsys.readouterr()
    assert "Hello Bob" in out

    with pytest.raises(SystemExit):
        manage("hello --name Mike".split())
    out, err = capsys.readouterr()
    assert "Hello Mike" in out
