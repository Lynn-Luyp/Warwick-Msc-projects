 
import openpyxl
import os 
os.chdir(r'C:\Users\Perry_Lu\Desktop\ebm\正课\课程\DDSC\python')
import pandas as pd

wb = openpyxl.load_workbook("machine_data_for_student_4.xlsm")

sheet = wb['machines']

sheet['A1'].value = 'rrrrr'


wb.save('machine_data_for_student_4.xlsm')
#workbook=xlrd.open_workbook("改machine_data_for_student_4.xlsx")  #文件路径
 
 