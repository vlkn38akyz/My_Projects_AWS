#! /bin/bash
cat event_history.csv | grep -i serdar |grep -i terminate| cut -d"[" -f2 | cut -d"]" -f1| cut -d":" -f7| cut -d"}" -f1 |sort |uniq|tee serdar1

cat event_history.csv | grep -i serdar |grep -i terminate| cut -d"[" -f2|cut -d"]" -f1| cut -d"}" -f2|cut -d":" -f7|sort| uniq|tee serdar2

cat serdar2 >> serdar1

cat serdar1 |sort |uniq| nl | tee serdar3

rm -r serdar1 serdar2


