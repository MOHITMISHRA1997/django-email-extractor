import re

str1 = "sdfffaaaaaaaaaaaaaafsdaf mohit@gmail.com dfsdfdsf asdfsdfsadf mera naam mohit mishra hai aur meri id ye hai mohit@proton.me bur lohit ka email it hai lohit@hotmail.in"

matches = re.finditer(r"\s\w*@\w*.\w*",str1)
for match in matches:
    print(match)


