"""postmanlog数据分析
    1.响应时间平均值（最大值最小值）
    2.响应文件大小平均值（最大值最小值）"""
import os
import json

Json_filepath = os.getcwd()
for root,dirs,filelist in os.walk(Json_filepath):
    for filename in filelist:
        if os.path.splitext(filename)[1] == ".json":
            itemfile_wholepath = os.path.join(root,filename)

with open(itemfile_wholepath,'r',encoding='UTF-8') as f:
    response_dict = json.load(f)
    num_of_test = len(response_dict['results'])
    totaltime = response_dict['totalTime']
    print("测试名称",response_dict['name'])
    print("测试包含项目数：",num_of_test)
    print("测试次数",response_dict['count'])
    print("共用时%s ms"%totaltime)
    print("\n")

#创建一个字典，键：name，值：url
name_list = []
url_list = []
for ele in response_dict['requests']:
    name_list.append(ele['name'])
    url_list.append(ele['url'])
info_dict = dict(zip(name_list,url_list))

def Items():
    """这里以列表的形式给出每一项测试"""
    for item in response_dict['results']:
        responseCode = item['responseCode']
        name = item['name']
        if name in info_dict:
            info_url = info_dict[name]
        trans = []
        for i in item['times']:
            num = int(i)
            trans.append(num)
        LongestTime = max(trans)
        ShortestTime = min(trans)
        AverageTime = item['totalRequestTime'] / response_dict['count']
        print("测试项目名:%s,状态码：%s" %(item['name'],responseCode['code']))
        print("url:",info_url)
        print("每次响应时长：",item['times'])
        print("%s 次响应共用时%s ms，最长用时%s ms，最短用时%s ms，平均用时%s ms"%(response_dict['count'],item['totalRequestTime'],LongestTime,ShortestTime,AverageTime))
        print("测试用例及结果：")
        for trkv in item['testPassFailCounts']:
            print(trkv,item['testPassFailCounts'][trkv])
        print("\n")
Items()