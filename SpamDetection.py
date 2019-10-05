#file porbo
import xlrd
loc = ("C:/Users/noshi\PycharmProjects\SpamDetection\SpamDetection\SpambaseDataset.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)

#column count korbo
numOfColumns=sheet.ncols
print(numOfColumns)

numOfRows=sheet.nrows
print(numOfRows)

pSpamList=[]
pHamList=[]
#per column er jonno
for columnCount in range (0,numOfColumns-1):
    spam=0
    ham=0
    spamWord=0.0
    hamWord=0.0
    for rowCount in range (0,numOfRows):
        #1 for spam, 0 for non-spam
        if sheet.cell_value(rowCount,numOfColumns-1)==1:
            spamWord+=sheet.cell_value(rowCount,columnCount)
            spam+=1
        elif sheet.cell_value(rowCount,numOfColumns-1)==0:
            hamWord+=sheet.cell_value(rowCount,columnCount)
            ham+=1

    #jegulay spam oigular freq sum kora lagbe
    #jegulay ham oigular freq sum kora lagbe

    pSpam=(spamWord/spamWord+hamWord)/((spamWord/spamWord+hamWord)+(hamWord/spamWord+hamWord))
    pHam=(hamWord/spamWord+hamWord)/((spamWord/spamWord+hamWord)+(hamWord/spamWord+hamWord))

    #p = p(w/s)/[p(w/s)+p(w/h)] ei formulay per column er p ber kora lagbe
    #p gula ekta p er list e store korte hobe

    pSpamList.append(pSpam)
    pHamList.append(pHam)
    #print(pHam)

#shbgula p gun korte hobe

resultSpam=1.0
resultHam=1.0

locationInput = ("C:/Users/noshi\PycharmProjects\SpamDetection\SpamDetection\input.xlsx")

wb2 = xlrd.open_workbook(locationInput)
sheet2 = wb2.sheet_by_index(0)

sheet2.cell_value(0, 0)

#column count korbo
numOfInpCol=sheet2.ncols
print(numOfInpCol)

numOfInpRows=sheet2.nrows
print(numOfInpRows)

print(len(pSpamList))
for inp in range (0,numOfInpRows):
    for inpCol in range(0,numOfInpCol-1):
        if sheet2.cell_value(inp,inpCol)!=0:
            resultSpam=resultSpam*pSpamList[inpCol]
            resultHam=resultHam*pHamList[inpCol]


print("resultSpam: ")
print(resultSpam)

print("resultHam: ")
print(resultHam)

if resultHam>resultSpam:
    print("Not a Spam!")
else:
    print("Spam!!!")
