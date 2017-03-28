#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlwt


def work_book():
    workbook = xlwt.Workbook(encoding = "ascii")
    worksheet = workbook.add_sheet("classmate")
    worksheet.write(0, 0, label = u"name")
    worksheet.write(0, 1, label = u"class")
    worksheet.write(1, 0, label =u"小白")
    worksheet.write(1, 1, label = u"高一班")
    worksheet.write(2, 0, label = u"小红")
    worksheet.write(2, 1, label = u"高一班")
    workbook.save("student.xls")

if __name__ == "__main__":
    work_book()