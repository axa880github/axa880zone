import unittest
from ddt import ddt, data
import syntax_validator

@ddt
class test_syntax_validator(unittest.TestCase):

# User name test cases
    @data("Abcdefg1", "Abcdefg12", "Abcdefg123", "Abcdefg1234", "Abcdefg12345", "Z1234567890a", "A1b2c3d4e5d6")
    def test_is_valid_username_returns_true_given_valid_input_within_the_range(self, username):
        self.assertTrue(syntax_validator.is_valid_username(username))

    @data("", "A", "A1", "A12", "A123", "A1234", "B12345", "C123456", "Z123456789000", "O0000000000000")
    def test_is_valid_username_returns_false_given_invalid_input_outside_the_range(self, username):
        self.assertFalse(syntax_validator.is_valid_username(username))

    @data("Hbcdefg1", "O00000000", "Xb8defg123", "Ubcde9g1s34", "Sb0defg12345", "M1234t678j0a", "V1b2c3d4e5d6")
    def test_is_valid_username_returns_true_given_valid_input_contains_alpha_numeric(self, username):
        self.assertTrue(syntax_validator.is_valid_username(username))

# These tests can be expanded to many more combinations, but I just stopped here.
    @data("", "!", "$1", "A@", "A%23", "A1(34", "B12*45", "________", "++++++", ">", "123_abc", "|||||||||", "^", "%i)")
    def test_is_valid_username_returns_false_given_invalid_input_contains_non_alpha_numeric(self, username):
        self.assertFalse(syntax_validator.is_valid_username(username))

    @data("Abcdefg1", "Abcdefg12", "Abcdefg123", "Abcdefg1234", "A12345bcdefg", "O12345678900")
    def test_is_valid_username_returns_true_given_valid_input_contains_1_or_more_digit(self, username):
        self.assertTrue(syntax_validator.is_valid_username(username))

# BUG FOUND - All of these tests should pass as negaive tests, but they are failing.
# The code is failing to find out that there is not a single digit in the user names. 
    @data("Aaaaaaaa", "Abasdfghj", "Addddddddd", "Akjhgfdefgh", "Abcdefghijkl")
    def test_is_valid_username_returns_false_given_invalid_input_contains_no_digit(self, username):
        self.assertFalse(syntax_validator.is_valid_username(username))

    @data("Abcdefg1", "Abcdefg12", "Abcdefg123", "Abcdefg1234", "Abcdefg12345", "Z1234567890a", "A1b2c3d4e5d6")
    def test_is_valid_username_returns_true_given_valid_input_starts_with_capital_letter(self, username):
        self.assertTrue(syntax_validator.is_valid_username(username))

    @data("abcdefg1", "bbcdefg12", "cbcdefg123", "dbcdefg1234", "obcdefg12345")
    def test_is_valid_username_returns_false_given_invalid_input_starts_with_no_capital_letter(self, username):
        self.assertFalse(syntax_validator.is_valid_username(username))

# ZIP code test cases
    @data("12345", "13579", "55555", "00000", "01230", "98765", "99999")
    def test_is_valid_us_zip_code_returns_true_given_valid_input_contains_only_5digit(self, zipcode):
        self.assertTrue(syntax_validator.is_valid_us_zip_code(zipcode))

    @data("", "1", "13", "555", "0000", "101230", "987658888", "NotMyZip", "-1234", "%^&*(")
    def test_is_valid_us_zip_code_returns_false_given_invalid_input_contains_non_5digit(self, zipcode):
        self.assertFalse(syntax_validator.is_valid_us_zip_code(zipcode))

    @data("12345-6789", "13579-2468", "55555-5555", "00000-0000", "01230-4500", "98765-4321", "99999-9999")
    def test_is_valid_us_zip_code_returns_true_given_valid_input_contains_5digit_4digit(self, zipcode):
        self.assertTrue(syntax_validator.is_valid_us_zip_code(zipcode))

    @data("-", "1-1", "1_3", "555-555", "0o00000-0000000", "10123-12345", "98765-*888", "NotMyzip", "-1234", "%^&*-&*")
    def test_is_valid_us_zip_code_returns_false_given_invalid_input_contains_non_5digit_4digit(self, zipcode):
        self.assertFalse(syntax_validator.is_valid_us_zip_code(zipcode))

# End of File - Out of total 95 tests, 5 tests are failing for a bug - Ashfaque Ahammad

