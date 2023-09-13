import docx
#opening the file
doc = docx.Document('SergioAndrésHerrera Velásquez_Anexo_guia_aap1.docx')
print('Document Object:', doc)


#getting info out of the doc
print('Title of the document')
print(doc.paragraphs[1].text)

#attributes of the doc

print('Attributes of the document')
print('Author:',doc.core_properties.author)
print('Date Created:',doc.core_properties.created)
print('Document Revision',doc.core_properties.revision)

#reading tables

table=doc.tables[0]
print(table)
print('Column 1')
for i in range(len(table.rows)):
    print(table.rows[i].cells[0].paragraphs[0].text)
    

print('Column 2')
for i in range(len(table.rows)):
    print(table.rows[i].cells[1].paragraphs[0].text)
    
#writing data into  word Document(Adding headings, images,tables)
from docx import Document
document=Document()
document.add_heading('Test Document from Docs',0)
document.save('testdoc.docx')
    
