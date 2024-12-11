from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="letter")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="l", ln=1)
    pdf.line(10, 22, 205, 22, )
    pdf.set_text_color(200, 200, 200)
    for i in range(24):
        adding_num = (i+1)*10
        pdf.ln(adding_num)
        pdf.line(10, 22+adding_num, 205, 22+adding_num)
    for i in range(row["Pages"]-1):
        pdf.add_page()
        for i in range(24):
            adding_num = (i + 1) * 10
            pdf.ln(adding_num)
            pdf.line(10, 12 + adding_num, 205, 12 + adding_num)


pdf.output("output.pdf")