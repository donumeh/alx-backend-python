#!/usr/bin/env python3

"""
Test Client file
"""

from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch


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
