import collections
def check_anagram(c_one: str, c_two: str) -> bool:
    for i in range(26):
        if c_one[i] != c_two[i]:
            return False
    return True


def sig_anagram(str_one: str) :
    no_of_char = 26
    counter_array = [0 for i in range(no_of_char)]
    for i in range(len(str_one)):
        counter_array[ord(str_one[i]) - ord('a')] += 1
    return counter_array


def groupAnagrams(strs: [str]) :
    if strs:
        sig_grp_map = collections.defaultdict(list)
        sig_grp_map[tuple(sig_anagram(strs[0]))].append(strs[0])
        for i in range(1, len(strs)):
            sig_grp_map[tuple(sig_anagram(strs[i]))].append(strs[i])
        return sig_grp_map.values()


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))