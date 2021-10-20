# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 20:43:35 2021

@author: Seema S Kanaje

  Method to return a formatted string based on the input Object
  Accepts a JSON Object containing message, date, views, author as the properties
  Returns formatted string.

"""

import json
from dateutil import parser

trendingChirpLimit = 100000;
chirpCharacterLimit = 140


with open("chirpViews.json", encoding="utf8") as f:
    chripViews = json.load(f)
    
    
def chripViewsFormat(chrips):
    
    for chrip in chrips:
        if(chrip=='message'):
            message=chrips[chrip]
            
        elif(chrip=='author'):
            author=chrips[chrip]
        
        elif(chrip=='views'):
            views=(chrips[chrip])
            
        elif(chrip=='date'):
            
            ISODate = parser.parse(chrips[chrip])
            date=(ISODate.strftime('%m/%d/%Y'))
            
    chripInfo=(date+" "+str(views)+" "+author)  
    #Adding Fire Emoji If Views greater than 100000
    if(views>trendingChirpLimit):
            chripInfo+=" \N{fire}"
   
    formattedMessage=message+" "+chripInfo  
    #Slicing if Length of Characters is greater than 140
    if(len(formattedMessage)>chirpCharacterLimit):
        trunc_len=(chirpCharacterLimit-1-len(chripInfo)-3)
        
        formattedMessage=message[:trunc_len]+"... "+chripInfo
        
    return(formattedMessage)
    

for chrips in chripViews:
    final_message=chripViewsFormat(chrips)
  
    
    


          
            









