################################################################################
#Libraries
import pandas as pd
import requests
import datetime
import numpy as np
from bs4 import BeautifulSoup
################################################################################



################################################################################

#Enter your own file name
f=open('youtube_data.csv','w')
f.close()
f=open('youtube_data.csv','a')



while(True):
    #Enter the url of the youtube video here...
    page=requests.get("https://www.youtube.com/watch?v=MfTbHITdhEI")
    soup=BeautifulSoup(page.content,'html.parser')

    #For date and time
    now=datetime.datetime.now()
    #df=pd.DataFrame(columns=['Month','Day','Hour','minute','views','likes','dislikes','subscribers'])

    ################################################################################















    ################################################################################
    '''
    This part contains code for scrapping the number of views
    '''
    views=soup.find_all(class_='watch-view-count')[0].get_text()
    views2=views[0:int(len(views))-6]
    views2=views2.replace(',','')
    views=int(views2)
    ################################################################################











    ################################################################################
    '''
    This part contains code for scrapping the number of likes, dislikes and subscribers
    '''
    likes=soup.find_all(class_='yt-uix-button-content')[15].get_text()
#    print("likes="+likes)
    likes=likes.replace(',','')
    likes=int(likes)


    dislikes=soup.find_all(class_='yt-uix-button-content')[18].get_text()
#    print("dislikes="+dislikes)
    dislikes=dislikes.replace(',','')
    dislikes=int(dislikes)


    subscribers=soup.find_all(class_='yt-uix-button-content')[20].get_text()
#    print("subscribers="+subscribers)
    subscribers=subscribers.replace(',','')
    subscribers=int(subscribers)

    ################################################################################






















    ################################################################################

    '''
    Writing data into the csv file
    '''
    a=np.asarray([[now.month,now.day,now.hour,now.minute,views,likes,dislikes,subscribers]])
    np.savetxt(f,a,fmt='%i',delimiter=",")
    ################################################################################
