import os
import sys
import time
import struct
import datetime

sz_day_path = r"C:\fzzq\小方\vipdoc\sz\lday"
sh_day_path = r"C:\fzzq\小方\vipdoc\sh\lday"

path = r"F:\workspace\stockPicker\testData"
dayFiles = os.listdir(path)
loctime = time.localtime(time.time())
today = time.strftime("%Y%m%d", loctime)  # 无运行参数，则默认为当天（样式为YYYYMMDD,如20220301）

txtfile = os.path.join(path, today+".txt")  # 输出文本文件名

for dfn in dayFiles:
    if ".day" in dfn:
        (short_name, extension) = os.path.splitext(dfn)
        txt_file = os.path.join(path, short_name+today+".txt")  # 输出文本文件名
        tf = open(txt_file,"a+")
        with open(os.path.join(path, dfn), 'rb') as f:
            m = 0
            d = 0
            while True:
                try:
                    buf = f.read(32)
                    record = struct.unpack('IIIIIfII', buf)
                    # print record
                    if record[5] > m:
                        m = record[5]
                        r = buf
                except:
                    break
                
            #     stock_date = f.read(4)
            #     stock_open = f.read(4)
            #     stock_high = f.read(4)
            #     stock_low = f.read(4)
            #     stock_close = f.read(4)
            #     stock_amount = f.read(4)
            #     stock_vol = f.read(4)
            #     # date,open,high,low,close,amount,vol,reservation
            #     stock_reservation = f.read(4)
            #     if not stock_date:
            #         break

            #         # 4字节如20091229
            #     stock_date = struct.unpack("l", stock_date)
            #     #开盘价*100
            #     stock_open = struct.unpack('I', stock_open)
            #     #最高价*100
            #     stock_high = struct.unpack('I', stock_high)
            #     #最低价*100
            #     stock_low = struct.unpack('I', stock_low)
            #     #收盘价*100
            #     stock_close = struct.unpack('I', stock_close)
            #     #成交额
            #     stock_amount = struct.unpack('I', stock_amount)
            #     #成交量
            #     stock_vol = struct.unpack('I', stock_vol)
            #     #保留值
            #     stock_reservation = struct.unpack("l", stock_reservation)
            #     #格式化日期
            #     date_format = datetime.datetime.strptime(
            #         str(stock_date[0]), '%Y%M%d')
            #     list = date_format.strftime('%Y-%M-%d') + "," + str(stock_open[0]/100)+","+str(stock_high[0]/100.0) + "," + str(stock_low[0]/100.0)+","+ str(stock_close[0]/100.0)+"," + str(stock_vol[0])+"\n"
            #     tf.writelines(list)
            tf.close()

print("文件输出完毕！")
