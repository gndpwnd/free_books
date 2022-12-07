#!/usr/bin/python3

import glob
import os
from colorama import Fore
#import filenamefixer
import shutil
from g_analytics import *
from do_spaces_files import *

prog = Fore.GREEN + "[+] " + Fore.RESET

num_checks = 1
#filenamefixer.ffixer(num_checks)
#clear_screen()

host_dir = os.path.realpath(__file__).split("book_list_generator.py")[0]
print("Host Dir:" + host_dir)
out_dir = host_dir + "docs/"
books_dir = out_dir + "books/"

book_file = out_dir + "books.html"
audio_book_file = out_dir + "audiobooks.html"
index_file = out_dir + "index.html"

rel_books_dir = "./books/"

book_html_codes = []
books = {}

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

def scan_dir_for_books(books_dir):

    for filename in os.listdir(books_dir):
        book_name = filename.split(".")[0].replace("_", " ")
        # replace full dir path with relative path

        book_path = "./" + books_dir.split("docs/")[1]
        book_path = book_path + filename

        books[book_name] = book_path

def get_book_data():
    num_books = 1
    num_books_found = 0

    num_max_dir_depth = 4
    fancy_print("Scanning for books (only 3 directories deep)...", "", 0)

    for item in os.listdir(books_dir):
        if os.path.isdir(books_dir + item):
            new_dir = books_dir + item + "/"
            
            for item2 in os.listdir(new_dir):
                if os.path.isdir(new_dir + item2):
                    new_dir2 = new_dir + item2 + "/"
            
                    for item3 in os.path.isdir(new_dir2 + item3):
                        if os.path.isdir(new_dir2 + item3):
                            new_dir3 = new_dir2 + item3 + "/"
                            
                            for item4 in os.listdir(new_dir3):
                                if os.path.isdir(new_dir3 + item4):
                                    new_dir4 = new_dir3 + item4 + "/"
                                    fancy_print("Directory depth exceeded. Skipping...", "", 1)
                                    continue

                                else:
                                    scan_dir_for_books(new_dir3)
                                    num_books_found += 1

                        else:
                            scan_dir_for_books(new_dir2)
                            num_books_found += 1
                        
                else:
                    scan_dir_for_books(new_dir)
                    num_books_found += 1

        else:
            scan_dir_for_books(books_dir)
            num_books_found += 1


    for title in sorted(books.keys()):
        
        html_code = (f"""
        
        <div class="grid-item">
            <button class="normal_button"><span onclick="window.open('{books[title]}')"><strong>#{num_books}</strong><br>{title}</span></button>
        </div>

        """)

        book_html_codes.append(html_code)
        num_books += 1
    
    if num_books == 0:
        fancy_print("No books found in: ", books_dir, 1)
    elif num_books == 1:
        fancy_print("Found " + Fore.YELLOW + str(num_books) + Fore.RESET + " book", "", 1)
    else:
        fancy_print("Found " + Fore.YELLOW + str(num_books) + Fore.RESET + " books", "", 1)

    return num_books_found

def gen_book_list():

    fancy_print("Generating books.html...", "", 0)
    books_dir = "./books/"
    write_dir = "./docs/books/"

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

    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/grid.css">
    <link rel="stylesheet" href="css/button.css">


    <title>Freshavacado</title>
</head>
<body class="everything">
    <style>
        .progress-bar {
            height: 8px;
            background: #7DF9FF;
            width: 0%;
        }
    </style>

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

    <!-- <h1 class="title">Free Books</h1> -->
    <img class="title" src="assets/free_books.webp" alt="Free Books">

    <h2 class="subtitle">Valuable content for free. <i>No ads, no paywalls, no bullshit.</i></h2>
"""

    book_html_p4 = "\n\n    <div class=\"grid-container\">"

    book_html_p5 = """
    </div>
</body>
</html>
    """

    edge_data = Get_Data()
    book_titles = edge_data.book_titles1
    book_links = edge_data.book_links1

    with open(book_file, "a") as f:
        num_books = 1
        f.write(book_html_p1)
        f.write(book_html_p2)
        f.write(book_html_p3)
        f.write(book_html_p4)
        
        for i in range(len(book_titles)):
            
            book_name = book_titles[i].replace("_", " ")
            book_name = book_name.title()
            book_link = book_links[i]
            html_code = (f"""  
        <div class="grid-item">
            <button class="normal_button"><span onclick="window.open('{book_link}')"><strong>#{num_books}</strong><br>{book_name}</span></button>
        </div>
        """)
            f.write(html_code)
            num_books += 1
    
        f.write(book_html_p5)
        f.close()

def gen_book_list_audio():
    fancy_print("Generating audiobooks.html...", "", 0)
    books_dir = "./books/"
    write_dir = "./docs/books/"

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

    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/grid.css">
    <link rel="stylesheet" href="css/button.css">


    <title>Freshavacado</title>
</head>
<body class="everything">
    <style>
        .progress-bar {
            height: 8px;
            background: #7DF9FF;
            width: 0%;
        }

        .speedcontrolcontainer {
            width: 100%;
            display: block;
            border: 1px solid #000;
            padding: 10px;
            font-family: Sans-serif;
        }
        .speedcontrolcontainer audio {
            width: 100%;
            display: block;
        }
        .speedcontrolcontainer div {
            display: flex;
            padding: .5em 0;
            gap: 5px;
        }
        .speedcontrolcontainer label {
            flex: 1;
        }
        .speedcontrolcontainer input[type="range"] {
            flex: 5;
            color: #7DF9FF;
        }
        .speedcontrolcontainer span {
            flex: 1;
            text-align: center;
        }

        p {
            font-size: 1.5em;
            text-align: center;
        }
    </style>

    <script>
        // change the speed of the audio based on the slider
        var audio = document.querySelector('audio');
        var pbrate = document.querySelector('#pbrate');
        var pbrateValue = document.querySelector('#pbrate + span');
        pbrateValue.innerHTML = pbrate.value;
        pbrate.addEventListener('input', function() {
          pbrateValue.innerHTML = this.value;
          audio.playbackRate = this.value;
        });
    </script>

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

    <!-- <h1 class="title">Free Books</h1> -->
    <img class="title" src="assets/free_books.webp" alt="Free Books">

    <h2 class="subtitle">Valuable content for free. <i>No ads, no paywalls, no bullshit.</i></h2>
"""

    book_html_p5 = """
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

    edge_data = Get_Data()
    book_titles = edge_data.book_titles2
    book_links = edge_data.book_links2

    with open(audio_book_file, "a") as f:
        
        num_books = 1
        f.write(book_html_p1)
        f.write(book_html_p2)
        f.write(book_html_p3)
        
        for i in range(len(book_titles)):
            
            book_name = book_titles[i].replace("_", " ")
            book_name = book_name.title()
            book_link = book_links[i]
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
    
        f.write(book_html_p5)
        f.close()

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

    <!-- <h1 class="title">Free Books</h1> -->
    <img class="title" src="assets/free_books.webp" alt="Free Books">

  <h2 class="subtitle">
    <button class="menu_button"><span onclick="window.location='./books.html'">Books</span></button>
    <button class="menu_button"><span onclick="window.location='./audiobooks.html'">Audiobooks</span></button>
  </h2>

  <p class="description-head">Description</p>

  <ul class="description">
    <li class="bullet_point">This project aims to collect books that provide incredible value and host them free to download.</li>
    <li class="bullet_point">Book organization is simply via alphbetical order per category.</li>
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
    with open(index_file, "w") as f:
        f.write(index_html_p1)
        f.write(index_html_p2)
        f.write(index_html_p3)


if __name__ == "__main__":
    clear_screen()
    if os.path.exists(book_file):
        os.remove(book_file)
    if os.path.exists(audio_book_file):
        os.remove(audio_book_file)
    if os.path.exists(index_file):
        os.remove(index_file)

    try:
        shutil.rmtree("__pycache__")
        shutil.rmtree("docs/books")
    except:
        pass
    print("\n\n")
    fancy_print("Using directory: ", books_dir, 0)
    fancy_print("Outputting to: ", out_dir, 0)
    #num_books = get_book_data()
    #gen_index(num_books)
    gen_book_list()
    gen_book_list_audio()
    gen_index()
    fancy_print("Done!", "", 0)