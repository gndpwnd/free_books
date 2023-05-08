#!/usr/bin/python3

# This script is out-dated, it doesn't create a search index, storage isn't up to date, among other things.
# I switched to using google drive for now, but digital ocean spaces are always a viable option.

'''

(Books are categorized based on topic/content)


Basic Digital Ocean Space File Structure Example

DO_space/
├─ subject_folder/
│  ├─ category1/
│  │  ├─ book1
│  │  ├─ book2
│  │  ├─ book7
│  ├─ category2/
│  │  ├─ book3
│  │  ├─ book4
│  ├─ category3/
│  │  ├─ book5
│  │  ├─ book6



Specific Digital Ocean Space File Structure Example

dev00psarchive/
├─ archive-books/
│  ├─ business/
│  │  ├─ The_Richest_Man_In_Babylon.pdf
│  │  ├─ Your_Next_Five_Moves.pdf
│  │  ├─ Rich_Dad_Poor_Dad.pdf
│  ├─ survival/
│  │  ├─ Anarchist_Cookbook.pdf
│  │  ├─ Ammunition_Handbook.pdf
│  ├─ mindset/
│  │  ├─ A_Hackers_Mind.pdf
│  │  ├─ Breathe.pdf

'''

import os
from colorama import Fore
from DO_stuff.g_analytics import *
from DO_stuff.do_spaces_files import *

prog = Fore.GREEN + "[+] " + Fore.RESET

num_checks = 1

host_dir = os.path.realpath(__file__).split("site_maker_DO.py")[0]
print("Host Dir:" + host_dir)

out_dir = os.path.join(host_dir, "docs")
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

books_dir = os.path.join(out_dir, "books")
if not os.path.exists(books_dir):
    os.mkdir(books_dir)

audio_books_dir = os.path.join(out_dir, "audiobooks")
if not os.path.exists(audio_books_dir):
    os.mkdir(audio_books_dir)

book_index_file = os.path.join(out_dir, "books.html")
audio_book_index_file = os.path.join(out_dir, "audiobooks.html")
main_index_file = os.path.join(out_dir, "index.html")

def clear_screen():
		if os.name == "nt":
			os.system("cls")
		elif os.name == "posix":
			os.system("clear")

def fancy_print(str, val, ind):
        indent = ""
        for i in range(ind):
            indent += "    "

        if val == "":
            print(indent + Fore.GREEN + "[+] " +  Fore.RESET + str)
        else:
            print(indent + Fore.GREEN + "[+] " + Fore.RESET + str + Fore.YELLOW + val + Fore.RESET)

def get_categories(dict):
    categories = []
    for key in dict:
        if dict[key] not in categories:
            categories.append(dict[key])
    num_categories = len(categories)
    return categories, num_categories

def gen_book_list(edge_data):
    book_titles = edge_data.book_titles1
    book_categorization = edge_data.book_categorization1
    book_edge_urls = edge_data.book_edge_urls1
    num_reg_books = 0

    book_html_p1 = """<!DOCTYPE html>
<html lang="en">
<head>
"""
    
    book_html_p2 = g_analytics_template
    
    book_html_p3 = """
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <meta 
        name="description"
        content="Author: gndpnwd
        Free PDF books. 
        Valuable content for free. 
        No ads, no paywalls, no bullshit.">
"""

    book_html_p4_p1 = """
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/grid.css">
    <link rel="stylesheet" href="css/button.css">
"""
    
    book_html_p4_p2 = """
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/grid.css">
    <link rel="stylesheet" href="../css/button.css">
"""

    book_html_p5 = """
    <title>Freshavacado</title>
</head>
<body class="everything">

    <div class="progress-container">
        <div class="progress-bar" id="myBar"></div>
    </div> 

    <script>
        window.onscroll = function() {progressbar()};

        function progressbar() {
            var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            var scrolled = (winScroll / height) * 100;
            document.getElementById("myBar").style.width = scrolled + "%";
        }
    </script>
"""

    book_html_p6_p1 = """
    <a href="https://books.dev00ps.com">
        <img class="title" src="assets/free_books.webp" alt="Free Books" stye="width:563px;height:251px;">
    </a>
"""

    book_html_p6_p2 = """
    <a href="https://books.dev00ps.com">
        <img class="title" src="../assets/free_books.webp" alt="Free Books" stye="width:563px;height:251px;">
    </a>
"""

    book_html_p7 = "\n\n    <div class=\"grid-container\">"

    book_html_p8 = """
    </div>
</body>
</html>
    """
    
    book_categories, num_reg_book_categories = get_categories(book_categorization)
    fancy_print("Generating books.html...", "", 1)

    with open(book_index_file, "w") as f:
        f.write(book_html_p1)
        f.write(book_html_p2)
        f.write(book_html_p3)
        f.write(book_html_p4_p1)
        f.write(book_html_p5)
        f.write(book_html_p6_p1)
        f.write(book_html_p7)
        
        category_num = 1
        for i in range(num_reg_book_categories):
            category_name = book_categories[i]
            link_name = category_name.replace(" ", "_")
            html_code = (f"""  
        <div class="grid-item">
            <button class="normal_button"><span onclick="window.open('books/{link_name}.html')"><strong>#{category_num}</strong><br>{category_name}</span></button>
        </div>
        """)
            f.write(html_code)
            category_num += 1
    
        f.write(book_html_p8)
        f.close()
    
    fancy_print("Creating category pages...", "", 1)
    for i in range(num_reg_book_categories):
        # start writing a new html file, but this time instead of book categories, use book names
        category_name = book_categories[i]
        link_name = category_name.replace(" ", "_")
        fancy_print("Generating " + link_name + ".html...", "", 2)
        path_to_file = os.path.join(books_dir, link_name + ".html")
        
        with open(path_to_file, "w") as f:
            num_books = 1
            f.write(book_html_p1)
            f.write(book_html_p2)
            f.write(book_html_p3)
            f.write(book_html_p4_p2)
            f.write(book_html_p5)
            f.write(book_html_p6_p2)
            f.write(book_html_p7)
            
            for j in range(len(book_titles)):
                book_name = book_titles[j]
                if book_categorization[book_name] == category_name:
                    book_link = book_edge_urls[book_name]
                    html_code = (f"""  
            <div class="grid-item">
                <button class="normal_button"><span onclick="window.open('{book_link}')"><strong>#{num_books}</strong><br>{book_name}</span></button>
            </div>
            """)
                    f.write(html_code)
                    num_books += 1

            num_reg_books += num_books
        
            f.write(book_html_p8)
            f.close()

    fancy_print("Number of Reg Book Categories: " + Fore.YELLOW + str(num_reg_book_categories), "", 1)
    fancy_print("Number of Reg Books: " + Fore.YELLOW + str(num_reg_books), "", 1)

def gen_book_list_audio(edge_data):
    book_titles = edge_data.book_titles2
    book_categorization = edge_data.book_categorization2
    book_edge_urls = edge_data.book_edge_urls2
    num_audio_books = 0

    book_html_p1 = """<!DOCTYPE html>
<html lang="en">
<head>
"""
    
    book_html_p2 = g_analytics_template
    
    book_html_p3 = """
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <meta 
        name="description"
        content="Author: gndpnwd
        Free PDF books. 
        Valuable content for free. 
        No ads, no paywalls, no bullshit.">
"""
    
    book_html_p4_p1 = """
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/grid.css">
    <link rel="stylesheet" href="css/button.css">
"""

    book_html_p4_p2 = """
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/grid.css">
    <link rel="stylesheet" href="../css/button.css">
"""

    book_html_p5 = """
    <title>Freshavacado</title>
</head>
<body class="everything">

    <div class="progress-container">
        <div class="progress-bar" id="myBar"></div>
    </div> 

    <script>
        window.onscroll = function() {progressbar()};

        function progressbar() {
            var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            var scrolled = (winScroll / height) * 100;
            document.getElementById("myBar").style.width = scrolled + "%";
        }
    </script>
"""

    book_html_p6_p1 = """
    <a href="https://books.dev00ps.com">
        <img class="title" src="assets/free_books.webp" alt="Free Books" stye="width:563px;height:251px;">
    </a>
"""

    book_html_p6_p2 = """
    <a href="https://books.dev00ps.com">
        <img class="title" src="../assets/free_books.webp" alt="Free Books" stye="width:563px;height:251px;">
    </a>
"""

    book_html_p7 = "\n\n    <div class=\"grid-container\">"

    book_html_p8_p1 = """
    </div>
</body>
</html>
    """

    book_html_p8_p2 = """
    <script>
        // change the speed of the all audio based on the slider
        const audio_players = document.querySelectorAll('.audio-player');
        const pbrates = document.querySelectorAll('#pbrate');
        const pbrateValues = document.querySelectorAll('#pbrate + span');
        // only change the speed of the selected audio player
        pbrates.forEach((pbrate, i) => {
            pbrateValues[i].innerHTML = pbrate.value;
            pbrate.addEventListener('input', function() {
                pbrateValues[i].innerHTML = this.value;
                audio_players[i].querySelector('audio').playbackRate = this.value;
            });
        });
    </script>
</body>
</html>
    """


    book_categories, num_audio_book_categories = get_categories(book_categorization)
    fancy_print("Generating audiobooks.html...", "", 1)

    with open(audio_book_index_file, "w") as f:
        category_num = 1
        f.write(book_html_p1)
        f.write(book_html_p2)
        f.write(book_html_p3)
        f.write(book_html_p4_p1)
        f.write(book_html_p5)
        f.write(book_html_p6_p1)
        f.write(book_html_p7)
        
        for i in range(len(book_categories)):
            
            category_name = book_categories[i]
            link_name = category_name.replace(" ", "_")
            html_code = (f"""  
        <div class="grid-item">
            <button class="normal_button"><span onclick="window.open('audiobooks/{link_name}.html')"><strong>#{category_num}</strong><br>{category_name}</span></button>
        </div>
        """)
            f.write(html_code)
            category_num += 1
    
        f.write(book_html_p8_p1)
        f.close()

    fancy_print("Creating category pages...", "", 1)
    for i in range(len(book_categories)):
        category_name = book_categories[i]
        link_name = category_name.replace(" ", "_")
        fancy_print("Generating " + link_name + ".html...", "", 2)
        path_to_file = os.path.join(audio_books_dir, link_name + ".html")

        with open(path_to_file, "w") as f:
            num_books = 1
            f.write(book_html_p1)
            f.write(book_html_p2)
            f.write(book_html_p3)
            f.write(book_html_p4_p2)
            f.write(book_html_p5)
            f.write(book_html_p6_p2)

            for j in range(len(book_titles)):
                book_name = book_titles[j]
                if book_categorization[book_name] == category_name:
                    book_link = book_edge_urls[book_name]
                    html_code = (f"""  
        <div class="audio-player">
            <br>
            <br>
            <p><strong>#{num_books}</strong> 
            <br>
                {book_name}
            </p>
            <div class="speedcontrolcontainer">
                <audio src="{book_link}" controls></audio>
                <div>
                <label for="pbrate">Speed:</label>
                <input type="range" id="pbrate" min=.6 max=3 value=1 step=.2>
                <span></span>
                </div>
            </div>
        </div>
        """)
                    f.write(html_code)
            num_books += 1
    
            f.write(book_html_p8_p2)
            f.close()
            num_audio_books += num_books

    fancy_print("Number of Audio Book Categories: " + Fore.YELLOW + str(num_audio_book_categories), "", 1)
    fancy_print("Number of Audio Books: " + Fore.YELLOW + str(num_audio_books), "", 1)

def gen_index():
    fancy_print("Generating index.html...", "", 0)
    index_html_p1 = """<!DOCTYPE html>
<html lang="en">
<head>
"""
    index_html_p2 = g_analytics_template
    index_html_p3 = """
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta 
        name="description"
        content="Author: gndpnwd
        Free PDF books. 
        Valuable content for free. 
        No ads, no paywalls, no bullshit.">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/button.css">

    <title>Freshavacado</title>
</head>
<body class="everything">

    <a href="https://books.dev00ps.com">
        <img class="title" src="assets/free_books.webp" alt="Free Books" stye="width:563px;height:251px;">
    </a>

  <h2 class="subtitle">Valuable content for free. <i>No ads, no paywalls, no bullshit.</i></h2>
    
  <h3 class="subtitle">
    <button class="menu_button"><span onclick="window.location='./books.html'">Books</span></button>
    <button class="menu_button"><span onclick="window.location='./audiobooks.html'">Audiobooks</span></button>
    <button class="menu_button"><span onclick="window.location='./donate.html'">Donate</span></button>
    <button class="menu_button"><span onclick="window.location='https://cliffnotes.dev00ps.com'">Cliffnotes</span></button>
  </h3>

  <p class="description-head">Project Goals</p>
  <ul class="description">
    <li class="bullet_point">To accumulate knowledge for success in life</li>
    <li class="bullet_point">To store such knowldege in an easily accessable library</li>
    <li class="bullet_point">To condense the size of such library to fit the completion of reading withing an average lifespan</li>
  </ul>

  <p class="description-head">Description</p>

  <ul class="description">
    <li class="bullet_point">This project uses paid cloud storage to host content free to download.</li>
    <li class="bullet_point">Book organization is simply via alphbetical order in each category.</li>
    <li class="bullet_point">Google Analytics is intended to be used to measure this site's impact on the world.</li>
    <li class="bullet_point"><strong>If using Chrome,</strong> it is recommended to <a href="https://chrome.google.com/webstore/detail/pdf-viewer/oemmndcbldboiebfnladdacbdfmadadm/">install this extension</a> to view pdfs rather than downloading them.</li>
  </ul>

  <h2 class="subsubtitle">
    <button class="menu_button"><span onclick="window.location='https://github.com/gndpwnd/free_books/'">Project Github</span></button>
    <button class="menu_button"><span onclick="window.location='https://github.com/gndpwnd'">Author</span></button>
  </h2>

  </body>
</html>
"""
    with open(main_index_file, "w") as f:
        f.write(index_html_p1)
        f.write(index_html_p2)
        f.write(index_html_p3)

if __name__ == "__main__":
    clear_screen()
    fancy_print("Using directory: ", host_dir, 0)
    fancy_print("Outputting to: ", out_dir, 0)
    fancy_print("Getting Library Data...", "", 0)
    edge_data = Get_Data()
    gen_book_list(edge_data)
    gen_book_list_audio(edge_data)
    gen_index()
    fancy_print("Done!", "", 0)