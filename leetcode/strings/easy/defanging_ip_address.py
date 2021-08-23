# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

"""
    INPUTS/OUTPUTS
        address = "1.1.1.1" => 1[.]1[.]1[.]1

    NOTES:
        split string a each '.'
        join string again with '[.]'
        ! split method breaks a string at specified separator and returns a list of strings

"""


def defangIPadr(address):
    print("[.]".join(address.split('.')))
    return "[.]".join(address.split('.'))


defangIPadr("1.1.1.1")

# Time complexity: O(n)
# Space complexity: O(1)
