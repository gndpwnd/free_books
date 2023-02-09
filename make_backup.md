# Notes for making a backup of the library

> Reference [here](https://thatcoder.space/download-files-from-digital-ocean-spaces/)


1. First, Install AWS CLI from here (https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)

2. Open a new terminal and run the following:

```
aws configure
```

3. Enter the access key and secret key, then leave everything else blank.

4. Now to download the files from the *archive-books* folder in the *dev00psarchive* space

```
aws s3 cp --recursive --endpoint=https://nyc3.digitaloceanspaces.com s3://dev00psarchive/archive-books/ ./
```

Note: This command will download everything to the current directory