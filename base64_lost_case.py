import base64
import re

def is3ascii(str):
    # boolean: is the string 1 to 3 characters which are alphanumeric or space
    x = len(re.findall("^[a-zA-Z0-9 ]{1,3}$",str))
    return x==1


def four_b64decode(string1):
    #base64 decode all possibilities of a four-character chunk which has lost letter case
    options=[""]
    for char in string1:
        buffer1=[]
        for option in options:
            buffer1.append(option+char)
            if char!=str.upper(char):
                buffer1.append(option+str.upper(char))
        options=buffer1
    buffer2=[]
    for option in options:
        decoded=base64.standard_b64decode(option)
        if is3ascii(decoded):
            buffer2.append(decoded)
    return buffer2

def base64decode_lostcase(string1):
    #base64 decode all possibilities of a string which has lost letter case
    index=0
    length1=len(string1)
    list1=[]
    options=[""]
    while index+4<length1:
        chunks=four_b64decode(string1[index:index+4])
        if len(chunks)>0:
            buffer1=[]
            for option in options:
                for chunk in chunks:
                    buffer1.append(option+chunk)
        options=buffer1
        index=index+4
    buffer2=[]
    return options

def cleanupstring(string1):
    #known cleanups specific to this data set
    string1=string1.replace('-', '=')
    string1=string1[7:]
    return string1
    
def pickfnamelnamessn(strings):
    #apply the knowledge that the plaintext is in the format of firstname, lastname, and SSN.
   #Note that this would fail on names that do not follow title case, but this data set does not have any.
    buffer1=[]
    for string in strings:
        match=re.findall("^[A-Z][a-z]*\s[A-Z][a-z]*\s\d{9}",string)
        if len(match)>0:
            buffer1.append(match[0])
    return buffer1

domainstrings=[
"tahsje3qm9ubmlliehpbgwgnde2odaymzgwf1r4kvpjakr",
"tahsje3tmljag9syxmgqmfycia2nzq4ntm4otc-ncd5ohstkd",
"tahsje3qwtpier1cmhhbsa4ntc2otqynjy-dfhfmmvtnoesp9idq9",
"tahsje3q2hhbnrhbcbny2zhcmxhbmqgntmzmzqymzuzzfgbizg8l",
"tahsje3wxvtasblbm93bgvzidgxmtk5ndg3mg--iwukrtdnd",
"tahsje3tgvzbgllienlcnzhbnrlcya0nda4oty2ndm-zd71xqba",
"tahsje3ugfsb21hiejhcmjlcia1mte3nzg5ndm-igpmggqa",
"tahsje3q2hpywtpietpzgqgmdkwmze0ndi2sfpe1",
"tahsje3vmfszxjpzsbxawxrzxjzb24gndywodcynjkzhokuyvgdq",
"tahsje3tmljb2xlie1jy295idq0mtq2mdiwoq--er5hqt",
"tahsje3rgfuawvsbgugr29vzca5njm2ody1mjk-zcceiamzawpxhv23"
]

for domainstring in domainstrings:
    print(pickfnamelnamessn(base64decode_lostcase(cleanupstring(domainstring))))
