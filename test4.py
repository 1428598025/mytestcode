import json
import os
import time
import shutil

# 读取日志文件，日志文件路径请自行修改
with open(r'C:/Users/14285/Desktop/2023-04-11.log', 'r', encoding='utf-8') as f:
    data = f.readlines()

# 提取需要保存的数据并保存到JSON文件
for i in range(len(data)):
    if 'INFO Write json：' in data[i]:
        save_data = data[i].split('INFO Write json：')[1].strip()
        # 检查'to C:'是否在save_data中出现，如果不存在，跳过当前迭代
        if 'to C:' not in save_data:
            continue
        save_data = save_data.split('to C:')[0].strip()
        if save_data:
            # 将数据写入JSON文件
            with open('C:/Users/14285/Desktop/test/data.json', 'w', encoding='utf-8') as f:
                json.dump(json.loads(save_data), f, ensure_ascii=False, indent=4)
            with open('C:/Users/14285/Desktop/test/data.json', 'r', encoding='utf-8') as f:
                data = f.read().replace(' ', '').replace('\n', '').replace('\t', '')
            with open('C:/Users/14285/Desktop/test/data.json', 'w', encoding='utf-8') as f:
                f.write(data)
            # 将JSON文件复制到到C:/Users/14285/Desktop/test1
            shutil.move('C:/Users/14285/Desktop/test/data.json', 'C:/Users/14285/Desktop/test1/data.json')
            # 删除test.json中的数据
            with open('C:/Users/14285/Desktop/test/data.json', 'w', encoding='utf-8') as f:
                f.write('')
            # 等待10秒
            time.sleep(10)
