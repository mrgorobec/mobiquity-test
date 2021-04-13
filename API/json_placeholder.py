import requests


class BlogAPI(object):
    """Blog REST API to manage comments
    https://jsonplaceholder.typicode.com/guide/
    """

    def __init__(self, host):
        """
        :param host - url stage/prod
        """
        self.url = host

    def get_all_users(self):
        """
        Get list of the users
        """
        return requests.get(self.url + 'users')

    def get_user_by_id(self, id):
        """
        Get the user by ID
        :param id:
        :return: json
        """
        return requests.get(self.url + 'users/{}'.format(id))

    def get_all_posts(self):
        """
        Get all posts
        :return: all posts
        """
        return requests.get(self.url + 'posts')

    def get_post_by_id(self, id):
        """Get post by ID
        :param id - post
        :return json
        """
        return requests.get(self.url + 'posts/{}'.format(id))

    def get_post_comments(self, id):
        """
        Get post comments by post ID
        :param id- post
        :return json
        """
        return requests.get(self.url + 'posts/{}/comments'.format(id))

    def get_comments_by_parameter(self, **kwargs):
        """
        Get post comments by post ID
        :param kwargs:
        :return: comments
        """

        return requests.get(self.url + 'comments', params=kwargs)

    def create_post(self, **kwargs):
        """
        Create new blog post
        :param kwargs:
        :return: post details
        """

        return requests.post(self.url + 'posts', json=kwargs)

    def fully_update_post(self, id, **kwargs):
        """
        Fully UPDATE blog post
        :param id:
        :param kwargs:
        :return: updated post details
        """

        return requests.put(self.url + 'posts/{}'.format(id), json=kwargs)

    def partial_update_post(self, id, **kwargs):
        """
        Partial update blog post
        :param id:
        :param kwargs:
        :return: updated post details
        """

        return requests.patch(self.url + 'posts/{}'.format(id), json=kwargs)

    def delete_post(self, id):
        """
        DELETE blog post
        :param id:
        :return: status code
        """

        return requests.patch(self.url + 'posts/{}'.format(id))
