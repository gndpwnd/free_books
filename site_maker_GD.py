import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from tqdm import tqdm
from colorama import Fore

# Replace with your own credentials file
creds_dir = "creds"
creds_file = os.path.join(creds_dir, "credentials.json")
pickle_file = os.path.join(creds_dir, "token.pickle")

host_dir = os.path.realpath(__file__).split("book_list_generator.py")[0]
out_dir = os.path.join(host_dir, "docs")
books_dir = os.path.join(out_dir, "books")

book_index_file = os.path.join(out_dir, "books.html")
audio_book_index_file = os.path.join(out_dir, "audiobooks.html")
main_index_file = os.path.join(out_dir, "index.html")

prog = Fore.GREEN + "[+] " + Fore.RESET

all_folders = []
all_files = []

print(Fore.YELLOW + "Host Dir: " + Fore.RESET + host_dir)
print(Fore.YELLOW + "Out Dir: " + Fore.RESET + out_dir)

def fancy_print(str, val, ind):
        indent = ""
        for i in range(ind):
            indent += "    "

        if val == "":
            print(indent + Fore.GREEN + "[+] " +  Fore.RESET + str)
        else:
            print(indent + Fore.GREEN + "[+] " + Fore.RESET + str + Fore.YELLOW + val + Fore.RESET)

def sys_checks():

    # Site Directories

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    if not os.path.exists(books_dir):
        os.mkdir(books_dir)

    # Creds Stuff

    if not os.path.exists(creds_dir):
        os.makedirs(creds_dir)

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

    service = get_service()

    # Step 4: List folders in Google Drive
    folders = service.files().list(q="mimeType='application/vnd.google-apps.folder' and trashed=false", fields="nextPageToken, files(id, name, createdTime)").execute().get('files', [])
    folders = sorted(folders, key=lambda x: x['name'])
    

    total_num_books = 0

    # Step 5: List files in each folder
    folders_pbar = tqdm(folders)
    for folder in folders_pbar:
        # add current folder name to list if not already in list
        if folder not in all_folders:
            all_folders.append(folder['name'])

        folders_pbar.set_description(Fore.GREEN + "Processing " + Fore.RESET + str(folder['name']) + Fore.GREEN)

        files = service.files().list(q="'{}' in parents and trashed=false".format(folder['id']), fields="nextPageToken, files(id, name, createdTime, webViewLink, permissions)").execute().get('files', [])
        files = sorted(files, key=lambda x: x['name'])
        
        # Step 6: Check if file has "anyone" permission with "reader" role
        # If not, add the permission and record file URL for each file
        files_pbar = tqdm(files)
        curr_files = []

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
                print(f"name: {file_name}")
                print(f"url: {file_url}\n")

                total_num_books += 1
            except HttpError as error:
                print(f'An error occurred: {error}')
            
            # the list of file info is stored in the list of files in the current folder
            curr_files.append(file_info)
        # the list of list of file info is stored in the list of all files
        all_files.append(curr_files)

    print(Fore.RESET + "Total Books: " + Fore.CYAN + str(total_num_books))

def gen_site():
    
    data = get_good_data()
    print(data)

    fancy_print("Generating books.html...", "", 1)
    
    with open(book_index_file, "w") as f:
        
        f.write(html_to_use[0])
        f.write(html_to_use[1])
        f.write(html_to_use[2])
        f.write(html_to_use[4])
        f.write(html_to_use[5])
        f.write(html_to_use[6])
        
        category_num = 1

        for i in range(len(all_folders)):
            category_name = all_folders[i]
            link_name = category_name.replace(" ", "_")
            html_code = (f"""  
        <div class="grid-item">
            <button class="normal_button"><span onclick="window.open('books/{link_name}.html')"><strong>#{category_num}</strong><br>{category_name}</span></button>
        </div>
        """)
            f.write(html_code)
            category_num += 1
    
        f.write(html_to_use[7])
        f.close()
    
    fancy_print("Creating category pages...", "", 1)


#gen_site()

data = get_good_data()
print(data)