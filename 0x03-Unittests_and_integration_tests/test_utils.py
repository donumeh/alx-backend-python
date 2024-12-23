#!/usr/bin/env python3

"""
Unittest for access_nested_map
"""
from parameterized import parameterized
from typing import Mapping, Tuple, Any
import utils
from utils import memoize
import unittest
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for Access Nested Map
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Mapping, path: Tuple, result: Any
    ) -> None:
        """
        Test the access_nested_map function for correct output
        """
        self.assertEqual(utils.access_nested_map(nested_map, path), result)

    @parameterized.expand([({}, ("a",), "a"), ({"a": 1}, ("a", "b"), "b")])
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: Tuple, error_msg: str
    ) -> None:
        """
        Test the access nested map for error raises
        """

        with self.assertRaises(KeyError, msg=error_msg):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test Case for get json function in utils
    """

    @patch("utils.requests.get")
    def test_get_json(self, mock_get):
        """
        Define a test case to test utils.get_json
        """

        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]

        for test_url, test_payload in test_cases:

            # mock_response = Mock()
            # mock_response.json.return_value = test_payload
            mock_get.return_value.json.return_value = test_payload

            result = utils.get_json(test_url)

            mock_get.assert_called_once_with(test_url)

            self.assertEqual(result, test_payload)

            mock_get.reset_mock()


class TestMemoize(unittest.TestCase):
    """
    Test case for memoization function
    """

    def test_memoize(self):
        """
        Tests the meoize function
        """

        class TestClass:
            """
            Test Class
            """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = TestClass()

        with patch.object(
                TestClass, "a_method", return_value=42
                ) as mocked_method:

            result1 = test_instance.a_property
            result2 = test_instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mocked_method.assert_called_once()
