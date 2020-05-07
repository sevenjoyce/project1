
# fo = open('E:\\简历\\松勤\\新建文本文档.txt')
# # print(fo.read())
# print(fo.read(2))
# print(fo.tell())
# print(fo.seek(1,0)) #(1进几步,0)0模式从头开始
# print(fo.tell())

'''
name: Jack ; salary:   1200
 name:  Jack ; salary:  1800
  name: Jack ; salary:     100
'''

rdir = r'E:\简历\松勤\Python\ex_file.txt'
wdir = r'E:\简历\松勤\Python\ex_file1.txt'
# 读取多个文件
with open(rdir) as f1, open(wdir, 'w') as f2:
    # 读取所有行放入列表
    rlines = f1.read().splitlines()

    for line in rlines:
        temp = line.split(';')
        name = temp[0].split(':')[-1].strip() #.strip()去掉空格
        sal = int(temp[1].split(':')[-1].strip())

        info = f'name:{name:<6}salary:{sal:<6}tax:{int(sal*0.1):<6}'
        print(info)

        f2.write(info+'\n')


