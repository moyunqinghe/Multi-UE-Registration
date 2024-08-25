"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@Project : Python_project
@File : ue_copy.py
@Time : 2023/6/10 21:18
@Author : ruoli

@Describe : 

"""
import shutil

count = 1000

for i in range(0, count):
    # 1.复制文件
    temp_file_path = "UERANSIM/config/free5gc-ue.yaml"
    new_file_path = "UERANSIM/config/free5gc-ue-{}.yaml".format(i)
    shutil.copyfile(temp_file_path, new_file_path)

    # 2. 修改 SUPI 和 K* 的值
    # 2.1 打开、读取模板文件
    temp_file = open(temp_file_path)
    infos = temp_file.readlines()
    temp_file.close()
    # 2.2 修改值
    SUPI = "supi: 'imsi-20xxxxxxxxxxxxxxx0{}'".format(str(i).rjust(4, "0"))
    infos[1] = SUPI
    K = "key: '8baf4xxxxxxxxxxxxxxxxxx097c{}'".format(str(i).rjust(4, "0"))
    infos[8] = K
    opType = "opType: 'OPC'"
    infos[12] = opType


    # 2.3 写入新文件
    fil = open(new_file_path, mode='w')
    fil.writelines(infos)
    fil.close()




