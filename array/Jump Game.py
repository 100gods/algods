def canReach(A, N):
    # code here
    if A[0] == 0:
        return 0
    if N == 1 and A[N] != 0:
        return 1
    dis_to_end = 1
    for i in range(N - 1 -1, 0, -1):
        if A[i] == 0:
            dis_to_end += 1
        elif A[i] >= dis_to_end:
            dis_to_end = 1
        else:
            dis_to_end +=1
        print(A[i], dis_to_end, i)
    print(dis_to_end+1,A[0])
    if A[0] >= dis_to_end >0 :
        return 1
    else:
        return 0
#1 1 2 0 2 0 1 1 1
#1 1 0 2 0 2 2 2 2
#print(canReach([1,1,0,2,0,2,2,2,2],9))
print(canReach([1,1,2,0,2,0,1,1,1],9))
#print(canReach([1,2,0,3,0,0],6))
#print(canReach([1,0,3],3))
s = "28 81 135 113 40 24 100 124 86 100 16 67 23 60 126 125 94 34 79 23 10 7 123 33 102 108 94 105 74 101 68 82 32 72 35 115 84 12 39 13 57 109 17 86 44 43 9 86 70 54 87 6 6 97 22 58 75 36 46 68 45 34 60 25 51 28 22 54 52 65 22 74 7 40 10 2 50 2 6 52 20 8 20 7 33 12 47 5 4 1 31 14 39 4 54 18 35 13 8 0 6 44 0 3 26 30 33 29 27 37 38 31 33 27 32 27 24 21 21 24 21 23 15 12 12 12 20 14 1 13 3 3 10 8 10 2 7 2 0 2 2 0 4 0 0 1 0 2 0 1 0 0"
arr = list(map(int,s.split(" ")))
#print(len(arr))
#print(canReach(arr,len(arr)))