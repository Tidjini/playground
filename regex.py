import re

# todo open a file and count all classes and display their names
# todo detect inhereted one
# todo get commented one
# todo agents example CENSERD one in Text
# todo CENSERD some private classes


identifier = 'class'
# must start with letter
name = r'[a-zA-Z]\w+'
# can be : module, module.other.third ...
parent = rf'{name}(.{name})*'

class_pattern = re.compile(
    rf'{identifier}\s+({name})(\(\s*{parent}\s*(,\s*{parent})*\))?:')
matched = class_pattern.search('class Model:')

if matched:
    print(matched.group(1))
else:
    print('Not Matched')


# for testing
p = re.compile(r'^\d+\d+$')
mo = p.search('15245465')

if mo:
    print(mo.group())


# todo anything first name : ...... last name : ......


po = re.compile(r'<.*>')
mo = po.search('<first:tidjini_first:messa>daonizaodnaiozdn>')
if mo:
    print(mo.group())
