# Harold is a kidnapper who wrote a ransom note, but now he is worried
# it will be traced back to him through his handwriting. He found a
# magazine and wants to know if he can cut out whole words from it
# and use them to create an untraceable replica of his ransom note.
# The words in his note are case-sensitive and he must use only whole
# words available in the magazine. He cannot use substrings or concatenation to create the words he needs.
# Given the words in the magazine and the words in the ransom note, print
# Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.
# The first line contains two space-separated integers, m and n,
# the numbers of words in the magazine and the note, respectively.


def check_magazine(magazine, note):

    note_dict = {}
    magazine_dict = {}
    for i in magazine:
        if i in magazine_dict:
            magazine_dict[i] += 1
        else:
            magazine_dict[i] = 1

    for j in note:
        if j in note_dict:
            note_dict[j] += 1
        else:
            note_dict[j] = 1
    li = []
    for key_j, val_j in note_dict.items():
        if key_j not in magazine_dict:
            li.append('No')
        else:
            if note_dict[key_j] > magazine_dict[key_j]:
                li.append('No')
            else:
                li.append('Yes')
    if 'No' in li:
        print('No')
    else:
        print('Yes')


magazine_words = input().rstrip().split()
note_words = input().rstrip().split()
check_magazine(magazine_words, note_words)
