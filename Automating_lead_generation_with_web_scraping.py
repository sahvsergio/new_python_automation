from bs4 import BeautifulSoup 
        from threading import Thread 
        import urllib 
 
        #Location of restaurants 
        home_url = "https://www.yelp.com" 
        find_what = "Restaurants" 
        location = "London" 
 
        #Get all restaurants that match the search criteria 
        search_url = "https://www.yelp.com/search?find_desc=" +
        find_what + "&find_loc=" + location 
        s_html = urllib.urlopen(search_url).read() 
        soup_s = BeautifulSoup(s_html, "lxml") 
 
        #Get URLs of top 10 Restaurants in London 
        s_urls = soup_s.select('.biz-name')[:10] 
        url = [] 
        for u in range(len(s_urls)): 
        url.append(home_url + s_urls[u]['href']) 
 
 
        #Function that will do actual scraping job 
        def scrape(ur): 
                html = urllib.urlopen(ur).read() 
                soup = BeautifulSoup(html, "lxml") 
 
                title = soup.select('.biz-page-title') 
                saddress = soup.select('.street-address') 
                phone = soup.select('.biz-phone') 
 
                if title: 
                     print "Title: ", title[0].getText().strip() 
                if saddress: 
                     print "Street Address: ",
        saddress[0].getText().strip() 
                if phone: 
                     print "Phone Number: ", phone[0].getText().strip() 
                print "-------------------" 
 
        threadlist = [] 
        i=0 
        #Making threads to perform scraping 
        while i<len(url): 
                  t = Thread(target=scrape,args=(url[i],)) 
                  t.start() 
                  threadlist.append(t) 
                  i=i+1 
 
        for t in threadlist: 
                  t.join() 
 