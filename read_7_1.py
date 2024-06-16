file_name = 'out_7_1.txt'
file = open(file_name, mode ='r', encoding='utf8')
file_content = file.read()
file.close()
print(file_content)