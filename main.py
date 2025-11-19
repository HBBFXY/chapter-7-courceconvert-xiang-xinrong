import keyword

# 读取原文件内容
with open('random_int.py', 'r') as f:
    content = f.read()

# 拆分内容为单词和非单词部分（简单处理）
words = content.split()
result = []
for word in words:
    if word not in keyword.kwlist:
        result.append(word.upper())
    else:
        result.append(word)

# 拼接处理后的内容
new_content = ' '.join(result)

# 写入新文件
with open('converted_random_int.py', 'w') as f:
    f.write(new_content)
