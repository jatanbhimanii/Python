from fpdf import FPDF
  
pdf = FPDF()
pdf.add_page()
  
pdf.set_font("Arial", size = 15)
  
pdf.cell(200, 10, txt = "Name: Jatan Bhimani",ln = 1, align = 'C') 
pdf.cell(200, 10, txt = "ID: 20CE007",ln = 2, align = 'C')
pdf.cell(200, 10, txt = "Practical 10",ln = 4, align = 'C')
pdf.cell(200, 10, txt = "RESULT",ln = 6, align = 'C')
pdf.cell(200, 10, txt = "CA224 Introduction to web designing                AA",ln = 7, align = 'C')
pdf.cell(200, 10, txt = "CE244 SGP-I                                        AA",ln = 8, align = 'C')
pdf.cell(200, 10, txt = "CE251 Java Programming                             AA",ln = 9, align = 'C')
pdf.cell(200, 10, txt = "CE251 Java Programming(Practical)                  AA",ln = 10, align = 'C')
pdf.cell(200, 10, txt = "CE252 Digital Electronics                          AB",ln = 11, align = 'C')
pdf.cell(200, 10, txt = "CE252 Digital Electronics(Practical)               BB",ln = 12, align = 'C')
pdf.cell(200, 10, txt = "CE257 Data Communicatons & Networking              AA",ln = 13, align = 'C')
pdf.cell(200, 10, txt = "CE257 Data Communicatons & Networking(Practical)   AA",ln = 14, align = 'C')
pdf.cell(200, 10, txt = "HS121 Creativity,Problem Solving & Innovative      AA",ln = 15, align = 'C')
pdf.cell(200, 10, txt = "MA253 Discrete Mathematics & Algebra               AA",ln = 16, align = 'C')
pdf.cell(200, 10, txt = "CGPA: 9.70         SGPA:9.79",ln = 18, align = 'C')

  
pdf.output("20CE007_Practical_10.pdf") 