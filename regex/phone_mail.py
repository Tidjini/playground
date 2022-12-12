import re
import pyperclip

sep = r"[\s.-_]?"
prfx = r"(0|\+213|\(\+213\))"
number = r"(\d\d)"
p = f"{prfx}{sep}(\d\d\d){sep}{number}{sep}{number}{sep}{number}"

phone_po = re.compile(p)


mo = phone_po.search("(+213)55994 2372")

if mo:
    print(mo.groups())
