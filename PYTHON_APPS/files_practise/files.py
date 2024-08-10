# user_prompt = input('Enter a New member :- ')
# user_prompt = user_prompt.strip()

# file = open('members.txt','r')
# file_output = file.readlines()
# file.close()

# file_output.append(user_prompt)

# file_1 = open('members.txt','w')
# new_file = file_1.writelines(file_output)
# file_1.close()


# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# file_content = ['hello']

# for filename in filenames:
#     file=open(filename,'w')
#     file.write('hello')
#     file.close()

file_names = ['a.txt','b.txt','c.txt']

for file_name in file_names:
    file = open(file_name,'r')
    a = file.read()
    file.close()
    print(a)
