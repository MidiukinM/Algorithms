lst = list(input().split())
ans = False
for el in lst:
    if el != 'None':
        print(el)
        ans = True
        break
        
if not ans:
    print('None')
