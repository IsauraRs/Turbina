from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter,landscape
from reportlab.platypus import Table, Image
from reportlab.lib.units import inch
import PIL
##add style
from reportlab.platypus import TableStyle
from reportlab.lib import colors
import Models2Consulta as consulta
from datetime import date
datos= consulta.vista(99)
d = datos[1]
def generar_PDF(datos):
    style = ParagraphStyle(
        name='Normal',
        fontSize=10,
    )

    img = "static/img/image.jpg"
    img1 = "static/img/imageEfmotor.jpg"
    img2 = "static/img/imageEfTurbina.jpg"
    data = [
        ["Potenciómetro digital", "RPM", "Diferencia de voltaje" , "Voltaje" , "Tiempo" , "Diferencia de voltaje[in]" , "Voltaje[in]"]
    ]
    for i in datos:
        l = list(i)
        data.append(l)
        print(l)
    fileName = 'table.pdf'
    #
    par = Paragraph('Reporte con fecha ' +str(date.today()),style)

    pdf = SimpleDocTemplate(
        fileName,
        pagesize =landscape(letter)
    )
    table = Table(data)
    table.setStyle(TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue),
('TEXTCOLOR',(1,1),(-2,-2),colors.black),
('VALIGN',(0,0),(0,-1),'TOP'),
('TEXTCOLOR',(0,0),(0,-1),colors.black),
('ALIGN',(0,-1),(-1,-1),'CENTER'),
('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
('TEXTCOLOR',(0,-1),(-1,-1),colors.black),
('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
('BOX', (0,0), (-1,-1), 0.25, colors.black),
]))
    
    
    imI = Image("static/img/logoFinal.png" , 10*inch , 1*inch)
    #imI.hAlign = 'RIGHT'
    imagen=Image(img, 10*inch, 6*inch)
    imagen1=Image(img1, 10*inch, 6*inch)
    imagen2=Image(img2 , 10*inch , 6*inch)
    elems = []
    elems.append(imI)
    elems.append(par)
    elems.append(table)
    elems.append(imagen)
    elems.append(imagen1)
    elems.append(imagen2)
    #elems.append(imI)
    pdf.build(elems)

generar_PDF(d)