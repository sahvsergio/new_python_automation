
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
from pptx import Presentation
prs=Presentation()
slide=prs.slides.add_slide(prs.slide_layouts[0])
slide.shapes.title.text='Yo, Python'
slide.placeholders[1].text='Yes, it is really awesome'
prs.save('yoPython.pptx')

"""We can also create a new presentation from an existing presentation. 
In the next code example, we take a PowerPoint template, create a new PPT, 
and add a slide to it with text content. We use the following template for this example:"""

from pptx import Presentation 
prs = Presentation('yoPython.pptx') 
 
first_slide = prs.slides[0] 
first_slide.shapes[0].text_frame.paragraphs[0].text = "Hello!" 
 
slide = prs.slides.add_slide(prs.slide_layouts[1]) 
text_frame = slide.shapes[0].text_frame 
p = text_frame.paragraphs[0] 
p.text = "This is a paragraph" 
 
prs.save('new_ppt.pptx')
# Playing with layouts, placeholders, and textboxes

from pptx import Presentation
prs=Presentation()
two_content_slide_layout=prs.slide_layouts[3]
slide=prs.slides.add_slide(two_content_slide_layout)
shapes=slide.shapes
title_shape=shapes.title
title_shape.text='Adding A two content slide'


body_shape=shapes.placeholders[1]
tf=body_shape.text_frame    
tf.text='This is line 1'

p=tf.add_paragraph()
p.text='Again a line 2'
p.level=1

p=tf.add_paragraph()
p.text='And this is line 3 ...'
p.level=2

prs.save('two_content.pptx')
# Working with different shapes and adding tables
# Visual treat with pictures and charts
# Automating weekly sales reports
