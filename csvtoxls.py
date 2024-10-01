import os
import glob
import csv
from xlsxwriter.workbook import Workbook
from pathlib import Path
import datetime

pathsearch = os.path.join('.', '*.csv')
#pathsearch = "C:/Users/Enduro/Documents/ctoksm/vvodvoborot/auto/xcsvtoxls/**/*.csv"
pathsearch = "**/*.csv"
current_date = datetime.datetime.now().strftime("%d%m")
pathsearch = f"C:/Users/Enduro/Documents/ctoksm/vvodvoborot/{current_date}/**/*.csv"
print(pathsearch)
counnsfilespocessed = 0
previusdir = ""
countdirprocessed = 0
for csvfile in glob.glob(pathsearch, recursive=True):
    #print(csvfile)
    #print(Path(csvfile).parent)
    currdir = Path(csvfile).parent
    #print("previud=", previusdir)
    #print("currdir=", currdir)
    if currdir!=previusdir:
        previusdir = currdir
        countdirprocessed = countdirprocessed +1
    #print(currdir)
    dirxls = os.path.join(currdir, "xls")
    #print(dirxls)
    Path(dirxls).mkdir(parents=True, exist_ok=True)
    newnamexls = Path(csvfile).stem
    #print(newnamexls)
    fullnamenewbook = os.path.join(dirxls, newnamexls + '.xlsx')
    #print(fullnamenewbook)
    counnsfilespocessed = counnsfilespocessed + 1
    #continue
    workbook = Workbook(fullnamenewbook)
    worksheet = workbook.add_worksheet()
    with open(csvfile, 'rt', encoding='utf8') as f:
        r = 0
        #print(csvfile)
        for line in f:
            val = line.split(chr(29),1)
            worksheet.write(r, 0, val[0])
            r=r+1
        #reader = csv.reader(f, delimiter="")
        #for r, row in enumerate(reader):
        #    for c, col in enumerate(row):
        #        val = col.split(chr(29),1)
        #        worksheet.write(r, c, val[0])
    workbook.close()
    counnsfilespocessed = counnsfilespocessed + 1
print("Всего писем обработано ", countdirprocessed)
print("Всего обработано файлов ", counnsfilespocessed)