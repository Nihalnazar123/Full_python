# store the square value of s1 in s2
#
# s1={1,4,7,9,22,3,44}
# s2=set()
# for i in s1:
#     s2.add(i*i)
# print(s2)
#
#
# # separate +ve and -ve values
# s={1,-4,2,5,-9,6,-3,99,-65,88,-54}
# pos=set()
# neg=set()
# for i in s:
#     if i>0:
#         pos.add(i)
#     else:
#         neg.add(i)
# print(pos)
# print(neg)

# separate even and odd values
s={1,2,3,4,5,6,7,8,9}
even=set()
odd=set()
for i in s:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
print('even',even)
print('odd',odd)
