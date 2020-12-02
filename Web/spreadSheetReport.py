from openpyxl import load_workbook
from openpyxl.drawing.image import Image

inData = []
headersL = []

filesheet = "ReporteSpreadsheet.xlsx"
wb = load_workbook(filesheet)
#datos = obtener_etiquetas(an2.ciudades,an2.edad_por_grupos,an2.sexo,an2.nse, an2.marcas)
sheet = wb.active

logos = Image("static/img/logoSS.png")
sheet.add_image(logos,'A1')

def getHeaders():
    A1 = sheet['A5'].value
    B1 = sheet['B5'].value
    C1 = sheet['C5'].value
    D1 = sheet['D5'].value
    E1 = sheet['E5'].value
    F1 = sheet['F5'].value
    G1 = sheet['G5'].value
    H1 = sheet['H5'].value
    I1 = sheet['I5'].value
    J1 = sheet['J5'].value

    headersL = ['A1','B1','C1','D1','E1','F1','G1','H1','I1','J1']

def setData(data):
    for i in data:
        inData.append(i)
        for t in inData:
            s = [headersL,t]
            
            #for r in s:
            #    sheet.append(r)
    sheet.append(s[0])
    sheet.append(s[1])

    print("data",inData)
    wb.save(filesheet)
#getHeaders()
'''s = [headersL,
    (1,2,3,4,5,6,7,8,9,10)]'''
#p = [1,2,3,4,5,6,7,8,9,10]
#setData(p)

