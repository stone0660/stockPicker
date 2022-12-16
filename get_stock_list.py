from urllib import request
import pandas as pd
from io import StringIO

#Download A-Stock stock list

# sse_stock_list_url = 'http://query.sse.com.cn/security/stock/downloadStockListFile.do?csrcCode=&stockCode=&areaName=&stockType=1'
# request_headers = {'X-Requested-With': 'XMLHttpRequest',
#                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/56.0.2924.87 Safari/537.36',
#                    'Referer': 'http://www.sse.com.cn/assortment/stock/list/share/'
#                   }

# req = request.Request(sse_stock_list_url, headers=request_headers)
# resp = request.urlopen(req)
# result = resp.read().decode('gb2312')#please use gb2312 to decode otherwise you will not get correct data

# TESTDATA = StringIO(result)
# df = pd.read_csv(TESTDATA, sep='\t')
# print(df)

# import akshare as ak
# stock_info_a_code_name_df = ak.stock_info_a_code_name()
# print(stock_info_a_code_name_df)

import akshare as ak
stock_info_sh_df = ak.stock_info_sh_name_code(indicator="主板A股")
# stock_info_sz_df = ak.stock_info_sz_name_code(indicator="A股列表")
# print(stock_info_sz_df)
print(stock_info_sh_df)