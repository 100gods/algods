def minSteps(s: str, t: str) -> int:
    '''
    1347. Minimum Number of Steps to Make Two Strings Anagram
    :param self:
    :param s:
    :param t:
    :return:
    '''
    if len(s) == len(t):
        no_of_char = 2 ** 8
        counter_array = [0 for i in range(no_of_char)]
        for i in range(len(s)):
            counter_array[ord(s[i])] += 1
            counter_array[ord(t[i])] -= 1
        return sum([abs(i) for i in counter_array]) // 2
    else:
        return -1

print(minSteps("leetcode","practice"))