dp = {}
 
# Function to check array can be 
# partition into sum of 3 equal 
def checkEqualSumUtil(arr, N, sm1, sm2, sm3, j):
     
    s = str(sm1) + "_" + str(sm2) + str(j)
     
    # Base Case
    if j == N:
        if sm1 == sm2 and sm2 == sm3:
            return 1
        else:
            return 0
         
    # If value at particular index is not 
    # -1 then return value at that index 
    # which ensure no more further calls 
    if s in dp:
        return dp[s]
     
    # When element at index 
    # j is added to sm1 
    l = checkEqualSumUtil(arr, N, sm1 + arr[j],
                          sm2, sm3, j + 1)
     
    # When element at index 
    # j is added to sm2 
    m = checkEqualSumUtil(arr, N, sm1,
                          sm2 + arr[j], sm3,
                            j + 1)
     
    # When element at index 
    # j is added to sm3 
    r = checkEqualSumUtil(arr, N, sm1, 
                          sm2, sm3 + arr[j], 
                                 j + 1)
     
    # Update the current state and 
    # return that value 
    dp[s] = max(l, m, r)
     
    return dp[s]
 
# Function to check array can be 
# partition to 3 subsequences of 
# equal sum or not 
def checkEqualSum(arr, N):
     
    # Initialise 3 sums to 0 
    sum1 = sum2 = sum3 = 0
     
    # Function Call
    if checkEqualSumUtil(arr, N, sum1,
                         sum2, sum3, 0) == 1:
        print("Yes")
    else:
        print("No")
         
# Driver code
 
# Given array arr[] 
arr = [ 17, 34, 59, 23, 17, 67, 57, 2, 18, 59, 1 ]
N = len(arr)
 
# Function call 
checkEqualSum(arr, N)
