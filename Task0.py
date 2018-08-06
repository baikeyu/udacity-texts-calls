# -*- coding:utf8 -*-
"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


def first_text_record(texts):
    record = list(texts[0])
    return record


def last_call_record(calls):
    record = list(calls[-1])
    return record


texts_record = first_text_record(texts)
calls_record = last_call_record(calls)

print ("First record of texts, {} texts {} at time {}".format(texts_record[0], texts_record[1], texts_record[2]))
print ("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(calls_record[0], calls_record[1],
                                                                                 calls_record[2], calls_record[3]))
