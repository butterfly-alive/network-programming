"""
1.创建数据库dict(utf8)
2.创建数据表words，将单词和单词解释分别存入不同字段
3.将单词存入words单词表 超过19500 即可
"""
import pymysql
import re


db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')
cur = db.cursor()
f = open("dict.txt")
# for line in f:
#     temp = line.split(" ")
#     word = temp[0]
#     explain = " ".join(temp[1:]).strip()
#     sql = "insert into words (word,explian) values (%s,%s)"
#     cur.execute(sql, [word,explain])
for line in f:
    tup = re.findall(r"(\S+)\s+(.*)", line)[0]
    # print(tup)
    sql = "insert into words (word,explian) values (%s,%s)"
    try:
        cur.execute(sql,tup)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
f.close()
cur.close()
db.close()



