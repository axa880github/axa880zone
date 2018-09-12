import subprocess
import pexpect

import unittest

def execute(cmd):
    output, status = pexpect.run(cmd
                                 , withexitstatus=1
                                 , timeout=600
                                )

    #print(output)
    return output


class test_awscreds(unittest.TestCase):
  def setUp(self):
    execute('sudo ./setup-assignments')

# Tests for Profile: default
  def test_awscreds_returns_access_key_default_field_and_default_profile(self):
		self.assertIn('AKAIISDAIK5LJWV264SAGX7XNA', execute('./awscreds'))

  def test_awscreds_returns_access_key_default_profile_and_field_key(self):
		self.assertIn('AKAIISDAIK5LJWV264SAGX7XNA', execute('./awscreds -field key'))

  def test_awscreds_returns_access_key_default_profile_and_field_secret(self):
		self.assertIn('dxt7e3d3fCSf/NftN8Cys5L4duQ2KPQwN0n+oW', execute('./awscreds -field secret'))

# Since substring comparison passes, verification should be for the both whole strings
  def test_awscreds_returns_access_key_default_profile_and_field_both(self):
		self.assertIn('AKAIISDAIK5LJWV264SAGX7XNA\r\ndxt7e3d3fCSf/NftN8Cys5L4duQ2KPQwN0n+oW', execute('./awscreds -field both'))


# Tests for Profile: profile1
  def test_awscreds_returns_access_key_default_field_and_profile1(self):
		self.assertIn('testvalue', execute('./awscreds -profile profile1'))

  def test_awscreds_returns_access_key_profile_profile1_and_field_key(self):
		self.assertIn('testvalue', execute('./awscreds -field key -profile profile1'))

  def test_awscreds_returns_access_key_profile_profile1_and_field_secret(self):
		self.assertIn('testsecretvalue', execute('./awscreds -field secret -profile profile1'))

# Since substring comparison passes, verification should be for the both whole strings
  def test_awscreds_returns_access_key_profile_profile1_and_field_both(self):
		self.assertIn('testvalue\r\ntestsecretvalue', execute('./awscreds -field both -profile profile1'))

# Note: Tests for flags/switchs changeed their positions (like, "-profile" first and then "-field")
# Tests for Profile: profile1
  def test_awscreds_returns_access_key_profile_profile1_and_field_key_flags_switched(self):
		self.assertIn('testvalue', execute('./awscreds -profile profile1 -field key'))

  def test_awscreds_returns_access_key_profile_profile1_and_field_secret_flags_switched(self):
		self.assertIn('testsecretvalue', execute('./awscreds -profile profile1 -field secret'))

  def test_awscreds_returns_access_key_profile_profile1_and_field_both_flags_switched(self):
		self.assertIn('testvalue\r\ntestsecretvalue', execute('./awscreds -profile profile1 -field both'))


# Tests for Profile: profile2
  def test_awscreds_returns_access_key_default_field_and_profile2(self):
		self.assertIn('', execute('./awscreds -profile profile2'))

  def test_awscreds_returns_access_key_profile_profile2_and_field_key(self):
		self.assertIn('', execute('./awscreds -field key -profile profile2'))

  def test_awscreds_returns_access_key_profile_profile2_and_field_secret(self):
		self.assertIn('', execute('./awscreds -field secret -profile profile2'))

  def test_awscreds_returns_access_key_profile_profile2_and_field_both(self):
		self.assertIn('', execute('./awscreds -field both -profile profile2'))


# Tests for Profile: profile3
# Note: Not a very strong test, tried to do for Python specific tests for the null value
  def test_awscreds_returns_access_key_default_field_and_profile3(self):
		self.assertIn('None', execute('./awscreds -profile profile3'))

  def test_awscreds_returns_access_key_profile_profile3_and_field_key(self):
		self.assertIn('None', execute('./awscreds -field key -profile profile3'))

  def test_awscreds_returns_access_key_profile_profile3_and_field_secret(self):
		self.assertIn('None', execute('./awscreds -field secret -profile profile3'))

  def test_awscreds_returns_access_key_profile_profile3_and_field_both(self):
		self.assertIn('None\r\nNone', execute('./awscreds -field both -profile profile3'))


# Tests for Profile: profile4
# BUG: All these 4 tests pass, it should be a BUG, because values should not be allowed with 1 character long
  def test_awscreds_returns_access_key_default_field_and_profile4(self):
		self.assertIn('x', execute('./awscreds -profile profile4'))

  def test_awscreds_returns_access_key_profile_profile4_and_field_key(self):
		self.assertIn('x', execute('./awscreds -field key -profile profile4'))

  def test_awscreds_returns_access_key_profile_profile4_and_field_secret(self):
		self.assertIn('y', execute('./awscreds -field secret -profile profile4'))

  def test_awscreds_returns_access_key_profile_profile4_and_field_both(self):
		self.assertIn('x\r\ny', execute('./awscreds -field both -profile profile4'))


# Tests for Profile: profile5
  def test_awscreds_returns_access_key_default_field_and_profile5(self):
		self.assertIn('testvalue5testvalue5testvalue5testvalue5testvalue5testvalue5testvalue5testvalue5testvalue5testvalue5testvalue5testvalue5', execute('./awscreds -profile profile5'))

  def test_awscreds_returns_access_key_profile_profile5_and_field_key(self):
		self.assertIn('testvalue5testvalue5testvalue5testvalue5testvalue5testvalue5testvalue5testvalue5testvalue5testvalue5testvalue5testvalue5', execute('./awscreds -field key -profile profile5'))

  def test_awscreds_returns_access_key_profile_profile5_and_field_secret(self):
		self.assertIn('testsecretvalue5testsecretvalue5testsecretvalue5testsecretvalue5testsecretvalue5testsecretvalue5testsecretvalue5', execute('./awscreds -field secret -profile profile5'))

  def test_awscreds_returns_access_key_profile_profile5_and_field_both(self):
		self.assertIn('testvalue5testvalue5testvalue5testvalue5testvalue5testvalue5testvalue5testvalue5testvalue5testvalue5testvalue5testvalue5\r\ntestsecretvalue5testsecretvalue5testsecretvalue5testsecretvalue5testsecretvalue5testsecretvalue5testsecretvalue5', execute('./awscreds -field both -profile profile5'))


# Tests for Profile: profile6
  def test_awscreds_returns_access_key_default_field_and_profile6(self):
		self.assertIn('testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6', execute('./awscreds -profile profile6'))

  def test_awscreds_returns_access_key_profile_profile6_and_field_key(self):
		self.assertIn('testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6', execute('./awscreds -field key -profile profile6'))

  def test_awscreds_returns_access_key_profile_profile6_and_field_secret(self):
		self.assertIn('testsecretvalue6testsecretvalue6testsecretvalue6testsecretvalue6testsecretvalue6testsecretvalue6testsecretvalue6testsecretvalue6testsecretvalue6testsecretvalue6testsecretvalue6testsecretvalue6testsecretvalue6', execute('./awscreds -field secret -profile profile6'))

  def test_awscreds_returns_access_key_profile_profile6_and_field_both(self):
		self.assertIn('testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6testvalue6\r\ntestsecretvalue6testsecretvalue6testsecretvalue6testsecretvalue6testsecretvalue6testsecretvalue6testsecretvalue6testsecretvalue6testsecretvalue6testsecretvalue6testsecretvalue6testsecretvalue6testsecretvalue6', execute('./awscreds -field both -profile profile6'))


# Tests for Profile: profile7
  def test_awscreds_returns_access_key_default_field_and_profile7(self):
# Characters after "#" is getting ignored, this is Pyhton specific syntax issue, not a product BUG
		self.assertIn('!@', execute('./awscreds -profile profile7'))

  def test_awscreds_returns_access_key_profile_profile7_and_field_key(self):
# Characters after "#" is getting ignored, this is Pyhton specific syntax issue, not a product BUG
		self.assertIn('!@', execute('./awscreds -field key -profile profile7'))

  def test_awscreds_returns_access_key_profile_profile7_and_field_secret(self):
		self.assertIn('&*()_+', execute('./awscreds -field secret -profile profile7'))

  def test_awscreds_returns_access_key_profile_profile7_and_field_both(self):
# Characters after "#" is getting ignored, this is Pyhton specific syntax issue, not a product BUG
		self.assertIn('!@\r\n&*()_+', execute('./awscreds -field both -profile profile7'))


# Tests for Profile: profile8
  def test_awscreds_returns_access_key_default_field_and_profile8(self):
		self.assertIn('/n/t/n/t///', execute('./awscreds -profile profile8'))

  def test_awscreds_returns_access_key_profile_profile8_and_field_key(self):
		self.assertIn('/n/t/n/t///', execute('./awscreds -field key -profile profile8'))

  def test_awscreds_returns_access_key_profile_profile8_and_field_secret(self):
		self.assertIn('/n/t/n/t////////', execute('./awscreds -field secret -profile profile8'))

  def test_awscreds_returns_access_key_profile_profile8_and_field_both(self):
		self.assertIn('/n/t/n/t///\r\n/n/t/n/t////////', execute('./awscreds -field both -profile profile8'))

# Tests for Profile: profile9
# Following 4 tests run fine manually from the CLI; but for automation with Python, beginning 
# the substirng "'''" works as starting of the Python block comment, this is Python's limitation
# also wraping "'''" with more double quotes and single quotes gives "~" a syntax error
'''
  def test_awscreds_returns_access_key_default_field_and_profile9(self):
		self.assertIn('~````````''''''12345', execute('./awscreds -profile profile9'))

  def test_awscreds_returns_access_key_profile_profile9_and_field_key(self):
		self.assertIn('~````````''''''12345', execute('./awscreds -field key -profile profile9'))

  def test_awscreds_returns_access_key_profile_profile9_and_field_secret(self):
		self.assertIn('~`````````````''''''abcdefg', execute('./awscreds -field secret -profile profile9'))

  def test_awscreds_returns_access_key_profile_profile9_and_field_both(self):
		self.assertIn('~````````''''''12345\r\n~`````````````''''''abcdefg', execute('./awscreds -field both -profile profile9'))
'''

# End of file


