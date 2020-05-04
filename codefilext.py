mydict={
"c":"C",
"class":"Java",
"cpp" : "C++" ,
".cs" :"Visual C" ,
"h" : "C, C++, and Objective-C header file" ,
"jav": "Java Source code file" ,
"pl" : "Perl script file" ,
"sh": "Bash shell script" ,
"swift": "Swift" ,
"vb": "Visual Basic file" ,
"py":"python"
}
file=input("enter the file name with extension")
f_ext=file.split('.')
extension=f_ext[1]
if extension in mydict :
    a=mydict[extension]
    print("the extension of the file is ", (a))
else:
    print("the extension of the file is ", (extension))
