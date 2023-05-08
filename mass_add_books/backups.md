## Convert PDF to Audio Book

I use [this script](https://gist.github.com/gndpwnd/cfaa8ee83c24c01c2da7a3ebf44ea97f) to convert PDFs to TXT files. Essentially generate a list of sentences, then a bit of manual tweaking of the TXT file to help normalize the workload for the next tool.

I then use [this site](https://audio.online-convert.com/convert/txt-to-mp3) to convert the TXT files into an audible MP3 file.

Additionally, while it is very limited for free use, [Zamazar](https://zazmar.com) provides an alternative for the conversion of TXT to MP3.


## Make a backup of your library from Digital Ocean

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

## Backing Up From Google Drive 

1. Download Google Drive For Desktop [here](https://www.google.com/drive/download/)
    1. Run the installer
    2. Sign in with your Google Account
2. Navigate to your google drive on your PC's physical drive 
    1. Copy the folders and files you would like to backup to a new location


## Backing Up From Mega 

1. Download MegaSync [here](https://mega.nz/sync)
    1. Run the installer
    2. Sign in with your Mega Account
2. Navigate to your Mega Drive on your PC's physical drive
    1. Copy the folders and files you would like to backup to a new location