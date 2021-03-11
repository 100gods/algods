def lengthOfLongestSubstring(s: str) -> int:
    '''
    Longest Substring Without Repeating Characters
    :param self:
    :param s:
    :return:
    '''
    seen_dict = dict()
    res, start_pos = -1, 0
    for i in range(len(s)):
        if s[i] in seen_dict:
            # check if start_pos is after last seen index
            if start_pos > seen_dict[s[i]]:
                seen_dict[s[i]] = i
            else:
                res = max(res, i - start_pos)
                start_pos = seen_dict[s[i]] + 1
                seen_dict[s[i]] = i

        else:
            seen_dict[s[i]] = i

    res = max(res, len(s) - start_pos)
    return res

print(lengthOfLongestSubstring("abacafd"))