import os
import xmltodict
for file in os.listdir('Rules'):
    with open(f'Rules/{file}', 'r') as f:
        xml = f.read()
        my_dict = dict(xmltodict.parse(xml))
        Rule = dict(dict(my_dict['COMPLETERULE'])['Rule'])
        Parameter = dict(dict(my_dict['COMPLETERULE'])['Rule']['Parameter'])
        break
        
        
    