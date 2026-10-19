# 3.1

# A = True
# B = False
# C = False

# res_a = A or B #T or F -> T
# res_b = A and B # T and F -> F
# res_c = B or C #F or F -> F

# print(res_a, res_b, res_c)

# # 3.3

# A = True
# B = False
# C = False
# res_a = not(A) and B #not(T) -> f and F - > F
# res_b = A or not(B) #T or not(F) -> T or T -> T
# res_c = (A and B) or C #(T and F) or F -> F or F -> F

# # 3.7

# A = True
# B = False
# C = False

# res_a = (A or not(A and B)) or C #(T or not(T and F)) or F -> (T or T) or F -> T or F -> T
# res_b = not(A) or A and (B or C) #F or T and F -> F or F -> F
# res_c = (A or B and not(C)) and C #T or F and T) and F -> F

# 3.12 

A = True
B = False
C = False

res_a = not(A or not(B) and C)
res_b = A and not(B or not(C))
res_c = not(not(A) or B and C)
print(res_a, res_b, res_c)

# 3.14

A = True
B = False
C = False

res_a = (not(A) and not(B)) and (not(A) or not(C))