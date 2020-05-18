# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def sum_to_k(input_list, k):
    # set does not keep repeated elements so more efficient search
    list_items = set()

    # one traversal through list, if given num - list at index from list is equal to item 
    # in set then sum must exist
    for i in input_list:
        if k - i in list_items:
            return True

        list_items.add(i)
    
    return False