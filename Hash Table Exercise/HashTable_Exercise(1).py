# Kaitlyn Forsberg - uses hash table to store the keywords from MLKSpeech_Keywords(1).txt and
# counts the number of times each word appears in MLKSpeech(1).txt


import sys
import time


def counting_key(filename):
    # open second file to be read
    infile = open(filename, "r")
    line_count = 0
    # potential list of words from file
    file_list = []
    word_count = 0
    # read file, change to lower-case, then split the lines into words and combine
    # the temp_words list with the file_list list
    file_line = infile.readline()
    line_count += 1
    file_line = file_line.lower()
    temp_words = file_line.split()
    file_list.extend(temp_words)
    # number of words = number of words in list from file
    word_count += len(temp_words)
    # loop performs the same action as the lines above until the file is empty
    while file_line != "":
        file_line = infile.readline()
        # ensures that the line above is not counted into line_count
        if file_line == "":
            break
        file_line = file_line.lower()
        temp_words = file_line.split()
        file_list.extend(temp_words)
        word_count += len(temp_words)
        line_count += 1
    infile.close()

    print(f"***** Statistics *****\n"
          f"**********************\n"
          f"Total Lines Read: {line_count}\n"
          f"Total Words Read: {word_count}\n\n"
          f"Break Down by Key Word: \n")
    # list of words from the file returned to the hash_table function
    # so that it can be determined if each word is a keyword
    return file_list


def hash_table(keywords_list, lett):
    g_val = {}
    # g_val has a 0 value for every key
    for letter in lett:
        g_val[letter] = 0

    # fill list with 23 zeros
    hashTable = [0] * len(keywords_list)

    # i is the index of the while loop below
    i = 0
    attempt = 0
    gmax = 11
    while i < len(keywords_list):
        # if the length of the keyword is 1, then the gval of the "last" letter is 0
        tempLast_Gval = g_val[keywords_list[i][0][-1]]
        attempt += 1
        # equation for hash value
        hash_val = (keywords_list[i][2] + g_val[keywords_list[i][0][0]] + tempLast_Gval) % len(keywords_list)
        # if value at index is already 0 then insert keyword and reset attempts
        if hashTable[hash_val] == 0:
            hashTable[hash_val] = keywords_list[i][0]
            i += 1
            attempt = 0
        # if trying to place keyword and an empty spot has not been found, increment the gvalue
        elif attempt < gmax:
            g_val[keywords_list[i][0][0]] += 1
        elif attempt >= gmax:
            # if attempt not successful, reset gvalue to value before attempt (to have 11 total tries at placement)
            # reset attempt to 0 and backtrack to the previous keyword
            # attempt to replace the previous keyword and clear the value in the hash table that the kw was placed at
            # originally. Increment the gvalue so that the keyword is not placed in its previous spot
            g_val[keywords_list[i][0][0]] -= (gmax - 1)
            i -= 1
            attempt = 0
            hashTable[hashTable.index(keywords_list[i][0])] = 0
            g_val[keywords_list[i][0][0]] += 1
    # print(hashTable)
    # file_words holds the words from file #2
    file_words = counting_key(filename2)

    # to determine if words from file #2 are in the hash table, create
    # dictionary with all gvalues for the keywords initialized to 0
    gval_temp = {}
    for temp_letter in lett:
        gval_temp[temp_letter] = 0

    # create dictionary with all letters from the keywords initialized to 0
    values_count = {}
    for key in hashTable:
        values_count[key] = 0

    # runs through each word in the second file to determine if it is contained within the hash table
    for temp_word in file_words:
        first_letter = temp_word[0]
        last_letter = temp_word[-1]
        # variable determines whether the two while loops below need to be exited
        exit1 = 0
        # if statement ensures that the first and last letter of the word are contained within the letters from the kws.
        # while statements go through each gvalue, starting at 0, until the max gvalue for that letter to determine
        # whether or not the word is contained within the keywords.
        if (gval_temp.get(first_letter) is not None) and (gval_temp.get(last_letter) is not None):
            while (gval_temp[last_letter]) < (g_val[last_letter] + 1):
                while (gval_temp[first_letter]) < (g_val[first_letter] + 1):
                    # ind contains a possible index where the word could be found (if the word is contained in kws)
                    ind = (gval_temp[first_letter] + gval_temp[last_letter] + len(temp_word)) % len(hashTable)
                    # if found then increment the count of the word and exit the two while loops to move to next word
                    if temp_word == hashTable[ind]:
                        values_count[temp_word] += 1
                        gval_temp[last_letter] = 0
                        gval_temp[first_letter] = 0
                        exit1 = 1
                        break
                    # increment first and last letter gvalues to determine if the word can be found in the keywords
                    gval_temp[first_letter] += 1
                if exit1 == 1:
                    break
                gval_temp[last_letter] += 1
            # if not found then reset gvalues
            gval_temp[last_letter] = 0
            gval_temp[first_letter] = 0

    # wrd -> keyword from the dictionary
    for wrd in values_count:
        print(values_count[wrd], " : ", wrd)

    val_tot = 0
    for val in values_count:
        val_tot += values_count[val]
    print("\nTotal Key Words in File #2: ", val_tot)


if len(sys.argv) != 3:
    raise ValueError('Please provide two file names.')

sys.argv[0] = sys.argv[0][0:len(sys.argv[0]) - sys.argv[0][::-1].find('/')]

inputFile1 = sys.argv[0] + sys.argv[1]
inputFile2 = sys.argv[0] + sys.argv[2]

print("\nThe files that will be used for input are {0} and {1}\n".format(sys.argv[1], sys.argv[2]))

# strings of file names
filename1 = str(sys.argv[1])
filename2 = str(sys.argv[2])

start = time.time()

# file objects
infile1 = open(filename1, "r")

# creates list of keywords from file #1
line = infile1.readline()
line = line.lower()
temp_keywords = line.split()
keywords = []
index = 0
# gets rid of repetitive words in the line from the file
# words placed into keywords are not placed randomly as they would be if a set was used
for kw in temp_keywords:
    if keywords.count(kw) == 0:
        keywords.append(kw)

# print(f"Unique Keywords: {keywords}\n")
# print(f"Number of Unique Keywords: {len(keywords)}\n")

# dictionary, "letters", holds count of the number of times each letter occurs
# in the keywords as a first or last letter
letters = {}
for word in keywords:
    if word[0] in letters:
        letters[word[0]] += 1
    else:
        letters[word[0]] = 1

    last = word[len(word) - 1]
    if last in letters:
        letters[last] += 1
    else:
        letters[last] = 1

# print(letters, '\n')

temp_list = []
sorted_kws = []
for keyword in keywords:
    # "word_strength" is equal to the count of the first letter added to the count of the last letter in the word
    # counts come from variable "letters" above
    # if the keyword is only one letter, then the word strength is just the count of that one letter
    if len(keyword) > 1:
        word_strength = letters[keyword[0]] + letters[keyword[len(keyword) - 1]]
    else:
        word_strength = letters[keyword[0]]
    temp_list.append(keyword)
    temp_list.append(word_strength)
    temp_list.append(len(keyword))
    # copy used so that the temp_list.clear() did not overwrite sorted_kws
    # sorted_kws is not sorted yet, it gets sorted below
    sorted_kws.append(temp_list.copy())
    temp_list.clear()

infile1.close()

# sorts sorted_kws by the "word_strength" variable
sorted_kws.sort(key=lambda keywrd: keywrd[1], reverse=True)
# print(sorted_kws, '\n')
hash_table(sorted_kws, letters)

end = time.time()

print("\nTotal Time of Program: ", end - start)
