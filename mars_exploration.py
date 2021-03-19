# Mars Exploration
# A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.
# Letters in some of the SOS messages are altered by cosmic radiation during transmission.
# Given the signal received by Earth as a string,s , determine
# how many letters of the SOS message have been changed by radiation.


def mars_exploration(s):

    count = 0

    for i in range(len(s)):
        if s[i] != "SOS"[i%3]:
            count += 1
    return count


s = input()
result = mars_exploration(s)
print(result)