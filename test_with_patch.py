from example_patch import GitHubUser
import mock
import pytest


@pytest.fixture
def user():
    return GitHubUser('sigmavirus24')

def test_user_short_info(user):
    info = ''
    with mock.patch.object(user, 'fetch') as fetch:
        fetch.return_value = {
            'login': 'sigmavirus24',
            'name': 'Ian',
            'html_url': 'https://github.com/sigmavirus24'
        }
        info = user.short_info()
        assert fetch.called is True

    assert 'sigmavirus24' in info
    assert 'Ian' in info
    assert 'https://github.com/sigmavirus24' in info
