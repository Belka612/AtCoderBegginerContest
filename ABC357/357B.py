S = input()
upper_num = sum([s.isupper() for s in S])
lowwer_num = sum([s.islower() for s in S])
if upper_num > lowwer_num:
    print(S.upper())
else:
    print(S.lower())