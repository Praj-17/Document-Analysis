from inspect import Parameter
import xmltodict
import pprint
import json

my_xml = """
<Rule
    Name="Minimum Internal Corner Radius"
    Status="0"
    LifeStatus="1"
    Summary="Minimum corner radius on turned profile should be &gt;= 0.5 mm."
    Module="dfmturnrulesvalidator"
    RuleModule="Turn Rules"
    Severity="2"
    RuleCategory="Turning"
    RuleModuleFileName="dfmturnrulesu.dll"
    SelectedDatabase=""
    ><DataBases /><Parameter Name="Turn Corner Radius" Type="1038" Status="1"
      ><Operator>7</Operator><ParameterType>1</ParameterType
      ><Value>0.500000</Value><Remarks></Remarks></Parameter>
      </Rule>
      <Rule
    Name="Blind Hole Relief"
    Status="0"
    LifeStatus="1"
    Summary="Blind bored holes should be defined with tool relief at the end of the hole. The amount of relief should be &gt;= 0.03 times the Diameter of the Bored hole."
    Module="dfmturnrulesvalidator"
    RuleModule="Turn Rules"
    Severity="1"
    RuleCategory="Turning"
    RuleModuleFileName="dfmturnrulesu.dll"
    SelectedDatabase=""
    ><DataBases /><Parameter
      Name="Bore Relief(% of Bore Diameter)"
      Type="1041"
      Status="1"
      ><Operator>7</Operator><ParameterType>1</ParameterType
      ><Value>3.000000</Value><Remarks></Remarks></Parameter></Rule
  >

"""
print(type(my_xml))
my_dict = xmltodict.parse(my_xml)
dict=my_dict['Rule']
newdict = {key: dict[key] for key in dict.keys() if key in ('@Name', '@Summary','@RuleCategory','@RuleModule','Parameter')}
#ndict = newdict(['Rule']['Parameter'])
#pdict = {key: newdict[key] for key in newdict.keys() if key in ('@Name','@Operator','@Value')}
pdict = newdict['Parameter']
sdict = {key: pdict[key] for key in pdict.keys() if key in ('@Name','Operator','Value')}
#print(newdict)
print(sdict)  