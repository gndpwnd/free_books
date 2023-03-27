# About

Valuable content for free.

### Projects Goals

- To accumulate knowledge for success in life
- To store such knowldege in an easily accessable library
- To condense the size of such library to fit the completion of reading withing an average lifespan

### Convert PDF to Audio Book

I use [this script](https://gist.github.com/gndpwnd/cfaa8ee83c24c01c2da7a3ebf44ea97f) to convert PDFs to TXT files. Essentially generate a list of sentences, then a bit of manual tweaking of the TXT file to help normalize the workload for the next tool.

I then use [this site](https://audio.online-convert.com/convert/txt-to-mp3) to convert the TXT files into an audible MP3 file.

Additionally, while it is very limited for free use, [Zamazar](https://zazmar.com) provides an alternative for the conversion of TXT to MP3.

### Making Suggestions

1. Create a list of books
   1. Include full title
   2. Include author
   3. [Example books list](https://raw.githubusercontent.com/gndpwnd/free_books/main/mass_add_books/example_book_list.md)

2. Start creating a new file [here](https://github.com/gndpwnd/free_books/new/main/mass_add_books)

3. Copy your booklist to the file

4. Click the green button below to: 
   1. commit the new file
   2. iniate a new pull request

## Notes for making a backup of the library

> Reference [here](https://thatcoder.space/download-files-from-digital-ocean-spaces/)


1. First, Install AWS CLI from here (https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)

2. Open a new terminal and run the following:

```
aws configure
```

3. Enter the access key and secret key, then leave everything else blank.

4. Now to download the files from the *archive-books* folder in the *dev00psarchive* space
   1. Note: This command will download everything to the current directory

```
aws s3 cp --recursive --endpoint=https://nyc3.digitaloceanspaces.com s3://dev00psarchive/archive-books/ ./
```

## Public Backup


[AnonFiles Publication]()