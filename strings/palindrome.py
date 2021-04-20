def is_palin(s : str ) -> bool :
    '''
    :param s:
    :return:
    '''
    if s :
        i,j = 0 , len(s) -1
        while i <= j:
            print((s[i],s[j]))
            if s[i] != s[j]:
                return False
            i +=1
            j -=1
        return True

inputs = ["a","ab","aa","aba","hello","malayalam"]
for i in inputs :
    print("{} is Palindrome".format(i) if is_palin(i) else "{} is not palindarome".format(i))