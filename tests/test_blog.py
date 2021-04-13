from pytest import mark
from tests.conftest import check_email_format, get_user_posts_by_name
from assertpy import assert_that

from tests.support.assertions import assert_valid_schema

@mark.parametrize('username', ['Delphine'])
def test_emails_correctness_for_posts_comments_of_the_user(req, username):
    """
    Get all users
    Find the user with specific name
    Find all post of the user
    Get all comments for the user posts
    Test email correctness
    :param req:
    :param username:
    :return:
    """

    user_posts = get_user_posts_by_name(req, username)  # get all user posts by user name

    comments_emails = []
    for post in user_posts:
        comments_by_post_id = req.get_post_comments(post).json()  # Get all comments for the all each post
        [comments_emails.append(x['email']) for x in comments_by_post_id]  # Save all emails to the list
        # comments_emails = [x['email'] for x in comments_by_post_id]

    for email in comments_emails:
        assert check_email_format(email)  # Assert that all emails are in the allowed format


@mark.parametrize('username', ['Delphine', 'Moriah.Stanton'])
def test_emails_correctness_by_the_user_post_from_all_comments(req, username):
    """
    Get all users
    Find the user with specific name
    Find all post of the user
    Get all comments from the comment GET call
    Test email correctness
    :param req:
    :param username:
    :return:
    """

    user_posts = get_user_posts_by_name(req, username)  # get all user posts by user name

    comments_emails = []
    for post in user_posts:
        comments_by_post_id = req.get_comments_by_parameter(postId=str(post)).json()
        # Get all comments for the each post
        [comments_emails.append(x['email']) for x in comments_by_post_id]  # Save all emails to the list
        # comments_emails = [x['email'] for x in comments_by_post_id]

    for email in comments_emails:
        assert check_email_format(email)  # Assert that all emails are in the allowed format


@mark.parametrize('username', ['Delphine'])
def test_compare_comment_emails(req, username):
    """
    Compare user emails for the comment from different api methods
    :param req:
    :param username:
    :return:
    """
    user_posts = get_user_posts_by_name(req, username)  # get all user posts by user name

    comments_emails = []
    for post in user_posts:
        comments_by_post_id = req.get_post_comments(post).json()  # Get all comments for the all each post
        [comments_emails.append(x['email']) for x in comments_by_post_id]  # Save all emails to the list
        # comments_emails = [x['email'] for x in comments_by_post_id]

    comments_emails_from_all_comments = []
    for post in user_posts:
        comments_by_post_id = req.get_comments_by_parameter(postId=str(post)).json()
        # Get all comments for the each post
        [comments_emails_from_all_comments.append(x['email']) for x in comments_by_post_id]  # Save all
        # emails to the list
        # comments_emails = [x['email'] for x in comments_by_post_id]

    assert_that(comments_emails).is_equal_to(comments_emails_from_all_comments)  # compare API returning
    # the same data from the different API cals


@mark.parametrize('username', ['Delphine', 'Bret'])
def test_get_users(req, username):
    """
    Get username and validate JSON schema
    :param req:
    :param username:
    :return:
    """
    all_users = req.get_all_users().json()
    user_id = [x['id'] for x in all_users if x['username'] == username][0]
    r = req.get_user_by_id(user_id)
    assert_that(r.status_code).is_equal_to(200)
    assert_valid_schema(r.json(), '{}.json'.format(username))
