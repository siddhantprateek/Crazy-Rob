"""
Given a valid (IPv4) IP address, return a defanged(rendered harmless or ineffectual) version of that IP address.
A defanged IP address replaces every period "." with "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
"""


class Solution:
    def defangIPaddr(self, address: str):
        self.address = address
        self.address = self.address.replace(".", "[.]")

        return print(self.address)


ret = Solution().defangIPaddr("1.1.1.1")
