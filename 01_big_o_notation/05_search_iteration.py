# WORST CASE SENARIO
# 0(n) 
a_list = [4, 9,15,21,34,57,68,91]
search_item = 68
for i in range(len(a_list)):
    if a_list[i] == search_item:
        print(i)
# LINEAR SEARCH - THIS WILL CHECK ALL ITEM AND MATCH THEM 




# BINARY SEARCH 
# ITERATION 1=N/2     - THIS WILL CHECK FOR THE MIDDLE ELEMENT FIRST 
# ITERATION 2=(N/2)/2 = N/2^2    - N IF SEARCH ELEMENT IS NOT IN THE LEFT OF MIDDLE ELEMET THEN LEFT SIDE WILL BE DISCARDED 
# ITERATION 3=(N/2)/2 = N/2^3    - IN EVERY ITERATION HALF ELEMENT WILL BE DISCARDED
# ITERATION K=K/2^K 


"""
Iteration k = n/2^k
1=n/2^k
n=2^k
log_2 n=log_2 2^k
log_2 n=k*log_2 2            we know, log_2 2 = 1
K = log n
O(log n)
"""

# K = O(log n) -> log_2 8 -> log_2 2^3 -> 3 * log_2 2 = 3 Iterations 

