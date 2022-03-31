import re

txt = "Use of python in machine learning"
x = re.findall("in",txt)
print(x)

txt1 = "Python is one of the most popular languages around the world"
searchObj = re.search("\s",txt1)
print("first",searchObj.start())
searchObj1 = re.split("\s",txt1)
print(searchObj1)
a=len(txt1.split(" "))-1
print(a)
searchObj2 = re.sub("\s","_",txt1)
print(searchObj2)
searchObj3 = re.search("on",txt1)
print(searchObj3)

def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9$@.]')
    string = charRe.search(string)
    return not bool(string)
print(is_allowed_specific_char("ABCDEFabcdef123450$@"))
print(is_allowed_specific_char("*&%@#!}{"))

def text_match(text):
    patterns = 'ab*?'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')
print(text_match("bb"))
print(text_match("abc"))
print(text_match("abbc"))

string1 = "2004-959-559"
a = re.sub("-","",string1)
print(a)
print(re.sub("-","","2004-959-559"))

phone = "2004-959-559 # This is Phone Number"
# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print( "Phone Num : ", num)
# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print ("Phone Num : ", num)

def text_match(text):
    patterns = '^[a-zA-Z0-9_]*$'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python_Exercises_1"))




