from pytest import fixture

HOST_STAGING = 'https://jsonplaceholder.typicode.com/'
HOST_PROD = 'https://jsonplaceholder.typicode.com/'


def pytest_addoption(parser):
    """Declaring the command-line options for test run"""
    parser.addoption('--host',
                     default='staging',
                     help='host options: "staging", "production", or your own host for local testing')


@fixture(autouse=True)
def host(request):
    """Return the target host
    :param request:
    :return:
    """
    # get host value
    cli_value = request.config.getoption('--host')

    if cli_value == '' or cli_value == 'staging':
        domain = HOST_STAGING
    elif cli_value == 'prod':
        domain = HOST_PROD
    else:
        domain = cli_value
    yield domain
