#coding: utf-8
import tushare as ts
import sys
import time
import os

# code = '000001'
code = sys.argv[1]
start_year = int(sys.argv[2])
end_year = int(sys.argv[3])


output_base_path = 'data/index/%s/' % code
if not os.path.exists(output_base_path):
    os.mkdir(output_base_path)
print 'output_base_path = ', output_base_path

for year in range(start_year, end_year+1):
    # 获取今年的数据时，end不允许超过今天的日期，否则返回空
    start_date = '%s-01-01' % year
    end_date = '%s-12-31' % year if year < int(time.strftime('%Y')) else time.strftime('%Y-%m-%d')
    print '[%s, %s]' % (start_date, end_date)

    output_csv = os.path.join(output_base_path, '%s.csv.gz' % year)

    year_data = ts.get_h_data(code, start=start_date, end=end_date, index=True, pause=2)
    if len(year_data) > 0:
        year_data.to_csv(output_csv, compression='gzip')
        print year, 'finish. save to %s' % output_csv
    else:
        print 'no %s data about %s' % (year, code)

