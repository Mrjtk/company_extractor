import requests
from bs4 import BeautifulSoup
from time import sleep
import csv
state=input("Enter name of the state: ")
f=open('companynames.csv','w+')
cs=csv.writer(f)
cs.writerow(['Company Name',"CIN no"])
a=0
error=0
while True:
        url2=f"https://www.infoqik.com/companies/{state}/registered-list-{a}.html"
        headers = {
            'User-Agent': 'Mozilla/6.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                                            }

        page2=requests.get(url2,headers=headers)
        if page2.status_code==200:
                    soup2=BeautifulSoup(page2.content,'html.parser')
                    company_data2=(soup2.get_text())
                    c=company_data2.splitlines()
                    try:
                        
                        b=c[92]
                        b=b.split("  ")
                        for i in b:
                            try:
                                i=int(i)
                            except:
                                out=i.split("-")
                                
                                if len(out)>=3:
                                    out=out[1::]
                                    print(out)
                                    cs.writerow(out)
                                else:
                                    pass
                                
                    except:
                        pass
                    
                    a+=1
        else:
            print('faced an error ')
            error+=1
            if error==2:
                break
            else:
                pass
