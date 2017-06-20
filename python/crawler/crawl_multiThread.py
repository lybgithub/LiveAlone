# coding=utf-8
import sys
import urllib.request
from lxml import etree
import re
import psycopg2
import time
import multiprocessing
import datetime
from random import choice
# import win32ras
import time, os

def Connect(dialname, account, passwd):
    dial_params = (dialname, '', '', account, passwd, '')
    return win32ras.Dial(None, None, dial_params, None)
def DialBroadband():
    dialname = '宽带连接'  # just a name
    account = 't534fhsyb0065'
    passwd = '123123'
    try:
        handle, result = Connect(dialname, account, passwd)
        if result == 0:
            print("Connection success!")
            return handle, result
        else:
            print("Connection failed, wait for 5 seconds and try again...")
            time.sleep(3)
            DialBroadband()
    except:
        print("Can't finish this connection, please check out.")
        return
def Disconnect(handle):
    if handle != None:
        try:
            win32ras.HangUp(handle)
            print("Disconnection success!")
            return "success"
        except:
            print("Disconnection failed, wait for 5 seconds and try again...")
            time.sleep(3)
            Disconnect()
    else:
        print("Can't find the process!")
        return
def Check_for_Broadband():
    connections = []
    connections = win32ras.EnumConnections()
    if (len(connections) == 0):
        print("The system is not running any broadband connection.")
        return
    else:
        print("The system is runining %d broadband connection." % len(connections))
        return connections
def ShowIpAddress():
    data = os.popen("ipconfig", "r").readlines()
    have_ppp = 0
    ip_str = None
    for line in data:
        if line.find("宽带连接") >= 0:
            have_ppp = 1
        if have_ppp and line.strip().startswith("IPv4 地址"):
            ip_str = line.split(":")[1].strip()
            have_ppp = 0
            print(ip_str)
def adsl():
    data = Check_for_Broadband()
    # if exist running broadband connection, disconnected it.
    if data != None:
        for p in data:
            ShowIpAddress()
            Disconnect(p[0])
            DialBroadband()
    else:
        DialBroadband()
        ShowIpAddress()



def crawler1(url):
    headers = {
        'Accept': 'extml,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'ccept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': ' sessionid=E3004469-51D1-7E0B-AA89-CF002BE8C4D4%7C%7C2015-12-07+10%3A52%3A28.712%7C%7Cwww.baidu.com; sessionuid=E3004469-51D1-7E0B-AA89-CF002BE8C4D4||2015-12-07+10%3A52%3A28.712||www.baidu.com; pcpopclub=8CBEF65B62D7ECBDB805C3CA3F607FFC1F0424A39D01708E06F99319F63A2D592E22F94129ECD94701E16E8C0933C83B280910443D9219F0D8909DF8154974C56B609955474A2C22813150039F7FAD0451F9A219A805F4B600B2DF4AD255928F25E830F4ADEF27ABCBF52EA2F733BE0ED02DC8F06953FC86AF2FBC68504CB39AE70D693E8B8C0230177E2266EE0CDEF29151FA19C9F65D5EF641EBDBB5E06C688392B4278715A6F7318629355EFFC49B4E4EB31B3F626EE92CA1666B21C3E24E43098B8AB4CF995710E7E03CB4717DD8BC86D4B827ED18C4588DD57EA5F16CB831D297DA8172F83075A1EA034353E7A7ADA326CBBD15D459CA82AB28FCBD75A393B992F3DA398F10B458D21C7126325F7BA886B5BF47F55DEE1CABA1C24810743424D84BC2DD791F86737A84C419F8583B337D73; clubUserShow=23409717|0|110100|%e8%8f%b2%e8%8f%b20363|0|0|0||2015-12-08 20:49:23|0; mylead_23409717=-1; sessionfid=3030395356; AccurateDirectseque=404; area=110199; sessionip=123.119.190.197; Hm_lvt_90ad5679753bd2b5dec95c4eb965145d=1449456746,1449566663,1449628070; Hm_lpvt_90ad5679753bd2b5dec95c4eb965145d=1449628070; __utma=1.1178593714.1449456744.1449566661.1449628065.3; __utmb=1.0.10.1449628065; __utmc=1; __utmz=1.1449628065.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_c5241958b568d64c9f23212513a22b7f=1449578969,1449628122; Hm_lpvt_c5241958b568d64c9f23212513a22b7f=1449628122; sessionvid=8A78DF8D-1896-0A21-9AB8-8ED8B6752704; ref=www.baidu.com%7C%7C0%7C8-1%7C2015-12-09+10%3A27%3A51.483%7C2015-12-07+10%3A52%3A28.712; ASP.NET_SessionId=kszp3ka1dws1lnvaumgryd5p',
        'Host': 'i.autohome.com.cn',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req).read().decode('gbk')
    return response

def crawler(url):
    headers = {
        'Accept': 'extml,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'ccept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': ' sessionid=E3004469-51D1-7E0B-AA89-CF002BE8C4D4%7C%7C2015-12-07+10%3A52%3A28.712%7C%7Cwww.baidu.com; sessionuid=E3004469-51D1-7E0B-AA89-CF002BE8C4D4||2015-12-07+10%3A52%3A28.712||www.baidu.com; pcpopclub=8CBEF65B62D7ECBDB805C3CA3F607FFC1F0424A39D01708E06F99319F63A2D592E22F94129ECD94701E16E8C0933C83B280910443D9219F0D8909DF8154974C56B609955474A2C22813150039F7FAD0451F9A219A805F4B600B2DF4AD255928F25E830F4ADEF27ABCBF52EA2F733BE0ED02DC8F06953FC86AF2FBC68504CB39AE70D693E8B8C0230177E2266EE0CDEF29151FA19C9F65D5EF641EBDBB5E06C688392B4278715A6F7318629355EFFC49B4E4EB31B3F626EE92CA1666B21C3E24E43098B8AB4CF995710E7E03CB4717DD8BC86D4B827ED18C4588DD57EA5F16CB831D297DA8172F83075A1EA034353E7A7ADA326CBBD15D459CA82AB28FCBD75A393B992F3DA398F10B458D21C7126325F7BA886B5BF47F55DEE1CABA1C24810743424D84BC2DD791F86737A84C419F8583B337D73; clubUserShow=23409717|0|110100|%e8%8f%b2%e8%8f%b20363|0|0|0||2015-12-08 20:49:23|0; mylead_23409717=-1; sessionfid=3030395356; AccurateDirectseque=404; area=110199; sessionip=123.119.190.197; Hm_lvt_90ad5679753bd2b5dec95c4eb965145d=1449456746,1449566663,1449628070; Hm_lpvt_90ad5679753bd2b5dec95c4eb965145d=1449628070; __utma=1.1178593714.1449456744.1449566661.1449628065.3; __utmb=1.0.10.1449628065; __utmc=1; __utmz=1.1449628065.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_c5241958b568d64c9f23212513a22b7f=1449578969,1449628122; Hm_lpvt_c5241958b568d64c9f23212513a22b7f=1449628122; sessionvid=8A78DF8D-1896-0A21-9AB8-8ED8B6752704; ref=www.baidu.com%7C%7C0%7C8-1%7C2015-12-09+10%3A27%3A51.483%7C2015-12-07+10%3A52%3A28.712; ASP.NET_SessionId=kszp3ka1dws1lnvaumgryd5p',
        'Host': 'i.autohome.com.cn',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req).read().decode('gbk')
    return response

def getUserInfo(userid):
    userName = ''
    sex = ''
    certificated = 0
    birth = 'null'
    dizhi = ''
    province = ''
    city = ''
    url = 'http://i.autohome.com.cn/' + str(userid) + '/info'
    response = crawler(url)
    REarea = re.compile('<span>(.*?):</span>(.*?)</p>')
    REresult = REarea.findall(response)
    for key, value in REresult:
        if key == '用户名':
            userName = value
        elif key == '性别':
            if value == '男':
                sex = 'm'
            if value == '女':
                sex = 'f'
        elif key == '手机认证':
            if '已认证' in value:
                certificated = 1
        elif key == '生日':
            birth = value
        elif key == '所在地':
            dizhi = value.replace('&nbsp;', ' ')
            area = value.split('&nbsp;')
            if len(area) == 2:
                province, city = area[0], area[1]
            if len(area) == 1:
                province = area[0]
    return userName, sex, certificated, birth, dizhi, province, city


def dealeachIDprocess(userid):
    conn = psycopg2.connect(database="dpidb", user="cndmp", password="DgzysLrdfk1401^", host="60.205.147.49", port="5432")
    cur = conn.cursor()
    flag = 0
    try:
        userName, gentle, certificated, birth, address, province, city = getUserInfo(userid)
        if userName != '':
            infoSql = "insert into gauss_car_webuser_info (web_code, user_id, name, certificated, gentle, address, province, city) values (1, '{}','{}','{}','{}','{}','{}','{}')".format(
                str(userid), userName, certificated, gentle, address, province, city)
        else:
            infoSql = "insert into gauss_car_webuser_info (user_id, certificated) values ('{}', '{}')".format(str(userid), 99)
        cur.execute(infoSql)
        conn.commit()
        flag = 1
    except Exception as e:
        print(e)
        pass
    if flag == 1:
        print(userid, 'success', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    else:
        print(userid, 'error', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    cur.close()
    conn.close()


def generateTaskList(start, end, queryCondition):
    conn = psycopg2.connect(database="dpidb", user="webuserowner", password="Njzyb204^", host="60.205.147.49",
                            port="5432")
    cur = conn.cursor()
    try:
        cur.execute("drop view gauss_car_webuser_info_{}".format(str(queryCondition)))
        print('delete old view...')
    except:
        print('old view dont exits')
    conn.commit()

    create = "create view gauss_car_webuser_info_{} as select user_id from gauss_car_webuser_info where user_id like '{}%'".format(str(queryCondition), str(queryCondition))
    cur.execute(create)
    conn.commit()
    print('create view finished...')
    cur.execute('select user_id from gauss_car_webuser_info_{}'.format(str(queryCondition)))
    finishUserList = [int(each[0]) for each in cur.fetchall()]
    print('get finished user list finish...')
    cur.close()
    conn.close()
    return set(range(start*10000, end*10000)).difference(set(finishUserList))


def processRun(start, end, queryCondition, processeslimit = 20):
    try:
        jobList = range(10100)
        while(len(jobList) > 10000):
            jobList = generateTaskList(start, end, queryCondition)
            pool = multiprocessing.Pool(processes=processeslimit)
            result = []
            for each in jobList:
                result.append(pool.apply_async(dealeachIDprocess, (each, )))
            pool.close()
            pool.join()
            print('多进程完毕')
    except Exception as e:
        print(e)
        print('爬取失败！！！')

if __name__ == '__main__':
    # if len(sys.argv) == 4:
    #     start = datetime.datetime.now()
    #     processRun(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    #     end = datetime.datetime.now()
    #     totaltime = end - start
    #     print('程序总用时：%s' % str(totaltime))
    # else:
    #     print('没有传入参数！！！')

    start = datetime.datetime.now()
    processRun(2600,2700,26)
    end = datetime.datetime.now()
    totaltime = end - start
    print('21区块总用时：%s' % str(totaltime))