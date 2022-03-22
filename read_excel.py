import xlrd
# #打开Excel文件读取数据('文件所在路径')
# data = xlrd.open_workbook(r'D:\BaiduNetdiskDownload\work\视频清单.xls')
# #根据sheet索引获取sheet内容
# sheet = data.sheet_by_index(0)
# #获取行数
# sheet_nrows = sheet.nrows
# # 创建存放这列数据的列表
# list1 = []
# # 从第三行开始读取数据
# i = 1
# while i < sheet_nrows:
#     list1.append(sheet.cell(i,0).value)
#     i +=1
# print(list1)
# # new_list = list(set(list1))                # 去重
# # new_list.sort(key=list1.index)             # 去重后顺序不变
# # print(new_list )
#

def read_name(file_dir):
    data = xlrd.open_workbook(r'{}\视频清单.xls'.format(file_dir))
    # 根据sheet索引获取sheet内容
    sheet = data.sheet_by_index(0)
    # 获取行数
    sheet_nrows = sheet.nrows
    # 创建存放这列数据的列表
    video1 = []
    video2 = []
    path1 = []
    k_v = {}
    # 从第三行开始读取数据
    i = 1
    while i < sheet_nrows:
        video1.append(sheet.cell(i, 0).value)
        path1.append(sheet.cell(i, 3).value)
        k_v[sheet.cell(i, 0).value]= sheet.cell(i, 3).value
        i += 1
    print(video1)   #从excel中读取全部的视频
    print(path1)  #从excel中读取全部的视频  对应的路径

    #可以将 第一次压缩 继续 第二次压缩
    for i in video1:
        if(i[-7:-4]!="_01"):  # 将没有压缩过的原文件名称 赋值给video2 即筛选过的数据
            video2.append(i)
        if (i[-7:-4] == "_01"):  #将源文件中k-v 有压缩二字的删除
            del k_v[i]
    print(video2) #剔除压缩过的视频  赋值给video2
    print(k_v)  #同时删除 压缩的视频以及路径

    return k_v,video2  #返回字典key-value 分别对应的视频和路径