from bs4 import BeautifulSoup 
import requests
import threading
import time 

url = "https://www.google.co.in"

def parse(url):
    response = requests.get(url) 
    print(response.text)  
    soup = BeautifulSoup(response.text, 'html.parser')
    o = []
    for e in soup.select('a'):
        o.append(e.attrs['href'])
    print(o)
    
if __name__ == '__main__':
    print("Sequentially")
      
    print("Parallely")
    ths = []
    st = time.time()
    for _ in range(10):
        th = threading.Thread(target=parse, args=(url,))
        ths.append(th)
     
    [th.start() for th in ths]
    
    [th.join() for th in ths]
    print("Time taken", time.time()-st, "secs")

    
    
    


