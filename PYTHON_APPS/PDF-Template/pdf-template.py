from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')

pdf = FPDF(orientation='portrait',unit='mm',format='A4')
pdf.set_auto_page_break(auto=False,margin=0)

for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times',style='B',size=24)
    pdf.cell(w=0,h=12,txt=row['Topic'],align='L',ln=1)

    for line in range(22,288,10):
        pdf.line(10,line,200,line)

    pdf.ln(265)
    pdf.set_font(family='Times',style='i',size=12)
    pdf.cell(w=0,h=12,txt=row['Topic'],align='R')

    for i in range(0,row['Pages']-1):
        pdf.add_page()
        for line in range(22,288,10):
            pdf.line(10,line,200,line)

        pdf.ln(277)
        pdf.set_font(family='Times',style='i',size=12)
        pdf.cell(w=0,h=12,txt=row['Topic'],align='R')

pdf.output('PDF_bot.pdf')

