import docx

document = docx.Document('1.docx')

def iter_headings(paragraphs):
    for paragraph in paragraphs:
        print(paragraph.text)
        if paragraph.style.name.startswith('Normal'):
            print(paragraph)
            yield paragraph
for heading in iter_headings(document.paragraphs):
    print (heading.text)