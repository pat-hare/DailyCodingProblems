from collections import defaultdict
# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.

# basic answer, meets use cases  of '', 1, 11, 111 - runtime of O(n)
def decoder(message):
    split_message = list(message)
    count = 0

    if len(message) == 0:
        return 1

    for index, i in enumerate(split_message):
        if index != 0:
            if int(split_message[index-1] + i) <= 26:
                count += 1
        else:
            count += 1
    
    print(count)

# given answer - runtime of O(n)
def num_encodings(s):
    # On lookup, this hashmap returns a default value of 0 if the key doesn't exist
    # cache[i] gives us # of ways to encode the substring s[i:]
    cache = defaultdict(int)
    cache[len(s)] = 1 # Empty string is 1 valid encoding

    for i in reversed(range(len(s))):
        if s[i].startswith('0'):
            cache[i] = 0
        elif i == len(s) - 1:
            cache[i] = 1
        else:
            if int(s[i:i + 2]) <= 26:
                cache[i] = cache[i + 2]
            cache[i] += cache[i + 1]
    return cache[0]