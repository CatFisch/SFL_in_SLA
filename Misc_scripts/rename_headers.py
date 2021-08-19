#!/usr/bin/env python3

#Copyright 2021 Catharina Fischer

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at

    #http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.


import glob
import os
import openpyxl

excel_files = glob.glob(os.getcwd() + '/*.xlsx')

for excel in excel_files:
    wb = openpyxl.load_workbook(filename=excel, read_only=False, data_only=True)
    ws = wb.worksheets[0]

    for rows in ws.iter_rows(min_row=1, max_row=1, min_col=1):
        for cell in rows:
            names=cell.value
            if names == 'ZH1:ZH1':
                cell.value = 'ZH1'
            if names == 'ZH1:ZH1pos':
                cell.value = 'ZH1pos'
            if names == 'ZH1:ZH1lemma':
                cell.value = 'ZH1lemma'
    wb.save(excel)




