import xlsxwriter
import time
import shutil
import os
import pandas as pd
import sqlite3

def writer_report():  #officer
    workbook = xlsxwriter.Workbook('name_file.xlsx')
    worksheet = workbook.add_worksheet()

    my_list = [ID_card, Name ,Day, Date, Time,Arrival,Status]  #writehead
    for col_num, data in enumerate(my_list):
        worksheet.write(0, col_num, data)
    #ลูปลงข้อมูล


    #ลูปคำนวนStatus


def writer_daily():

    workbook = xlsxwriter.Workbook('name_file.xlsx')
    worksheet = workbook.add_worksheet()

    my_list = [ID_card, Name ,Day, Date, Time,Arrival,Depart,Office]  #writehead
    for col_num, data in enumerate(my_list):
        worksheet.write(0, col_num, data)



    workbook.close()
def writer_month():
    return

''''
def Excel_Daily(x ,camera_out):
    file_name = x + 'xlsx' #date
    workbook = xlsxwriter.Workbook('file_name')
    worksheet = workbook.add_worksheet()
    my_list = [[1, 1, 1, 1, 1],
           [2, 2, 2, 2, 1],
           [3, 3, 3, 3, 1],
           [4, 4, 4, 4, 1],
           [5, 5, 5, 5, 1]]
    for row_num, row_data in enumerate(my_list):
        for col_num, col_data in enumerate(row_data):
            worksheet.write(row_num, col_num, col_data)
    workbook.close()
    return 0
def Excel_month():
    return 0
'''
