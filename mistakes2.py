defletterToIndex(letter):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    idx = alphabet.find(letter)
    if idx == -1:       # Means it wasnt in the alphabet
        print("error", letter, "is not in the alphabet")
    return idx

def indexToLetter(idx):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    letter = ''
    if idx >= len(alphabet):
        print("error", idx, "is to large")
    elif idx < 0:
        print("error", idx, "is to small")
    else:
        letter = alphabet[idx]
    return letter


from mistakes2 import *
print(letterToIndex('a'))

print(indexToLetter(44))

this_is_a_secret_meassage_that_i_want_to_transmit


ti_s_a_sce_masg_ta__at_rnmt
hs_i__ert_esse_ht_i_wn_t_tasi