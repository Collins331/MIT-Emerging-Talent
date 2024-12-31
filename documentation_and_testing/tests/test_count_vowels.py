#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Test module for count_vowels function
Contains intentionally buggy codes for debugging practice

Test Categories:
    - Standard test: typical strings with varying vowels
    - Edge case test: empty string and single characters
    - Error case test: non-string inputs and non-ASCII characters
    
Created on 2024-12-31
@author: Collins Ochieng
"""

import unittest
from ..count_vowels import count_vowels

class TestCountVowels(unittest.TestCase):
    """Test suite for count_vowels and also has bugs"""
    def test_with_many_vowels(self):
        """Test with a string containing many vowels"""
        self.assertEqual(count_vowels("queue"), 4)
        
    def test_long_string(self):
        """Test with a long string containing many vowels"""
        self.assertEqual(count_vowels("lincsoftwares"), 4)
    
    def test_single_string(self):
        """Test with a single character string"""
        self.assertEqual(count_vowels("a"), 1)
    
    def test_empty_string(self):
        """Test with an empty string"""
        self.assertEqual(count_vowels(""), 0)
    
    def test_with_integer(self):
        """Test with an integer input"""
        with self.assertRaises(AssertionError):
            count_vowels(123)
            
            
if __name__ == "__main__":
    unittest.main()
