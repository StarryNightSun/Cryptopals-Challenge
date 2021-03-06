import binascii

# Most frequency characters in English
char_freq_array = {'e': 12.02, ' ': 10, 't': 9.10, 'a': 8.12, 'o': 7.68,
                   'i': 7.31, 'n': 6.95, 's': 6.28, 'r': 6.02, 'h': 5.92,
                   'd': 4.32, 'l': 3.98, 'u': 2.88, 'c': 2.71, }


# Scores the coded or decoded message based on number of frequent characters
def score_val(key, code, message, ismessage):
    score = 0

    if ismessage:
        possible_message = message
    else:
        possible_message = [chr(x ^ key) for x in code]

    for char in possible_message:
        val = char_freq_array.get(char)
        if val is not None:
            score += val
    return score


# Single byte xor cipher break, returns (message,key)
def single_byte_xor_cipher(s):
    code = binascii.unhexlify(s)
    savekey = ''
    top_score = 0

    # Loops through every possible character as key and finds the highest score
    for key in range(256):
        curr_score = score_val(key, code, '', False)
        if top_score < curr_score:
            savekey = key
            top_score = curr_score

    # XOR operation
    message = ''.join(chr(x ^ savekey) for x in code)

    return message, savekey


def main():
    input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    print(single_byte_xor_cipher(input)[0])
    assert ("Cooking MC's like a pound of bacon" == single_byte_xor_cipher(input)[0])
