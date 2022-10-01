from inspect import Parameter
import xmltodict
import pprint
import json

import xml.etree.ElementTree as ET

with open("SampleRules.xml", "r") as f:
    data= f.read()
    print(type(data))
    #print(data)


tree = ET.parse('SampleRules.xml')
root = tree.getroot()
print(root)

for i in range(0,len(root)):
    _, _, roottag = root[i].tag.rpartition('}')
    for ele in root[i].getiterator():
        _, _, tag = ele.tag.rpartition('}')
        print(str(tag)+"("+str(roottag)+str(i)+")")