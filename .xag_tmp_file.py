
#!/usr/bin/env python
# -*- coding: gb2312 -*-

import msvcrt
import sys
import TradeX
import pdb


def check_start_time(want_time):
    # eg:a="11:59:59"
    import time
    while True:
        #a = time.strftime('%H:%M:%S', time.localtime(time.time()))
        a=datetime.datetime.now().strftime('%H:%M:%S:%f')
        print(a)
        if (a[0:2] == want_time[0:2] and a[3:5] == want_time[3:5] and a[6:8] == want_time[6:8]):
            break
        else:
            print("还没到点...")
            time.sleep(0.5)
            continue
    time.sleep(0.7)
    a = time.strftime('%H:%M:%S', time.localtime(time.time()))
    print("到点,现在时刻:%s" % a)


print("\t**********************************************************************")
print("\t*                                TradeX v1.4.0                       *")
print("\t*                                                                    *")
print("\t*  TradeX 股票程序交易接口全新发布！                                 *")
print("\t*                                                                    *")
print("\t*  版本描述：                                                        *")
print("\t*  1）支持普通账户/融资融券信用账户业务，包括全新的担保品买入、卖出  *")
print("\t*   和免配置一键打新功能；解决了华福证券50条记录的限制；             *")
print("\t*  2）支持批量多连接下单和多账户同时下单，每秒批量下单可达数百单；   *")
print("\t*  3）支持股票的普通行情、Level 2十档、逐笔行情以及期货等扩展行情，  *")
print("\t*   允许同时批量多连接取行情；                                       *")
print("\t*  4）直连交易服务器和行情服务器，无中转，安全、稳定，实盘运行中；   *")
print("\t*  5）支持C++，C#，Python，Delphi，Java，易语言，AutoIt等语言；      *")
print("\t*  6）完美兼容trade.dll，解决了华泰、光大等券商的连接问题。          *")
print("\t*                                                                    *")
print("\t*  技术QQ群：318139137  QQ：3048747297                               *")
print("\t*  技术首页：https://tradexdll.com/                                  *")
print("\t*  http://pan.baidu.com/s/1jIjYq1K                                   *")
print("\t*                                                                    *")
print("\t**********************************************************************")

#print("\n\t按任意键继续...\n")
#msvcrt.getch()

#
#
#
print("\t1、初始化...\n")
err = TradeX.OpenTdx(14, "7.06", 12, 0)
if err != "":
    print(err)

#
#
#
print("\t2、登录交易服务器...\n")

# 交易服务器主机
nQsid = 22
#sHost = "mock.tdx.com.cn"
sHost = "rzjy1.gtja.com"
nPort = 7708
sVersion = "7.06"
nBranchID = 89
nAccountType = 8
sAccountNo = "220033390"
sTradeAccountNo = "220033390"
sPassword = "850503"
sTxPassword = ""

try:
    client = TradeX.Logon(nQsid, sHost, nPort, sVersion, nBranchID,
                          nAccountType, sAccountNo, sTradeAccountNo, sPassword, sTxPassword)
    errinfo = client.IsConnectOK()
    if errinfo != 1:
        print(errinfo)
        sys.exit(-1)
    else:
        print("交易连接正确")
        print("\n\t成功登录\n")
except TradeX.error as err:
    print("error: ", err)
    msvcrt.getch()
    TradeX.CloseTdx()
    sys.exit(-1)


#print ("\n\t按任意键继续...\n")
# msvcrt.getch()

shenAgudong = "0219191964"
huAgudong = "A704617409"
#
#
#


#09:15:00买入

nCategory = 0
nOrderType = 0
sInvestorAccount = shenAgudong
# 深A股票:宁德时代
sStockCode = "300750"
# 25.14*1.2=30.168
sPrice = 30.17
#sVolume = 500 * 10000
sVolume = 100
order1 = (nCategory, nOrderType, sInvestorAccount, sStockCode, sPrice, sVolume)

nCategory = 0
nOrderType = 0
sInvestorAccount = huAgudong
# 沪A股票:绿色时代
sStockCode = "601330"
# 3.29*1.2=3.948
sPrice = 3.95
#sVolume = 500 * 10000
sVolume = 100
order2 = (nCategory, nOrderType, sInvestorAccount, sStockCode, sPrice, sVolume)

check_start_time("00:05:50")
res = client.SendOrders((order1, order2))
for elem in res:
    errinfo, result = elem
    if errinfo != "":
        print(errinfo)
    else:
        print(result)
        pdb.set_trace()


pdb.set_trace()
sys.exit(0)
#09:30:00买入

nCategory = 0
nOrderType = 0
sInvestorAccount = shenAgudong
# 深A股票:宁德时代
sStockCode = "300750"
# 25.14*1.44=36.2016
sPrice = 36.20
sVolume = 500 * 10000
order1 = (nCategory, nOrderType, sInvestorAccount, sStockCode, sPrice, sVolume)

nCategory = 0
nOrderType = 0
sInvestorAccount = huAgudong
# 沪A股票:绿色时代
sStockCode = "601330"
# 3.29*1.44=4.7376
sPrice = 4.74
sVolume = 500 * 10000
order2 = (nCategory, nOrderType, sInvestorAccount, sStockCode, sPrice, sVolume)

check_start_time("09:30:00")
res = client.SendOrders((order1, order2))
for elem in res:
    errinfo, result = elem
    if errinfo != "":
        print(errinfo)
    else:
        print(result)



#10:00:00买入

nCategory = 0
nOrderType = 0
sInvestorAccount = shenAgudong
# 深A股票:宁德时代
sStockCode = "300750"
# 25.14*1.44=36.2016
sPrice = 36.20
sVolume = 500 * 10000
order1 = (nCategory, nOrderType, sInvestorAccount, sStockCode, sPrice, sVolume)

nCategory = 0
nOrderType = 0
sInvestorAccount = huAgudong
# 沪A股票:绿色时代
sStockCode = "601330"
# 3.29*1.44=4.7376
sPrice = 4.74
sVolume = 500 * 10000
order2 = (nCategory, nOrderType, sInvestorAccount, sStockCode, sPrice, sVolume)

check_start_time("10:00:00")
res = client.SendOrders((order1, order2))
for elem in res:
    errinfo, result = elem
    if errinfo != "":
        print(errinfo)
    else:
        print(result)

input()
sys.exit(0)

print("\t3、查询资金...\n")

nCategory = 0

status, content = client.QueryData(nCategory)
if status < 0:
    print("error: " + content)
else:
    print(content)

#print ("\n\t按任意键继续...\n")
# msvcrt.getch()

#
#
#
print("\t4、查询股份...\n")

nCategory = 1

status, content = client.QueryData(nCategory)
if status < 0:
    print("error: " + content)
else:
    print(content)

print("\n\t按任意键继续...\n")
msvcrt.getch()

#
#
#
print("\t5、查询可交易股票数量...\n")

nCategory = 0
nPriceType = 0
sAccount = ""
sStockCode = "000002"
fPrice = 3.11

status, content = client.GetTradableQuantity(
    nCategory, nPriceType, sAccount, sStockCode, fPrice)
if status < 0:
    print("error: " + content)
else:
    print(content)

print("\n\t按任意键继续...\n")
msvcrt.getch()

#
#
#
print("\t6、一键新股申购...\n")

status = client.QuickIPO()
if status < 0:
    print("error: " + str(status))
else:
    print("ok: " + str(status))

#
#
#
print("\t7、新股申购明细...\n")

status, content = client.QuickIPODetail()
if status < 0:
    print("error: " + content)
elif status == 0:
    print(content)
else:
    for elem in content:
        errinfo, result = elem
        if errinfo != "":
            print(errinfo)
        else:
            print(result)

print("\n\t按任意键继续...\n")
msvcrt.getch()

#
#
#
print("\t8、委托...\n")

status, content = client.SendOrder(0, 4, "p001001001005793", "601988", 0, 100)
if status < 0:
    print("error: " + content)
else:
    print(content)

print("\n\t按任意键继续...\n")
msvcrt.getch()

#
#
#
print("\t9、批量委托...\n")

status, content = client.SendOrders(
    ((0, 0, "p001001001005793", "601988", 3.11, 100), (0, 0, "p001001001005793", "601988", 3.11, 200)))
if status < 0:
    print(content)
else:
    for elem in content:
        errinfo, result = elem
        if errinfo != "":
            print(errinfo)
        else:
            print(result)

print("\n\t按任意键继续...\n")
msvcrt.getch()

#
#
#
print("\t10、查询五档行情...\n")

status, content = client.GetQuotes(('000001', '600600'))
if status < 0:
    print(content)
else:
    for elem in content:
        errinfo, result = elem
        if errinfo != "":
            print(errinfo)
        else:
            print(result)

print("\n\t按任意键继续...\n")
msvcrt.getch()

#
#
#
print("\t11、查询资金、持仓...\n")

Category = (0, 1, 3)

status, content = client.QueryDatas(Category)
if status < 0:
    print(content)
else:
    for elem in content:
        errinfo, result = elem
        if errinfo != "":
            print(errinfo)
        else:
            print(result)

print("\n\t按任意键继续...\n")
msvcrt.getch()

#
#
#
print("\t12、关闭服务器连接...\n")

del client
TradeX.CloseTdx()

#
#
#
print("\t按任意键退出...\n")

msvcrt.getch()
