#!/usr/bin/python

import requests
import urllib.parse # added for python 3
import xml.etree.ElementTree as xmlET



# Make up a text block
text_block = "PH-1 41.3567 -70.7348 91 std 4.5 2.70 1.0000 8.00e-05 123500 3700 KNSTD 712400 31200 KNSTD"

# Form URL
url = ("http://hess.ess.washington.edu/cgi-bin/matweb/?mlmfile=al_be_age_many_v22_ws&" \
    + "text_block=" + urllib.parse.quote(text_block) \
    + "&P10_St=3.93089&delP10_St=0.18857" \
    + "&P10_Lm=3.87397&delP10_Lm=0.18737")

s = requests.Session()
r = s.get(url)

# Read response
for i in range(1,383135):
    r = s.get(url)
    print(i)

# Parse XML
tree = xmlET.fromstring(r.text)

# Print results
print("t10St (yr) = ", tree.findall("./exposureAgeResult/t10St")[0].text, \
    " +/- ", tree.findall("./exposureAgeResult/delt10_int_St")[0].text, \
    " (", tree.findall("./exposureAgeResult/delt10_ext_St")[0].text, ")\n")
print("t26St (yr) = ", tree.findall("./exposureAgeResult/t26St")[0].text , \
    " +/- ", tree.findall("./exposureAgeResult/delt26_int_St")[0].text, \
    " (", tree.findall("./exposureAgeResult/delt26_ext_St")[0].text, ")\n")
print("t10Lm (yr) = ", tree.findall("./exposureAgeResult/t10Lm")[0].text, \
    " +/- ", tree.findall("./exposureAgeResult/delt10_int_Lm")[0].text, \
    " (", tree.findall("./exposureAgeResult/delt10_ext_Lm")[0].text, ")\n")
print("t26Lm (yr) = ", tree.findall("./exposureAgeResult/t26Lm")[0].text, \
    " +/- ", tree.findall("./exposureAgeResult/delt26_int_Lm")[0].text, \
    " (", tree.findall("./exposureAgeResult/delt26_ext_Lm")[0].text, ")\n")
print(format(tree[1].tag), ": ", format(tree[1].text), "\n")

#maybe speed up with this? http://stackoverflow.com/questions/34512646/how-to-speed-up-api-requests
# better yet, this http://www.eamonnbell.com/blog/2015/10/05/the-right-way-to-use-requests-in-parallel-in-python/
