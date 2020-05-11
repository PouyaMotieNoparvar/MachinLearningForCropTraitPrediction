'''
برای جدا کردن مسیرهای تمام شده با کلمه
calls
'''



import re


target = open('d:/Dave/all_paths.txt', 'r').readlines()
out_put = open('d:/Dave/all_line_by_calls.txt','w')

# if find a line that finished by calls write it in out_put file
for item in target:
    if re.findall('^.*calls$',item):
        out_put.write(item)

out_put.close()
