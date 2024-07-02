# csv 文件的读取

import csv

f1 = open("score.csv", mode="a", encoding="utf8")
cf = csv.writer(f1)
cf.writerow(["jack", "java", "100"])

