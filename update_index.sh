#!/bin/bash

# 上证指数 / 深证成指 / 沪深300 / 中证500
index_codes="000001 399001 000300 000905"

thisyear=$1
thisyear=${thedate:-`date +%Y`}

for code in ${index_codes}; do
    python3 get_index_hist_data.py $code $thisyear $thisyear
done


# crontab
# 00 17 * * * cd ${work_dir} && bash update_index.sh  # 必须15点后运行
