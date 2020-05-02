def get_info(books_list):
  result = []
  for book in books_list:
    
    title = book.find("a", {"class" : "N=a:bta.title"}).string


    author = book.find("dd",{"class" : "txt_block"}).find("a", {"class" : "txt_name N=a:bta.author"}).string.strip()


    publisher = book.find("dd", {"class" : "txt_block"}).find("a", {"class" : "N=a:bta.publisher"}).string.strip()


    pub_date = book.find("dd", {"class" : "txt_block"}).text[-10:]


    try: 
      price = book.find("dd", {"class" : "txt_desc"}).find("em", {"class" : "price"}).string
    except: #error in getting price
      price = "null"

    link = book.find("dt").find("a", {"class" : "N=a:bta.title"})["href"]

    img_src = book.find("a", {"class" : "N=a:bta.thumb"}).find("img")["src"]
    book_info = {
      "title" : title,
      "author" : author,
      "publisher" : publisher,
      "pub_date" : pub_date,
      "price" : price,
      "link" : link,
      "img_src" : img_src,

    }
    result.append(book_info)
  return result
