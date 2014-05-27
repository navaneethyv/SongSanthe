SongSanthe
====================
For those who like music!!
Built on pinax

Install Dependencies
====================
    $ #only in ubuntu
    $ sudo apt-get install redis-server 
    $ sudo apt-get install graphviz
    $ sudo apt-get install tcl8.5
    $ sudo apt-get install python-imaging
    $ sudo apt-get install python-dev
    $ sudo apt-get install python-virtualenv
    $ #ubuntu specific done

Clone The Code
====================
    $ git clone https://<your_bibucket_username>@bitbucket.org/navaneethbhat/songsanthe.git 
    $ mv songsanthe ss   #(renaming for readabilty)
    $ virtualenv ss
    $ source ss/bin/activate
    (ss)$ pip install Django==1.5.1
    (ss)$ cd ss/songsanthe
    (ss)$ pip install -r requirements.txt
    (ss)$ python manage.py syncdb
    (ss)$ python manage.py runserver

Hit http://127.0.0.1:8000 to view the site!

What's Done
===============

 * user profiles which are hooked up to the sign up process
 * Import friends list from facebook and google and recommend such friends
 * Importing task assigned to a celery que to make sure that reply does not stop 

