from itertools import zip_longest

hobby_f = open('hobby.csv', 'r', encoding='utf-8')
user_f = open('users.csv', 'r', encoding='utf-8')
out_f = open('out_file', 'w', encoding='utf=8')
"""
программа записывала каждый раз на новой строке, чтобы убрать сделал Content и Clean_content
они создают строку и убирают из нее лишние символы \n
"""
for user, hobby in zip_longest(user_f, hobby_f):
        content = (f'{user}: {hobby}')
        clean_content = content.replace('\n', ' ')# убирает лишние \n
        out_f.write(f'{clean_content}\n')# используется уже для вывода каждого результата на новой строке
hobby_f.close()
user_f.close()
out_f.close()
