# Blank Flask App
## Table of content
- [Term of use](#term-of-use)
- [Project Description](#project)
- [Structure](#structure)
- [Files Description](#files-description)
- [Authors](#authors)
#
## Term of use
By using this "Blank" application, you agree to the following terms:

1. __Copyright Notice__ :
    - All files and code within the ___"Blank"___ application are protected by copyright laws.
    - Users of the application must retain the original copyright notice at the top of each file.
2. __Permitted Use__:
    - You are granted permission to use the ___"Blank"___ application for personal or commercial purposes.
3. __No Warranty__:
    - The ___"Blank"___ application is provided "as is" without any warranty, expressed or implied.
    - The developers of the application cannot be held responsible for any damages or liabilities arising from its use.
4. __Modification and Redistribution__:
    - You may modify the ___"Blank"___ application to suit your needs, provided that you retain the original copyright notice.
    - Redistribution of the modified application must include a notice indicating the changes made.
5. __Compliance with Laws__:
    - Users of the ___"Blank"___ application must comply with all applicable laws and regulations in their jurisdiction.

__Please read these terms carefully before using the _"Blank"_ application. By using the application, you acknowledge that you have read, understood, and agreed to be bound by these terms of use__.

If you __do not agree__ with any of these terms, you are __not permitted to use__ the ___"Blank"___ application.

Date of Last Revision: 2023 Mai 16th

For any questions or concerns regarding these terms, please contact us at info@moneysmartinvestmentgroup.com.
#
## Project
This project are built only as a basic Flask application to save time
#
## Structure : 
    

    |-- Procfile
    |-- README.md
    |-- index.py
    |-- project
    |   |-- __init__.py
    |   |-- __pycache__
    |   |   |-- __init__.cpython-310.pyc
    |   |   |-- config.cpython-310.pyc
    |   |   |-- database.cpython-310.pyc
    |   |   |-- factory.cpython-310.pyc
    |   |   |-- forms.cpython-310.pyc
    |   |   |-- route.cpython-310.pyc
    |   |   |-- stuff.cpython-310.pyc
    |   |   `-- time.cpython-310.pyc
    |   |-- config.py
    |   |-- database.py
    |   |-- factory.py
    |   |-- forms.py
    |   |-- route.py
    |   |-- static
    |   |   `-- images
    |   |-- stuff.py
    |   `-- templates
    |       |-- en
    |       |   |-- home.html
    |       |   `-- maintemplate.html
    |       `-- fr
    |           |-- home.html
    |           `-- maintemplate.html
    `-- requirements.txt
#
## Files Description

    Procfile
    Used for deployment on railway.app
#
    README.md
    Actual file
#
    index.py
    Used for start the app (virtual and production environement)
#
    project (directory)
    All app file on this directory
#
    __init__.py
    Use to create var for the app
#
    __pycache__ (directory)
    Some cache file the app need to work
#
    config.py
    Can be use to put configuration for the app
#
    database.py
    Setup table for the MySQL database
#
    factory.py
    Initializing db and app var, write the table in db if empty
#
    forms.py
    All class form here
#
    route.py
    Route for the app
#
    static (directory for static file)
#
    images (directory)
    For images
#
    stuff.py
    All the confidential informations for running the app
#
    templates (directory)
    For html files
#
    en (directory)
    Put english file here (default / or home or index)
#
    home.html
    Content for english home webpage
#
    maintemplate.html
    Content for english static content like menu
#
    fr (directory)
    Put french file here (francais) 
#  
    home.html
    Content for french home webpage
#
    maintemplate.html
    Content for french static content like menu
#
    requirements.txt
    Requirement module to run the app (let there for zope.interface and gunicor for using with railway.app)
#
## Authors
Build by MSIG team 