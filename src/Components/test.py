import re

# 读取文件内容
with open('metadata.json', 'r', encoding='utf-8') as file:
    content = file.read()

# 正则表达式匹配特定键的括号中的内容
pattern = re.compile(r'"gStaticUrl":"(.*?)"|'
                     r'"leftEmoji":"(.*?)"|'
                     r'"rightEmoji":"(.*?)"')
matches = pattern.findall(content)

# 提取匹配结果并过滤空值
results = [match for sublist in matches for match in sublist if match]

# 输出匹配结果到文本文件
with open('output.txt', 'w', encoding='utf-8') as output_file:
    for i in range(0, len(results) // 3):
        if results[i * 3 + 1] == '😱':
            print(results[i * 3 ] + results[i * 3 + 1] + results[i * 3 + 2])
        output_file.write(results[i * 3] + ' ' + results[i * 3 + 1] + ' ' + results[i * 3 + 2] + '\n')

