# This is to test GitHub 
#this is a commmand 
#print('Hello, World!')
#print('What is your name?')
#myName = input()
#print('it is good to meet you, ' + myName)
#print('The length of your name is: ' )
#print(len(myName) )
#print('What is your age?')      #Ask for their age
#myAge = input()
#print('You will be ' + str(int(myAge)+1) + ' in a year. ')

Header = "JOBS     M/S    TS USERS    SYSAS    INITS   ACTIVE/MAX VTAM     O"
str = "CT=000.058S  ET=01.37.57"
#sampleStr =  {" LUISAM   OWT     A=00A1   PER=NO   SMC=000  PGN=N/A  DMN=N/A  A"
samplesStr=  [
                "ATS1      2020316  19:24:55.02             ISF041I CONSOLE NAME LUISAM MODIFIED", 
                "ATS1      2020316  19:24:55.02             ISF031I CONSOLE LUISAM$ ACTIVATED", 
                "ATS1      2020316  19:24:55.02            -D TS,ALL", 
                "ATS1      2020316  19:24:55.02             CNZ4106I 19.24.55 DISPLAY ACTIVITY 060", 
                "                                             JOBS    M/S    TS USERS    SYSAS    INITS   ACTIVE/MAX VTAM     OAS", 
                "                                           00093    00027    00001      00037    00109    00001/00060       00110", 
                "                                           LUISAM   OWT     A=00AF   PER=NO   SMC=000  PGN=N/A  DMN=N/A  AFF=NONE", 
                "                                                            CT=000.023S  ET=01.20.47", 
                "                                                            WUID=TSU29441", 
                "                                                            WKL=TSO_WKL  SCL=TSO_DEF  P=1", 
                "                                                            RGP=N/A      SRVR=NO  QSC=NO", 
                ""
            ]

HeadKey = list(Header.split()) 
#Headkey = list(filter(None, Header.split("  ")))
#HeadKey = [s.strip() for s in Header.split('  ') if s]
#print(HeadKey)
res={}
finalResult ={}

for i in range(5,10): 
#d = dict( x.split("=") for x in str.split() )
#for key in HeadKey: 
    info_line =  samplesStr[i].strip()  
   # info_line = samplesStr[i]
    InfoString = list(info_line.split())
    #InfoString = [w.strip() for w in info_line.split('  ') if w]
    #print(InfoString[0])
    #for (key,value) in zip (HeadKey, samplesStr):
   
    #if len(HeadKey) > len(InfoString):
     #print(len(HeadKey))
    for y in range(len(InfoString)):
       
         res[HeadKey[y]] = InfoString[y]
         print(res)
    finalResult[i] = dict(res)       
        
print("final")
print(finalResult)
#print("rest array now")
#print(  res)
#for k, v in d.items():
    #print(k, v)


#print(d) 

# result['headerInfo'] = module.params['string'][3].strip()            
#    result['user']       = module.params['string'][5].strip()            
                                                                         
    #create a list of header keys                                        
#    HeadKey = list(Header.split())                           
                                                             
    