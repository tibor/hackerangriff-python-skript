#!/usr/bin/env python
# coding: utf8
import re
import io
with io.open("/SPD.txt", "r", encoding="utf-16") as file:
    lines= file.readlines()
for line in lines:
    mobil =""
    email =""
    count = re.search(r"^(\d+\.?\d?)\)", line.strip())
    if count:
        print count.group(0)
    name = re.search(r"^([A-Z][\wäöü\s-]+)$", line.strip(),re.UNICODE)
    if name:
        print name.group(0)
    mobil = re.search(r"(Mobil|01\d+).*", line.strip(),re.UNICODE)
    if mobil:
        print "x"
        print line
    email = re.search(r"^(E-?[Mm]ail|[\w\d]+@[\w\d]+\.\w+)$", line.strip(), re.UNICODE)
    if email:
        print "x"
        print line
