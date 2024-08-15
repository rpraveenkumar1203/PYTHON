import pandas as pd 
from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob('Data/*.xlsx')

for filepath in filepaths :
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    pdf = FPDF(orientation = 'P',unit ='mm', format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_Number, invoice_Date = filename.split('-')
    #print(invoice_Number, invoice_Date )
    pdf.set_font(family = 'Times',size=16,style='B')
    pdf.cell(w=0,h=12,txt = f"Invoice Number : {invoice_Number}",align = 'L',ln=1)
    pdf.cell(w=0,h=12,txt = f"Invoice Date   : {invoice_Date}",align = 'L',ln=1)

    columns = list(df.columns)
    columns = [item.replace('_',' ').title() for item in columns]
    #print(columns)

    pdf.set_font(family = 'Times',size = 12 ,style='B')
    pdf.cell(w=30,h=8,txt=columns[0],align ='C',border =1)
    pdf.cell(w=50,h=8,txt=columns[1],align ='C',border =1)
    pdf.cell(w=50,h=8,txt=columns[2],align ='C',border =1)
    pdf.cell(w=30,h=8,txt=columns[3],align ='C',border =1)
    pdf.cell(w=30,h=8,txt=columns[4],align ='C',border =1,ln=1)

    for index ,rows in df.iterrows():
        #print(rows)
        pdf.set_font(family = 'Times',size = 12)
        pdf.cell(w=30,h=8,txt=str(rows['product_id']),align ='C',border =1)
        pdf.cell(w=50,h=8,txt=str(rows['product_name']),align ='C',border =1)
        pdf.cell(w=50,h=8,txt=str(rows['amount_purchased']),align ='C',border =1)
        pdf.cell(w=30,h=8,txt=str(rows['price_per_unit']),align ='C',border =1)
        pdf.cell(w=30,h=8,txt=str(rows['total_price']),align ='C',border =1,ln =1)
    
    pdf.set_font(family = 'Times',size = 12,style = 'B')
    pdf.cell(w=30,h=8,txt="",align ='C',border =1)
    pdf.cell(w=50,h=8,txt="",align ='C',border =1)
    pdf.cell(w=50,h=8,txt="",align ='C',border =1)
    pdf.cell(w=30,h=8,txt="Grand Total",align ='C',border =1)
    pdf.cell(w=30,h=8,txt=str(df['total_price'].sum()),align ='C',border =1,ln=1)

    pdf.set_font(family = 'Times',size = 16,style = 'B')
    pdf.set_text_color(0,200,0)
    pdf.cell(w=50,h=8,txt="",align ='C',ln =1)
    pdf.cell(w=30,h=8,txt=f"The total amount of the bill is {int(df['total_price'].sum())} rupees ",align ='L',ln=1)

    # pdf.ln(180)
    pdf.set_text_color(0,0,0)
    pdf.set_font(family = 'Times',size = 16,style = 'B')
    pdf.cell(w=50,h=8,txt='PKR_enterprises',align = 'C')
    pdf.image('logo/OIP.jpeg',w=10)
    
    pdf.output(f"invoice_pdf/{filename}.pdf")


