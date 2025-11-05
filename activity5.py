#words_file = open('CROSSWD.txt', 'r')  ##r = read

##print(words_file.readline()) //reads one line in .txt
##use .strip() to take unnecessary formatting || things out

# #for k in dir(words_file):  ##dir() = directory of methods
#     #if '__' not in k:
#        print(k)

##print((x for x in dir(words_file) if 'read' != x[0])) 
##list comprehension : what are u selecting? where are you selecting ur vals? Give lists that satisfy values

def more_than_20(file):
    words_file = open(file, 'r')
    words_list = []

    for i in words_file:
        curr_word = i.strip()
        if len(curr_word) > 20:
            words_list.append(curr_word)
    
    return words_list


def has_no_e(word):

    #iterates through String to find 'e', therefore result is false. If there is no 'e', skip letter and unchange result, so return value will default to True
    # for i in word: 
    #     if i == 'e':
    #         return False
    
    # return True

    return 'e' not in word
            
        
def uses_only(word,letters):
#no need to create a seperate variable to return
    for curr_letter in word:
        #  print(curr_letter) #a check for what is being iterated thru
        if curr_letter not in letters:
            return False

    return True        


def all_uses_only(file, letters):
    #open file
    words_file = open(file, 'r')
    words_list = []

    for word in words_file:
        current_word = word.strip()
        
        if uses_only(current_word, letters):
            words_list.append(word.strip())
    
    return words_list

# print(more_than_20('CROSSWD.txt'))
# has_no_e('allegory')
# print(uses_only('Alex', 'Alexas')) #true
# print(uses_only('abra', 'abr')) #false

print(all_uses_only('CROSSWD.txt', 'abrz'))