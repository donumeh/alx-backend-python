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
        Test the access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), result)
