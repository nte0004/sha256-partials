from hashlib import sha256
import string
from itertools import product
from base64 import b64encode
import sys

input_prefix  = 'nte0004@auburn.edu'
target_partial = '6e746500'         #'6e746500' is the Hex encoding of nte0x00

char_set =  string.ascii_letters + string.digits + string.punctuation
max_length = 8
partial_matches = []

for length in range(1, max_length + 1):
    # chars is one set of the iterable containing all possible combinations of the char_set
    # length represents the number of times a character from char_set is in a combination.
    
    for chars in product(char_set, repeat=length):
        input_str = input_prefix + ''.join(chars)
        input_str_utf8 = input_str.encode('utf-8')
        digest = sha256(input_str_utf8).hexdigest() 
    
        if digest.startswith(target_partial):
            input_b64 = b64encode(input_str_utf8).decode()
            partial_matches.append((input_b64))
    
            if len(partial_matches) == 2:
                print(partial_matches[0] + '\n')
                print(partial_matches[1] + '\n')
                sys.exit(0)

sys.exit(0)
