# main.py
from spaces import Client
import os
import urllib.parse


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
    data = self.client.list_files("archive-books/")
    return data
  
  def get_books_audio(self):
    data = self.client.list_files("archive-books-audio/")
    return data

  def reorg_json_data(self, data):
    book_links = []
    book_titles = []
    data = str(data).split("'Key': '")

    for item in data:
      for char in self.chars_2_replace:
        new_item = item.replace(char, "")
      # get book link
      book_link = new_item.split("',")[0]
      book_link = self.start_url + book_link
      book_links.append(book_link)
      # get book title
      book_title = book_link.split("/")[-1]
      book_title = book_title.split(".")[0]
      book_title = book_title.replace("_", " ")
      book_titles.append(book_title)

    for name in self.wierd_names:
      index = book_titles.index(name)
      book_titles.remove(book_titles[index])
      book_links.remove(book_links[index])

    return book_links, book_titles

  def clean(self, infile, outfile):
    if os.path.exists(infile):
      os.remove(infile)
    if os.path.exists(outfile):
      os.remove(outfile)

  def __init__(self):
  
      data1 = self.get_books_pdf()
      
      data2 = self.get_books_audio()

      self.book_links1, self.book_titles1 = self.reorg_json_data(data1)
      self.book_links2, self.book_titles2 = self.reorg_json_data(data2)

def test():
  
  print("Testing...")

  data = Get_Data()

  book_links1  = data.book_links1
  book_titles1 = data.book_titles1
  
  book_links2  = data.book_links2
  book_titles2 = data.book_titles2


  print(book_links1)
  print(book_titles1)

  print(book_links2)
  print(book_titles2)
