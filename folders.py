import os
titles = ['Title1', 'Title2', 'Title3']
for title in titles:
    os.mkdir('Content/' + title)
    os.chdir('Content/' + title)
    
text1 =data['page1']['title2']['image']
