#!/usr/bin/env python
# HW04_ex08_11

# The following functions are all intended to check whether a string contains 
# any lowercase letters, but at least some of them are wrong. For each function, 
# describe what the function actually does (assuming that the parameter is a
# string).

# Do not merely paste the output as a counterexample into the documentation 
# string, explain what is wrong.

################################################################################
# Body

def any_lowercase1(s):
    """The code only accesses the first index (ie 0) and exits before getting
    to the rest of the items
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False




def any_lowercase2(s):
    """The function checks to see if the character 'c' is lowercase... which it always is
    except on string length 0 (which is None)
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    """ variable flag only refers to the last index
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """ looks good
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """ this proves if all characters are lower case
    """
    for c in s:
        if not c.islower():
            return False
    return True


################################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong, 
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print(any_lowercase1("Hello"))
    print(any_lowercase2("HELLO"))
    print(any_lowercase3("hellO"))
    print(any_lowercase4(""))
    print(any_lowercase5("Hello"))
    

if __name__ == '__main__':
    main()