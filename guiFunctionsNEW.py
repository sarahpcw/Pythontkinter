# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:24:53 2019

@author: u
"""

class guiFunctionsNEW():
    
    def calcPassword(self, pw):
        #initialise variables   
        numbers = '0123456789'
        letters = 'abcdefghijklmnopqrstuvwxyz'
        caps = letters.upper()      
        n = l = myCap = length = False
        vN = vLo= vU = vL = 'Fail'
        validation = ''
        #validaton: 8 or more characters long, must have a letter, a capital letter and a number
        if len(pw) >= 8: 
                length=True
                vL = "Pass"
        for letter in pw: 
                if letter in caps : 
                    myCap = True
                    vU ='Pass'
                if letter in numbers :
                    n = True
                    vN='Pass'
                if letter in letters :
                    l = True
                    vLo ='Pass'        
        #messaging
        if not n:
                print ('Password Invalid. It should have at least one number' )   
        if not l:
                print ('Password Invalid. It should have at least one lowercase letter' )
        if not myCap:
                print ('Password Invalid. It should have at least one uppercase letter' )
        if not length:
                print ('Password Invalid. It should be 8 characters long' )
        
        #validation return value
        if (   n and l and myCap and length  ):
            print ('Password Valid')
            validation = 'Password valid'
        else:
            validation = 'Password invalid'
        return validation, vN, vLo, vU, vL