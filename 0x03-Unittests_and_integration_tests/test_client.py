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

    def test_public_repos_url(self):
        """
        Test the public_repos_url returns a payload
        """

        mock_payload = {
                "repos_url": "https://api.github.com/orgs/google/repos"
        }

        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock
                ) as mock_org:

            mock_org.return_value = mock_payload

            client = GithubOrgClient("google")

            repo_url = client._public_repos_url

            mock_org.assert_called_once()

            self.assertEqual(repo_url, mock_payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock_get):
        """
        Test public repos in GithubOrgClient
        """

        mock_get.return_value = [
            {"name": "repo1", "license": {"key": "MIT"}},
            {"name": "repo2", "license": {"key": "GPL"}},
            {"name": "repo3", "license": {"key": "MIT"}},
        ]
        mock_repo_url = "https://api.github.com/orgs/google/repos"

        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_org:

            mock_org.return_value = mock_repo_url

            client = GithubOrgClient("google")
            repos = client.public_repos(license="MIT")

            mock_get.assert_called_once_with(mock_repo_url)
            mock_org.assert_called_once()

            self.assertEqual(repos, ["repo1", "repo3"])

            repos_again = client.public_repos(license="MIT")
            mock_get.assert_called_once()

            self.assertEqual(repos_again, ["repo1", "repo3"])

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, license_map, value, result):
        """
        Test to run on method has_license
        """

        self.assertEqual(
                GithubOrgClient.has_license(license_map, value),
                result
                )
