from reportlab.pdfgen import canvas

# Cria um novo arquivo PDF
pdf = canvas.Canvas("relatorio.pdf")

# Insere texto no arquivo PDF
pdf.drawString(100, 750, "Relatório Geral")
pdf.drawString(100, 700, "Nome: João")
pdf.drawString(100, 650, "Idade: 30")

# Salva e fecha o arquivo PDF
pdf.save()