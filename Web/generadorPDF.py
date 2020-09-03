from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter,landscape
from reportlab.platypus import Table, Image
from reportlab.lib.units import inch
##add style
from reportlab.platypus import TableStyle
from reportlab.lib import colors
import Models2Consulta as consulta
datos= consulta.vista(0)
d = datos[1]
def generar_PDF(datos):
    img = "static/img/image.jpg"
    data = [
        ["Potenciómetro digital", "RPM", "Diferencia de voltaje" , "Voltaje" , "Tiempo" , "Diferencia de voltaje[in]" , "Voltaje[in]"]
    ]
    for i in datos:
        l = list(i)
        data.append(l)
    print(l)
    fileName = 'table.pdf'

    pdf = SimpleDocTemplate(
        fileName,
        pagesize =landscape(letter)
    )
    table = Table(data)
    """
    style = TableStyle([
        ##Starting Cell, Ending cell
        ('BACKGROUND',(0,0),(3,0), colors.green),
        ##Starting cell, Ending Cell = (-1,0)
        ('TEXTCOLOR',(0,0),(-1,0), colors.whitesmoke),
        ('ALIGN',(0,0),(-1,-1), 'CENTER'),
        ('FONTNAME',(0,0),(-1,0),'Courier-Bold'),
        ('BOTTOMPADDING',(0,0),(-1,0), 12),
        ('BACKGROUND',(0,1),(-1,-1), colors.beige)
    ])
    table.setStyle(style)
    #Alternative Backgroun color
    rowNumb = len(data)
    for i in range(1, rowNumb):
        if i%2==0:
            bc = colors.burlywood
        else:
            bc = colors.beige
        ts = TableStyle(
            [('BACKGROUND', (0,i),(-1,i),bc)]
        )
        table.setStyle(ts)
    ##Add Borders
    ts = TableStyle(
        [
            ('BOX', (0,0),(-1,-1),2,colors.black),
            ('LINEBEFORE', (2,1),(2,-1),2, colors.red),
            ('LINEABOVE',(0,2),(-1,2),2, colors.green),
            ('GRID', (0,1),(-1,-1),2,colors.black),
        ]
    )
    table.setStyle(ts)
    """
    imagen=Image(img, 4*inch, 4*inch)
    elems = []
    elems.append(table)
    elems.append(imagen)
    pdf.build(elems)
generar_PDF(d)