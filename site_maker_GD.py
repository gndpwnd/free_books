import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from tqdm import tqdm
from colorama import Fore

'''

(Books are categorized based on topic/content)

Basic Google Drive File Structure Example

Google Drive/
├─ category1/
│  ├─ book1
│  ├─ book6
│  ├─ book7
├─ category2/
│  ├─ book3
│  ├─ book5
│  ├─ book8
├─ category3/
│  ├─ book2
│  ├─ book4


Specific Google Drive File Structure Example

FreeBooks Drive/
├─ business/
│  ├─ The_Richest_Man_In_Babylon.pdf
│  ├─ Your_Next_Five_Moves.pdf
│  ├─ Rich_Dad_Poor_Dad.pdf
├─ mindset/
│  ├─ A_Hackers_Mind.pdf
│  ├─ Breathe.pdf
├─ survival/
│  ├─ Anarchist_Cookbook.pdf
│  ├─ Ammunition_Handbook.pdf

'''

# Replace with your own credentials file
creds_dir = "creds"
creds_file = os.path.join(creds_dir, "credentials.json")
pickle_file = os.path.join(creds_dir, "token.pickle")

host_dir = os.path.realpath(__file__).split("site_maker_GD.py")[0]
out_dir = os.path.join(host_dir, "docs")
books_dir = os.path.join(out_dir, "books")

book_index_file = os.path.join(out_dir, "books.html")
audio_book_index_file = os.path.join(out_dir, "audiobooks.html")
main_index_file = os.path.join(out_dir, "index.html")

prog = Fore.GREEN + "[+] " + Fore.RESET

def fancy_print(str, val, ind):
        indent = ""
        for i in range(ind):
            indent += "    "

        if val == "":
            print(indent + Fore.GREEN + "[+] " +  Fore.RESET + str)
        else:
            print(indent + Fore.GREEN + "[+] " + Fore.RESET + str + Fore.YELLOW + val + Fore.RESET)

fancy_print("Using The Following Information", "", 0)
print(Fore.YELLOW + "Host Dir: " + Fore.RESET + host_dir)
print(Fore.YELLOW + "Out Dir: " + Fore.RESET + out_dir)

def sys_checks():

    fancy_print("Performing System Checks", "", 0)

    # Site Directories

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    if not os.path.exists(books_dir):
        os.mkdir(books_dir)

    # Creds Stuff

    if not os.path.exists(creds_dir):
        os.makedirs(creds_dir)

    if not os.path.exists(creds_file):
        print(Fore.RED + "[-] " + Fore.RESET + "Credentials file not found. Please place credentials.json in " + creds_dir)
        exit()
    
    print(Fore.GREEN + "All System Checks Passed" + Fore.RESET)

def get_service():

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            creds = pickle.load(token)
    else:
        creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                creds_file, ['https://www.googleapis.com/auth/drive'])
            creds = flow.run_local_server(port=0)
        with open(pickle_file, 'wb') as token:
            pickle.dump(creds, token)

    # Build the Google Drive API service
    service = build('drive', 'v3', credentials=creds)
    
    return service

html_to_use = [

"""<!DOCTYPE html>
<html lang="en">
<head>

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-0KZX48SLMJ"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-0KZX48SLMJ');
</script>

""",

"""
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <meta 
        name="description"
        content="Author: gndpnwd
        Free PDF books. 
        Valuable content for free. 
        No ads, no paywalls, no bullshit.">
""",

"""
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/grid.css">
    <link rel="stylesheet" href="css/button.css">
""",

"""
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/grid.css">
    <link rel="stylesheet" href="../css/button.css">
""",


"""
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
""",

"""
    <a href="https://books.dev00ps.com">
        <img class="title" src="assets/free_books.webp" alt="Free Books" stye="width:563px;height:251px;">
    </a>
""",

"""
    <a href="https://books.dev00ps.com">
        <img class="title" src="../assets/free_books.webp" alt="Free Books" stye="width:563px;height:251px;">
    </a>
""",

"""\n\n    <div class=\"grid-container\">""",

"""
    </div>
</body>
</html>
"""

]

def get_good_data():

    fancy_print("Analyzing Files in Google Drive...", "", 0)
    service = get_service()

    # Step 4: List folders in Google Drive
    folders = service.files().list(q="mimeType='application/vnd.google-apps.folder' and trashed=false", fields="nextPageToken, files(id, name, createdTime)").execute().get('files', [])
    folders = sorted(folders, key=lambda x: x['name'])
    
    all_folders = []
    all_files = []
    
    total_num_folders = 0
    total_num_books = 0

    # Step 5: List files in each folder
    folders_pbar = tqdm(folders)
    for folder in folders_pbar:
        # add current folder name to list if not already in list
        if folder not in all_folders:
            all_folders.append(folder['name'])

        folders_pbar.set_description(Fore.GREEN + "Processing Folder: " + Fore.RESET + str(folder['name']) + Fore.GREEN)

        files = service.files().list(q="'{}' in parents and trashed=false".format(folder['id']), fields="nextPageToken, files(id, name, createdTime, webViewLink, permissions)").execute().get('files', [])
        files = sorted(files, key=lambda x: x['name'])
        
        # Step 6: Check if file has "anyone" permission with "reader" role
        # If not, add the permission and record file URL for each file
        files_pbar = tqdm(files)
        curr_files = []

        total_num_folders += 1

        for file in files_pbar:


            files_pbar.set_description(Fore.YELLOW + "Analyzing " + Fore.RESET + str(file['name']) + Fore.YELLOW)
            
            # store file info in list
            file_info = []

            try:
                # Check if anyone has "reader" role on the file
                permissions = service.permissions().list(fileId=file['id'], fields="permissions(type,role)").execute()
                has_anyone_reader_permission = any(p.get("type") == "anyone" and p.get("role") == "reader" for p in permissions.get("permissions", []))
                if not has_anyone_reader_permission:
                    # Add "anyone" permission with "reader" role
                    permission = {'type': 'anyone', 'role': 'reader'}
                    service.permissions().create(
                        fileId=file['id'], body=permission, sendNotificationEmail=False).execute()

                # Get file URL and name
                file_url = 'https://drive.google.com/file/d/{}/view?usp=sharing'.format(file['id'])
                file_name = file['name']

                file_info.append(file_name)
                file_info.append(file_url)
                # Print file information
                #print(f"name: {file_name}")
                #print(f"url: {file_url}\n")

                total_num_books += 1
            except HttpError as error:
                print(f'An error occurred: {error}')
            
            # the list of file info is stored in the list of files in the current folder
            curr_files.append(file_info)
        # the list of list of file info is stored in the list of all files
        all_files.append(curr_files)
    
    print(Fore.GREEN + "File Analysis Successful")
    print(Fore.RESET + "Total Books In Google Drive: " + Fore.CYAN + str(total_num_books))
    print(Fore.RESET + "Total Folders (Categories) In Google Drive: " + Fore.CYAN + str(total_num_folders))
    return all_folders, all_files

def gen_site(folders2use, files2use):

    fancy_print("Generating books.html...", "", 0)
    
    with open(book_index_file, "w") as f:
        
        f.write(html_to_use[0])
        f.write(html_to_use[1])
        f.write(html_to_use[2])
        f.write(html_to_use[4])
        f.write(html_to_use[5])
        f.write(html_to_use[7])
        
        category_num = 1

        for folder in folders2use:
            category_name = folder.replace("_", " ").replace(".pdf", "").title()
            link_name = category_name
            html_code = (f"""  
        <div class="grid-item">
            <button class="normal_button"><span onclick="window.open('books/{link_name}.html')"><strong>#{category_num}</strong><br>{category_name}</span></button>
        </div>
        """)
            f.write(html_code)
            category_num += 1
    
        f.write(html_to_use[8])
        f.close()
    
    fancy_print("Creating category pages...", "", 0)

    for folder in folders2use:
        #print(folder)
        category_name = folder
        link_name = category_name.replace(" ", "_").title()
        file2write = os.path.join(books_dir, f"{link_name}.html")
        fancy_print("Creating " + file2write + "...", "", 1)
        #print(file2write)
        
        folderindex = folders2use.index(folder)
        with open(file2write, "w") as f:
            f.write(html_to_use[0])
            f.write(html_to_use[1])
            f.write(html_to_use[3])
            f.write(html_to_use[4])
            f.write(html_to_use[6])
            f.write(html_to_use[7])

            book_num = 1
            for file in files2use[folderindex]:
                book_name = file[0].replace("_", " ").replace(".pdf", "").title() + ""
                #print(File Name: " + file[0])
                #print(File URL: " + file[1])
                html_code = (f"""
        <div class="grid-item">
            <button class="normal_button"><span onclick="window.open('{file[1]}')"><strong>#{book_num}</strong><br>{book_name}</span></button>
        </div>
        """)
                f.write(html_code)
                book_num += 1

            f.write(html_to_use[8])
            f.close()

    fancy_print("Done!", "", 0)
                

sys_checks()
folders2use, files2use = get_good_data()
#print(folders2use)
#print(files2use)
gen_site(folders2use, files2use)