from bs4 import BeautifulSoup
import xmltodict
with open("SampleRules.xml", "r") as f:
    data= f.read()
    print(type(data))
    #print(data)
soup = BeautifulSoup(data, 'xml')
Rules = soup.find_all('COMPLETERULE')
# Parametes = soup.find_all('Parameter')
print(Rules[0])
for id, rule in enumerate(Rules):
    with open(f'Rules/Rule-{id}.xml', 'w+') as f:
        f.write(str(Rules[id]))
     
# my_dict = xmltodict.parse(Rules[0])
# print(my_dict)