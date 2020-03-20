def lps(string):
    n = len(string)
    dp = [[0 for i in range(n)] for i in range(n)]  
    for i in range(len(string)): dp[i][i] = 1  # length one palindrome
    for cl in range(2,n+1):  # length of palindrome cl
        for i in range(n+1-cl):  # iterating rows of dp  
            j = i+cl-1  # even though the palindrome length is "x" but ans will be stored at dp[i][x-1]
            if string[i] == string[j] and cl==2:  # if starting and ending character are same and palindrome length is 2 then simple 2
                dp[i][j] = 2
            elif string[i] == string[j]:  # if length is not two and char are same then 2 + diagonal value
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    print(dp[0][n-1], dp)

s = "bcgca"
lps(s)
