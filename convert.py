import os
import subprocess

import glob
import win32com.client
import os

word = win32com.client.Dispatch("Word.Application")
word.visible = 0

pdfs_path = "E:\CODING PLAYGROUND\CODE\DFMPro\\" # folder where the .pdf files are stored
for i, doc in enumerate(glob.iglob(pdfs_path+"*.pdf")):
    print(doc)
    filename = doc.split('\\')[-1]
    in_file = os.path.abspath(doc)
    print(in_file)
    wb = word.Documents.Open(in_file)
    out_file = os.path.abspath("E:\CODING PLAYGROUND\CODE\DFMPro\\" +filename[0:-4]+ ".docx".format(i))
    print("outfile\n",out_file)
    wb.SaveAs2(out_file, FileFormat=16) # file format for docx
    print("success...")
    wb.Close()

word.Quit()