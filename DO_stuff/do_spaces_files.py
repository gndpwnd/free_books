from spaces import Client
import os


def os_env_err():
  print("""OS ENV ERROR
Please set the following environment variables:

SPACE_NAME
SPACE_REGION
SPACE_PUB_KEY
SPACE_SEC_KEY

Reference file: /home/devel/Documents/env_vars/free_books_env_vars.txt
""")
  exit()

class Get_Data:

  chars_2_replace = [
    "',"
    "\","
    "'"
    "\""
    "("
    ")"
    "{"
    "}"
    "["
    "]"
  ]
  
  wierd_names = [
    "({"
  ]

  try:
    space_name = os.getenv('SPACE_NAME')
    space_region = os.getenv('SPACE_REGION')
    start_url = "https://{}.{}.cdn.digitaloceanspaces.com/".format(space_name, space_region)
  except:
    os_env_err()

  client = Client(
    region_name = space_region, # Required
    space_name = space_name, # Optional, can be set in spaces/env.yaml and/or be updated with <client>.set_space(space_name)
    public_key = os.getenv('SPACE_PUB_KEY'), # Required, but can set key in spaces/env.yaml                                                                         
    secret_key = os.getenv('SPACE_SEC_KEY'), # Required, but can set key in spaces/env.yaml
    # If any of region_name, public_key or secret_key are not provided, Client will override all values with env.yaml values.
  )

  def get_books_pdf(self):
    folder_name = "archive-books/"
    data = self.client.list_files(folder_name)
    return data
  
  def get_books_audio(self):
    folder_name = "archive-books-audio/"
    data = self.client.list_files(folder_name)
    return data

  def reorg_json_data(self, data):
    book_titles = []
    book_edge_urls = {}
    # books are stored in different folders, the folder names are the book categories
    book_categorization = {}
    
    # split data into a list
    data = str(data).split("'Key': '")

    for item in data:
      if item in self.wierd_names:
        pass
      else:

        # replace some chars
        for char in self.chars_2_replace:
          new_item = item.replace(char, "")
        
        # get the folder that the book is in
        # get book path
        book_path = new_item.split("',")[0]
        #print(book_path)
  
        #book_links.append(book_link)
        # get book title
        book_title = book_path.split("/")[-1]
        book_title = book_title.split(".")[0]
        book_title = book_title.replace("_", " ")
        book_titles.append(book_title)

        # get book edge url
        book_link = self.start_url + book_path
        book_edge_urls[book_title] = book_link

        # keep track of book categories
        book_category = book_path.split("/")[1]
        book_category = book_category.replace("_", " ")
        book_category = book_category.title()
        # add the book's name and category to book_categorization
        book_categorization[book_title] = book_category

    return book_titles, book_categorization, book_edge_urls

  def clean(self, infile, outfile):
    if os.path.exists(infile):
      os.remove(infile)
    if os.path.exists(outfile):
      os.remove(outfile)

  def __init__(self):
  
      data1 = self.get_books_pdf()
      
      data2 = self.get_books_audio()

      self.book_titles1, self.book_categorization1, self.book_edge_urls1 = self.reorg_json_data(data1)
      self.book_titles2, self.book_categorization2, self.book_edge_urls2 = self.reorg_json_data(data2)

def test():
  
  print("Testing...")

  data = Get_Data()

  book_titles1 = data.book_titles1
  book_categorization1 = data.book_categorization1
  book_edge_urls2 = data.book_edge_urls1

  book_titles2 = data.book_titles2
  book_categorization2 = data.book_categorization2
  book_edge_urls2 = data.book_edge_urls2

  #print(book_titles1)
  #for book in book_categorization1:
  #  print("\"" + book + "\",\"" + book_categorization1[book] + "\"")
  #for book in book_edge_urls2:
  #  print("\"" + book + "\",\"" + book_edge_urls2[book] + "\"")
  
  
  #print(len(book_titles1))

  #print(book_titles2)
  #print(len(book_links2))
  #print(len(book_titles2))

#test()