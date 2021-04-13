import re

from pytest import fixture

from API.json_placeholder import BlogAPI

regex = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'


def check_email_format(*arg):
    """
    Validate email
    :param arg:
    :return:
    """
    if (re.search(regex, *arg)):
        return True
    else:
        print('email is not valid {}'.format(*arg))
        return False


def get_user_posts_by_name(req, username):
    """
    Return user posts by name
    :param username:
    :return: list
    """
    all_users = req.get_all_users().json()
    user_id = [x['id'] for x in all_users if x['username'] == username][0]

    all_posts = req.get_all_posts().json()

    user_posts = [x['id'] for x in all_posts if x['userId'] == user_id]
    return user_posts


@fixture
def req(host):
    """
    Create host instance
    :param host:
    :return:
    """
    return BlogAPI(host)
