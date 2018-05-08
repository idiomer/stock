#!/bin/bash

index_codes="000001 000300 399001"

thisyear=`date +%Y`

for code in ${index_codes}; do
    python get_index_hist_data.py $code $thisyear $thisyear
done


# crontab
# 00 17 * * * cd ${work_dir} && bash update_index.sh  # 必须15点后运行
