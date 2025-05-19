from math import sqrt

def calculator():
     while True:
     
         f = input("enter the first number(or type 'exit' to quit): ")
         
#exit condition for first input :
         if str(f).lower() == "exit":
             print("calculator closed")
             break
             
#for float value of (f) :  
         try:
             f = float(f)
         except ValueError:
             print("invalid input")
             continue
             
         o = input("enter your operation:(+, -, *, /, //, %, <, >, <=, >=, ==, !=, sqrt, **)")
         
#sqrt condition :
         if o == "sqrt":
             print(sqrt(f))
             continue
             
         s = input("enter the second number(or enter 'exit' to quit): ")
         
#exit condition for second input :
         if str(s).lower() == "exit":
             print("calculator closed")
             break
             
#for float value of (s) :
         try:
             s = float(s)
         except ValueError:
             print("invalid input")
             continue
             
#'if', 'elif' and 'else' confition :
    
#"+" condition :     
         if o == "+" :
             print("result:", f + s)
#"-" condition  :            
         elif o == "-" :
             print("result: ", f - s)
#"*" condition :            
         elif o == "*" :
             print("result: ", f * s)
#"/" condition :           
         elif o == "/" :
                 print("result: ", f / s if s != 0 else "division with zero is not allowed")
#"//" condition  :          
         elif o == "//" :
                 print("result: ", f // s if s != 0 else "division with zero is not allowed")
#"%" condition  :         
         elif o == "%" :
                  print("result: ", f % s if s != 0 else "division with zero is not allowed")
#"<" condition  :           
         elif o == "<":
              print("result: ", f < s)
#">" condition  :           
         elif o == ">":
              print("result: ", f > s)
#"<=" condition :            
         elif o == "<=":
              print("result: ", f <= s)  
#">=" condition :              
         elif o == ">=":
              print("result: ", f >= s)
#"==" condition :             
         elif o == "==":
              print("result: ", f == s)
#"!=" condition :             
         elif o == "!=":
              print("result: ", f != s)
#"**" condition :             
         elif o == "**":
              print("result: ", f ** s)
#"else" condition :             
         else:
              print("invalid operation")
              
calculator()
         
     

