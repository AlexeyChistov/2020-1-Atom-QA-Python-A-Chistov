#!/bin/bash


path="$1"
if [[ -f "$path" ]]; then
  echo "Correct path"
elif  [[ -d "$path" ]]; then
  echo "Correct dir"
  path=$path*.log
else
  echo "No file or dir"
fi

{
#  общее количество запросов
  cat $path | wc -l


#  количество запросов
  cat $path | awk '$6~/"POST|"GET|"DELETE|"PUT|"HEAD|"CONNECT|"OPTIONS|"TRACE|"PATH/ {print($6)}'| sort | uniq -c | sort -nr


#  самые большие запросы
  cat $path | awk '{print($10, $7)}' | sort -nr | uniq -c | head -n 10
  echo "400"

#  поиск по топу количеств запросов с 400-ми ошибками
 cat $path | awk '{print($1,$7,$9)}' | grep '\s4[0-9][0-9]' | sort | uniq -c | sort -nr| head -n 10
  echo "500"

#  поиск по топу количеств запросов с 500-ми ошибками
  cat $path | awk '{print($1,$7,$9)}' | grep -E '\s5[0-9][0-9]' | sort | uniq -c | sort -nr | head -n 10
} > results.txt
