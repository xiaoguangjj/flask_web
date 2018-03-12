# -*- coding:utf-8 -*-
import main_user

def test_add():
    """

    :return:
    """
    param = {
        'text' : "bbbbb",
        'creater' : '123',
        'title': 'title12'
    }
    result = main_user.add(**param)
    return result

def test_query():
    param = {
        'title' : 'title',
        'creater':'123',
        'page': 1,
        'limit': 3,
    }
    result = main_user.query(**param)
    return result

def test_alter():

    param = {
        'title': 'title12',
        'text' : "bbbbbccccccc",
        'creater' : '嗡嗡',
    }
    result = main_user.alter(**param)
    return result

def test_info():
    param = {
        'title' : 'title',
        'creater':'123',
    }
    result = main_user.info(**param)
    return result

if __name__ == "__main__":

    result = test_add()
    # result = test_query()
    # result = test_alter()
    # result = test_info()
    print result