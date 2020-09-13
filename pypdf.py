from fpdf import FPDF
import datetime

pdf = FPDF()

pdf.add_page()

"""
pdf.set_font("Arial" , size= 15)

pdf.cell(200, 10 , txt = "Kangemi Hospital" , ln = 1 , align = 'C')

pdf.cell(200, 10 , txt = "Waroko Clinic" , ln = 2 , align = 'C')

pdf.output("rendered.pdf")


pdf.cell(40,10,'Drug Name ' ,4 , 0)
pdf.cell(40,10,'Quantity ' , 4, 0)

pdf.cell(40,10,'Price ' ,4 , 0)
pdf.cell(40,10,'Total Price ' ,4 , 0)
pdf.cell(40,10,'Payment Method ' ,4 , 0)
"""
pdf.set_font("Times"  ,size= 15)

pdf.cell(200, 10 , txt = "CARELINK  Hospital" , ln = 1 , align = 'C')
pdf.cell(200, 10 , txt = "AT Mzee Juma's Flats " , ln = 2 , align = 'C')
pdf.cell(200, 10 , txt = "Near Kangemi Memorial Park -  WARUKU" , ln = 3 , align = 'C')
pdf.cell(200, 10 , txt = "P.O Box 14496-00800" , ln = 4 , align = 'C')
pdf.cell(200, 10 , txt = "Nairobi" , ln = 5 , align = 'C')
pdf.cell(200, 10 , txt = "Tell : 0727546794" , ln = 6 , align = 'C')

pdf.set_font("Times"  ,'B' ,size= 15)
pdf.cell(200, 10 , txt = "TILL" , ln = 7 , align = 'C')

pdf.set_font("Times" , 'B' ,size= 15)

pdf.cell(200, 10 , txt = " PH00001 " , ln = 8 , align = 'L')
pdf.cell(200, 10 , txt = " Date : {} ".format(datetime.date.today()) , ln = 9 , align = 'L')



pdf.set_font("Times" , 'B' ,size= 15)

pdf.cell(40,10,'Drug Name ' ,2 , 0)
pdf.cell(40,10,'Quantity ' , 2, 0)
pdf.cell(40,10,'Price ' ,2, 0)
pdf.cell(40,10,'Total' ,2 , 0)


pdf.set_font("Times"  ,size= 15)
pdf.cell(40,10,'' ,2 , 1)
pdf.cell(40,10,'Quantity ' , 2, 0)
pdf.cell(40,10,'Price ' ,2, 0)
pdf.cell(40,10,'Total' ,2 , 0)

pdf.cell(40,10,'' ,2 , 1)
pdf.cell(40,10,'Quantity ' , 2, 0)
pdf.cell(40,10,'Price ' ,2, 0)
pdf.cell(40,10,'Total' ,2 , 0)

pdf.cell(40,10,'' ,2 , 1)
pdf.cell(40,10,'Quantity ' , 2, 0)
pdf.cell(40,10,'Price ' ,2, 0)
pdf.cell(40,10,'Total' ,2 , 0)











pdf.output('render.pdf', 'F')
