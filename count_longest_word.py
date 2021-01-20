# ask the user to type
# in 10 words using a loop, prompting the user for
# each word with a number. The program then
# should display the longest word

count = 1
largest_word = ''                                          # define a variable that is empty first
for i in range(10):                                        # 10 words
    word = input(f"please enter word number {count}:")     # input 10 words
    count += 1
    if len(word) > len(largest_word):                      # first it compares a first word to an empty string and said
        largest_word = word                                # it is the largest then each time compare to the privous word
print("The largest word is: ", largest_word)               # print the largest

