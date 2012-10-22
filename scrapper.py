'''
Created on 9 de Out de 2012

@author: pedrogoncalves
'''
import urllib



count = 1

while (count<8):    
    site = "http://www.windguru.cz/pt/index.php?sc="
    url= site + str(count)
    f = urllib.urlopen(url)  
    s = f.read()
    print s
    
    print("----------------")
    print "tamanho do dump em chars:", len(s)
    s  == ''
    f.close()
    print("----------------")
    count+=1
    
    
    

