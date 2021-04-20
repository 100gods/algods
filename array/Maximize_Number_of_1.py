def findZeroes(arr, n, m) :
    zero_counter = 0
    left ,right = 0,0
    max_win,cur_win = 0,0
    #print(arr[right], zero_counter, max_win,cur_win)
    while right < n and left <= right:
        if arr[right] == 0 and zero_counter < m:
            zero_counter +=1
            right +=1
            cur_win += 1
        elif zero_counter <= m and arr[right] == 1:
            right+=1
            cur_win +=1
        else:
            max_win = max(max_win, cur_win)
            while zero_counter >= m :
                if arr[left] == 0 :
                    zero_counter -=1
                left +=1
                cur_win -=1
    #print(max(max_win,cur_win))
    return max(max_win,cur_win)

print(findZeroes([1 ,0, 1, 0],4,0))
