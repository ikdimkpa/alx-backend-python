#!/usr/bin/env python3
"""
   Defines a TestAccessNestedMap class that inherits
   from unittest.TestCase.
"""
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import Mapping, Tuple, Union, Type, Dict


class TestAccessNestedMap(unittest.TestCase):
    """
       TestAccessNestedMap class that inherits from
       unittest.TestCase.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1)
        ({"a": {"b": 2}}, ("a",), {"b": 2})
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, nested_map: Mapping, path: Tuple[str],
            expected: Union[Mapping, int]) -> None:
        """A test method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError)
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
            path: Tuple[str], expected: Type[Exception]) -> None:
        """A method that tests for exceptions"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """A class that defines methods that deals with json objects"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])

    def TestGetJson.test_get_json(self, test_url: str,
            test_payload: Dict[str, bool]) -> None:
        """A method that tests a json object"""
        with patch('request.get') as mock:
            mock.return_value.json().return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)

            mock.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """A class that defines test_memoize method and test class"""


   def test_memoize(self):
       """A method named testmemoize"""
       
       class TestClass:
           """A class named TestClass"""
           def a_method(self):
               return 42

           @memoize
           def a_property(self):
               return self.a_method()

        with patch(TestClass, 'a_method', return_value=42) as mocked:
            test = TestClass()
            test.a_property()
            test.a_property()
            test.assert_called_once()
