files_list = ['1.txt', '2.txt', '3.txt']
dict_1 = {}
dict_2 = {}
with open('4.txt', 'w', encoding = 'utf-8') as new_txt:
    for file in files_list:
        with open(file, encoding = 'utf-8') as infile:
            count = 0
            for line in infile:
                count += 1
                if file in dict_2:
                    dict_2[file].append(line)
                else:
                    dict_2[file] = [line]
            dict_1[file] = count
            new_txt.write(infile.read())
    answer = sorted(dict_1.items(), key=lambda item: item[1], reverse=False)
    for new_text in answer:
        name_file = new_text[0]
        count_line = new_text[1]
        new_txt.write(name_file + '\n' + str(count_line) + '\n' + str('\n'.join(dict_2[new_text[0]])) + '\n')
new_txt.close()