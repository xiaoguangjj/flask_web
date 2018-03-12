# -*- coding:utf-8 -*-
import main


def test_add():
    """

    :return:
    """
    param = {
        'text' : "aaaa",
        'creater' : '123',
        'title': 'title'
    }

    result = add(**param)
    print result
    assert False