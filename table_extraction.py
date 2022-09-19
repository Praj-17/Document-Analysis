import camelot

# PDF file to extract tables from
file = "Design-Guidelines.pdf"
tables = camelot.read_pdf(file)
# number of tables extracted
print("Total tables extracted:", tables.n)