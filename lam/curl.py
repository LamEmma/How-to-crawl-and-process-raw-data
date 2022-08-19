import csv 
file = open('raw_data.txt', 'r')

# Read all the students
datas = file.read().split('\n')

# write header to csv
with open ('clean_data.csv', 'w', encoding='utf8', newline='') as file_csv:
    header = ["sbd", "tên", "dd", "mm", "yy", "toán", "ngữ văn", "khxh", "khtn", "lịch sử", "địa lí", "gdcd", "sinh học", "vật lí", "hóa học", "tiếng anh"]
    writer = csv.writer(file_csv)
    writer.writerow(header)

# file_csv = open('clean_data.csv', 'w', encoding='utf8', newline='')
# header = ["sbd", "tên", "dd", "mm", "yy", "toán", "ngữ văn", "khxh", "khtn", "lịch sử", "địa lí", "gdcd", "sinh học", "vật lí", "hóa học", "tiếng anh"]
# file_csv = csv.writer(file_csv)
# file_csv.writerow(header)

file = open('no_id.txt', 'r')
un_sbd = file.read().split('\n')
for i in range(len(un_sbd)):
    un_sbd[i] = int(un_sbd[i])

# file = open('data.txt', 'w', encoding='utf-8-sig')
sbd = 200000
for data in datas:
    sbd += 1
    if sbd in un_sbd:
        continue 
    sbd_str = '0' + str(sbd)
    # make data become a list
    data = data.split('\\n')
    # Remove \r and \t
    for i in range(len(data)):
        data[i] = data[i].replace('\\r', '')
        data[i] = data[i].replace('\\t', '')

    # remove tags
    for i in range(len(data)):
        tags = []
        for j in range(len(data[i])):
            if data[i][j] == '<':
                start = j
            if data[i][j] == '>':
                end = j 
                tags.append(data[i][start:end+1])
        for tag in tags: 
            data[i] = data[i].replace(tag, '')

    for i in range(len(data)):
        data[i] = data[i].strip()

    unempty_lines = []

    for i in range(len(data)):
        if data[i] != '':
            unempty_lines.append(data[i])

    data = unempty_lines 


    # choose info relevant 
    name = data[7]
    dob = data[8]
    scores = data[9]


    # process unicode 
    file = open('unicode.txt', 'r', encoding='utf-8-sig')
    unicode_table = file.read().split('\n')

    chars = []
    codes = []

    for code in unicode_table:
        x = code.split(' ')
        chars.append(x[0])
        codes.append(x[1])

    # replace codes by chars in name and scores
    for i in range(len(chars)):
        name = name.replace(codes[i], chars[i])
        scores = scores.replace(codes[i], chars[i])


    for i in range(len(name)):
        if name[i:i+2] == '&#':
            name = name[:i] + chr(int(name[i+2:i+5])) + name[i+6:]

    for i in range(len(scores)):
        if scores[i:i+2] == '&#':
            scores = scores[:i] + chr(int(scores[i+2:i+5])) + scores[i+6:]

    name = name.lower()
    scores = scores.lower()
    dob = dob.lower()

    # split dob
    dob_list = dob.split('/')
    dd = dob_list[0]
    mm= dob_list[1]
    yy = dob_list[2]

    # split scores
    scores = scores.replace(':', '')
    scores = scores.replace('khxh ', 'khxh   ')
    scores = scores.replace('khtn ', 'khtn   ')

    score_list = scores.split('   ')

    data = [sbd_str, name.title(), str(dd), str(mm), str(yy)]

    for subject in ['toán','ngữ văn','khxh', 'khtn', 'lịch sử', 'địa lí', 'gdcd', 'sinh học', 'vật lí', 'hoá học', 'tiếng anh']:
        if subject in score_list:
            data.append(score_list[(score_list.index(subject)+1)]) 
        else:
            data.append('-1')

    # with open('clean_data.csv', 'a', encoding='utf-8-sig', newline='') as file_csv:
    #     for i in range(len(data)):
    #         file_csv.write(str(data[i]) + ',')
    #     file_csv.write('\n')   

    with open('clean_data.csv', 'a', encoding='utf-8-sig', newline='') as file_csv: 
        writer = csv.writer(file_csv)
        writer.writerow(data)