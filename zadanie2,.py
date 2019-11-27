#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  zadanie2,.py
#  
#  Copyright 2019  <>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 
def sumuj_parzyste(a, b): 
    suma = 0 
    for liczba in range(a, b + 1):
        if liczba % 2 == 0 :
            suma = suma + liczba
    print(suma)
    
     
def sumuj_nieparzyste(a, b): 
    suma = 0 
    for liczba in range(a, b + 1):
        if liczba % 2 > 0:
            suma = suma + liczba
    print(suma) 
    
def main(args): 
    a = b = -1
    while a < 0: 
        a = int(input('Podaj 1 liczbę: '))
    while b <= a:
        b = int(input('Podaj 2 liczbę: '))
        
        
    sumuj_parzyste(a, b)
    
    return 0

   
    # ~if a > b or a == b:
       # ~print('Błędne dane')
       # ~return
    # ~if a < 0 or b < 0:
       # ~print('Błędne dane')
       # ~return
        
        
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
