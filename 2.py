s = '((IIII))))))(aa('
list_s = list(s)
list_s

L = []
for i in range(len(s)):
#     print(s[i])
    if s[i] == '(':
        L.append(')')
#         print(i)
        continue
    if s[i] == ')':
        if L and L[-1] == s[i]:
            print('hit')
            L.pop()
        else:
            list_s[i] = '?'

print(list_s)
print(L)
# print(list_s[:len(list_s)-len(L)] + L)
tmp = ''.join(list(reversed(list_s))).replace('(', 'x' , len(L))

final = ''.join(list(reversed(tmp)))

print(final, "\n", s)
