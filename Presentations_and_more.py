
# Reading PowerPoint presentations
from pptx import Presentation

path_to_presentation = 'Función empresarial.pptx'
# presentation object
prs = Presentation(path_to_presentation)
print('Presentation object for Funcion Empresarial:', prs)
print('*'*100)
# slides object
print('Slides are :')
for slide in prs.slides:
    print('slide object:', slide)
    
print('slide has the following objects')
slide1, slide2=prs.slides[0],prs.slides[1]
print('Slides ids:\n',slide1.slide_id,',',slide2.slide_id)
print('Slide Open XML elements:\n',slide1.element,',',slide2.element)
print('Slide Layouts: \n',slide1.slide_layout.name,slide2.slide_layout.name )
print('Shapes in the slides')
i=1
for slide in prs.slides:
    print(slide, i)
    for shape in slide.shapes:
        print('Shape:',shape.shape_type)
    i+=1

text_runs=[]
for slide in prs.slides:
    for shape in slide.shapes:
        if not shape.has_text_frame:
            continue
        for paragraph in shape.text_frame.paragraphs:
            for run in paragraph.runs:
                text_runs.append(run.text)
            
print('The text is:',text_runs)
            
            


# Creating and updating presentations, and adding slides
# Playing with layouts, placeholders, and textboxes
# Working with different shapes and adding tables
# Visual treat with pictures and charts
# Automating weekly sales reports
