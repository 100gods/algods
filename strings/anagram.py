def check_anagram(str_one : str , str_two : str) -> bool:
    '''
    Check if two strings are anagram
    :param str_one:
    :param str_two:
    :return:
    '''
    if len(str_one) == len(str_two):
        no_of_char = 2**8
        counter_array = [0 for i in range(no_of_char)]
        for i in range(len(str_one)):
            counter_array[ord(str_one[i])] +=1
            counter_array[ord(str_two[i])] -=1
        for i in counter_array:
            if i != 0 :
                return False
        return True
    else:
        return False


print("anagram" if check_anagram("cat","act") else "not anagram")