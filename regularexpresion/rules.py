#1.'[abc]'-Either a,b or c
# import re
# x='[abc]'#either a,b or c
# matcher=re.finditer(x,"abt c@5kz")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#2.'[^abc]'-Except a,b or c
# import re
# x='[^abc]'#except a,b or c
# matcher=re.finditer(x,"abt c@5kz")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#3.'[a-z]'-a to z letters
# import re
# x='[a-z]'#a to z
# matcher=re.finditer(x,"abt c@5kz")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#4.'[A-Z]'-A to Z letters
# import re
# x='[A-Z]'#A to Z
# matcher=re.finditer(x,"abt c@5kz")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#5.'[a-zA-Z]'-a to z and A-Z
# import re
# x='[a-zA-Z]'#a to z and A to Z
# matcher=re.finditer(x,"abt c@5kzAKKSJ")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#6.'[0-9]'-to check numbers
# import re
# x='[0-9]'#0 to 9
# matcher=re.finditer(x,"abt c@5kz")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#7.'[^a-zA-Z0-9]'-special symbols
# import re
# x='[^a-zA-Z0-9]'
# matcher=re.finditer(x,"abt c@5kz")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#8.'\s'-to check space
#9.'\d'-to check digits
# 10.'\D'-except digits
# import re
# x='\s'
# matcher=re.finditer(x,"abt c@5kz")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#11.'\w'-all words except special characters
#12.'\W'-special characters
# import re
# x='\W'
# matcher=re.finditer(x,"abt c@5kz")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#13."a+"-a including group
# import re
# x="a+"
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
#14."a*"-count including zero number of a
# import re
# x="a*"#if no zero
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
#15."a?"-count a as each including zero row of a
# import re
# x="a?"
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
#16."a{4}"-no:of a positions
#17."a{2,3}"-find between 2 and 3.2 is minimum 3 is maximum
# import re
# x="a{4}"#find a with for count
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
#18."^a"-check starting with a
import re
x="^a"
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())
#19."a$"-check ending with a