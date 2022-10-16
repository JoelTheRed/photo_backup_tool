# photo_backup_tool
A script to find duplicate images and backup to a secondary directory using the [difPy tool](https://github.com/elisemercury/Duplicate-Image-Finder).
There is an option to remove the backed up images from the source directory. This is useful when consolidating files whilst avoiding duplication.

There are other methods that can be used e.g. file metadata or hashes, however DifPy compares images based on their hashes. It compares them based on their tensors i.e. the image content.

Pre-requisites:

- difPy

Installation:

```pip install difPy```

Usage:
1. Simply run the command:

```Photo_backup_tool.py```

2. Input your source folder path e.g.:

```C:/path/to/folder```

3. Input your destination or backup folder path e.g.:

```F:/path/to/backup_folder```
