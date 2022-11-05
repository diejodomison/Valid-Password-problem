a= input() 
if 8<=len(a)<=32 and a[0].isalpha() and '/' not in a and '\\' not in a and '=' not in a and '\'' not in a and '\"' not in a and ' ' not in a : 
    print ('True') 
     
else : 
    print ('False') 