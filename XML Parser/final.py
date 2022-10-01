import os
import xmltodict


RuleModule    = []
Name          = []
RuleCategory  = []
Summary       = []
Parameters     = []

for file in os.listdir('Rules'):
    with open(f'Rules/{file}', 'r') as f:
        xml = f.read()
        my_dict = dict(xmltodict.parse(xml))
        Rule = dict(dict(my_dict['COMPLETERULE'])['Rule'])
        # Rule_dict = {key: Rule[key] for key in Rule.keys() if key in ('@Name', '@Summary','@RuleCategory','@RuleModule',)}
        RuleModule.append(Rule['@RuleModule'])   
        Name.append(Rule['@Name'])         
        RuleCategory.append(Rule['@RuleCategory']) 
        Summary.append(Rule['@Summary'])                
        Parameter = dict(dict(my_dict['COMPLETERULE'])['Rule']['Parameter'])
        print("_________________________RULE_______________")
        print(Rule)
        print("_________________________PARAMETER______________")
        print(Parameter)
        Parameter_filtered = {key: Parameter[key] for key in Parameter.keys() if key in ('@Name', 'Operator','Value','@RuleModule',)}
        print("_________________________PARAMETER FILTERED______________")
        print(Parameter_filtered)
        Parameters.append(Parameter_filtered)
        print("_________________________NAME______________")
        print(Name)
        ("_________________________RuleModule______________")
        print(RuleModule)
        ("_________________________RuleCategory______________")
        print(RuleCategory)
        ("_________________________NAME______________")
        print
        ("_________________________Parameters______________")
        print(Parameters)

        
        break
        
        
    