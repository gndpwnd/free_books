import os
import json

def clear_search_index(book_index_json_file):
    if os.path.exists(book_index_json_file):
        os.remove(book_index_json_file)
    return True

def add_to_index(book_index_json_file, folder_name, books_list):
    '''
    Example json:
    {
        "category1": [
            {
                "title": "Book 1",
                "link": "https://book1.com",
            },
            {
                "title": "Book 2",
                "link": "https://book2.com",
            }
        ],
        "category2": [
            {
                "title": "Book 3",
                "link": "https://book3.com",
            },
            {
                "title": "Book 4",
                "link": "https://book4.com",
            }
        ]
    }
    '''
    # the folder_name is the category that books are sorted into
    #book_list is a list of lists, every list has a book name "item[0]" and a book link "item[1]"
    # only one category and corresponding list of books is passed at a time to this function
    #so, add a new category to the json file
    if os.path.exists(book_index_json_file):
        with open(book_index_json_file, 'r') as f:
            book_index = json.load(f)
    else:
        book_index = {}

    # replace underscores in the category's names with spaces and capitalize
    folder_name = folder_name.replace("_", " ").title()

    # replace underscores in the book's names (the first item) with spaces
    # also remove ".pdf"
    for book in books_list:
        book[0] = book[0].replace("_", " ")
        book[0] = book[0].replace(".pdf", "")
    
    # add to json file
    book_index[folder_name] = books_list
    with open(book_index_json_file, 'w') as f:
        json.dump(book_index, f, indent=4)
        return book_index