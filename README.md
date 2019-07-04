# Record-Link-Reconciler
The purpose of this tool is to reconcile record links after a file migration

## Table of Contents
* [Tool Introduction](#tool-introduction)
* [Use Case Overview](#use-case-overview)
* [Using the Record Link Reconciler](#using-the-record-link-reconciler)
  * [Downloading the Tool](#downloading-the-tool)
  * [Setting up Environment](#setting-up-environment)
    * [Setting up Python](#setting-up-python)
    * [Setting up Folder](#setting-up-folder)
  * [Running the Tool](#running-the-tool)

## Tool Introduction

The Record Link Reconciler tool is specifically designed to be used to reconcile broken record (file) links when files are migrated to a new system. The tool is written completely using Python, and is designed for use with Python 2.7. Other versions of Python should work, but not all functionality is guaranteed. 

## Use Case Overview

The Record Link Reconciler tool should only be used after a large-scale File Migration where record links or file links might have been broken. The specific use case used to design this tool was a migration from an on-premeses server to a cloud storage provider, such as Microsoft OneDrive and SharePoint. This tool may be useful for other use cases, such as server to server, but functionality is not guaranteed.

## Using the Record Link Reconciler

In this section, you will find everything you need to run the Record Link Reconciler Tool. There is no formal user interface for this tool, and everything is done completely in Terminal or Command Prompt, depending on the OS on your system. 

### Downloading the Tool

The Record Link Reconciler tool can be downloaded from GitHub, at https://github.com/jacobjhansen/Record-Link-Reconciler 
There are two ways to download the tool to your computer:

1. Clone Repository using git
  * If you have git properly installed on your system, navigate to your desired folder and run this command in Terminal/Command Prompt:
  `git clone https://github.com/jacobjhansen/Record-Link-Reconciler.git`
2. Download ZIP Archive of Repository
  * If you do not have git properly installed on your system, you can click the 'Clone or Download' button on GitHub and click 'Download as ZIP'

### Setting up Environment

There are two main steps needed to set up your Environment to use the Record Link Reconciler Tool:

#### Setting up Python

Python must be properly installed on your system to use this tool. Python 2.7 was used in the development of this tool, and can be downloaded [here](https://www.python.org/download/releases/2.7/)
You can check if python is installed on your system by learning more [here](https://www.wikihow.com/Check-Python-Version-on-PC-or-Mac)

#### Setting up Folder

The project folder must also be set up properly for this tool to work. Because no formal user interface is given, there is no way for a user to specify files listing old or new files, or to set up an output file. Because of this, all input files must replace placeholder files in the project folder. 

There are two input files necessary for the project:

1. CurrentRecordLinks.csv
The format of this file MUST BE as follows:
[LINK ID],[RECORD ID],[CUSTOMER/VENDOR],[URL1],[FILE NAME]
HEADER ROW MUST NOT BE PRESENT

2. NewLocationFiles.csv
The format of this file MUST BE as follows:
[FILENAME], [FILEPATH], [SIZE], [EXTENSION]
HEADER ROW MUST NOT BE PRESENT

Both files must be properly formatted, and header rows and extraneous columns must be removed. 

The other .CSV file visible in the folder is `Reconciliation.csv`. This is the output file from the tool. This output file shows the file, its old location, and its new location.

### Running the Tool

In order to run the tool, these steps must be followed:

1. Open Terminal/Command Prompt
2. Navigate to the project folder using `cd`
3. Run the Script
  * Windows Users:
    * `py parse.py`
  * MacOS/Linux Users:
    * `python parse.py`

The script will show current progress in the terminal window, and will print completion info upon completion. You can now find the link reconciliation data in the file `reconciliation.csv`