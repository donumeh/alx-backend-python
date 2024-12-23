#!/usr/bin/env python3

"""
Test Client file
"""

from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """
    Test the GithubOrgClient
    """

    @parameterized.expand([("google",), ("abc",)])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """
        Test the org method in the GithubClient Class
        """

        mock_get_json.return_value = {"login": org_name}
        client = GithubOrgClient(org_name)

        result = client.org

        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name)
        )
        self.assertEqual(result, {"login": org_name})

    """
    memoize turns methods into properties. Read up on how to mock a property (see resource).

Implement the test_public_repos_url method to unit-test GithubOrgClient._public_repos_url.

Use patch as a context manager to patch GithubOrgClient.org and make it return a known payload.

Test that the result of _public_repos_url is the expected one based on the mocked payload
    """

    def test_public_repos_url(self):
        """
        Test the public_repos_url returns a payload
        """

        mock_payload = {"repos_url": "https://api.github.com/orgs/google/repos"}


        with patch("client.GithubOrgClient.org", new_callable=PropertyMock) as mock_org:

            mock_org.return_value = mock_payload

            client = GithubOrgClient('google')

            repo_url = client._public_repos_url

            mock_org.assert_called_once()

            self.assertEqual(repo_url, mock_payload['repos_url'])
