def get_info(book_list, abstract_list):
    result=[]
    for i in range(len(book_list)):
        book_info = {}
        title = book_list[i].find("td", {"class" : "goodsTxtInfo"}).find("p").find("a").text.strip()
        book_info["title"] = title
        
        img_src = book_list[i].find("div", {"class" : "goodsImgW"}).find("img")["src"]
        book_info["img_src"] = img_src
        
        author = book_list[i].find("td", {"class" : "goodsTxtInfo"}).find("div", {"class" : "aupu"}).find("a").text.strip()
        book_info["author"] = author
        
        publisher = book_list[i].find("td", {"class" : "goodsTxtInfo"}).find("div", {"class" : "aupu"}).find_all("a")[-1].text.strip()
        book_info["publisher"] = publisher

        price = book_list[i].find("td", {"class" : "goodsTxtInfo"}).find("span", {"class" : "priceB"}).text.strip()
        book_info["price"] = price

        abstract = abstract_list[i].find("p", {"class" : "read"}).text.strip()
        book_info["abstract"] = abstract

        result.append(book_info)
    return result