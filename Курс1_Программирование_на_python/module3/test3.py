# with open('file1.txt', 'r', encoding='utf-8') as file:
#     counter = {1: 0, 2: 0, 3: 0}
#     counter_of_strings = 0
#     for s in file:
#         s = s.strip().split(';')
#         rou = 0
#         count_in_string = 0
#         counter_of_strings += 1
#         for i in range(1, len(s)):
#             count_in_string += int(s[i])
#             counter[i] += int(s[i])
#         rou = count_in_string / 3
#         print(rou)
#     for key in counter.keys():
#         print(counter[key] / counter_of_strings, end=' ')
#     print(counter)
#     print(counter_of_strings)
#
#
#



with open('dataset_3363_4.txt', 'r', encoding='utf-8') as file:
    counter = {1: 0, 2: 0, 3: 0}
    counter_of_strings = 0
    for s in file:
        s = s.strip().split(';')
        rou = 0
        count_in_string = 0
        counter_of_strings += 1
        for i in range(1, len(s)):
            count_in_string += int(s[i])
            counter[i] += int(s[i])
        rou = count_in_string / 3
        with open('result.txt', 'a') as f:
            f.write(str(rou) + '\n')
    word = ''
    for key in counter.keys():
        word += str(counter[key] / counter_of_strings) + ' '
    with open('result.txt', 'a') as c:
        c.write(word)




