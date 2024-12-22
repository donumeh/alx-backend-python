#!/usr/bin/env python3

"""
Unittest for access_nested_map
"""
from parameterized import parameterized
from typing import Mapping, Tuple, Any
from utils import access_nested_map
import unittest


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
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([({}, ("a",), "a"), ({"a": 1}, ("a", "b"), "b")])
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: Tuple, error_msg: str
    ) -> None:
        """
        Test the access nested map for error raises
        """

        with self.assertRaises(KeyError, msg=error_msg):
            access_nested_map(nested_map, path)
