# logical_oper
# -----------
# and , or , not

# in case of AND
# true and true =true -  print(1<4 and 5>4)
# true and false = false - print(1<4 and 5>6)
# false and true = false - print(4<1 and 5>4)
# false and false = false - print(4<1 and 2>4)
# eg:
print(1<4 and 5>4)
print(5<4 and 5>8)

#  in case of OR
# # true and true =true - print(1<4 and 5>4)
# # true and false = true - print(1<4 and 5>6)
# # false and true = true - print(5<4 and 5>4)
# # false and false = false - print(5<4 and 5>8)
# eg:
print(1<4 or 5>4)
print(3<4 or 5>8)

#  in case of NOT

print(not (3>1)) # true = false
print(not (True==False)) # false = true