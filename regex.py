import re

# todo open a file and count all classes and display their names

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
