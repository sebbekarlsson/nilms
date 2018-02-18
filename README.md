# nilms
> A content management system with built-in on-sight page editing
> that does as little as possible.

## Installation
> Requirements:

    * python 2.7
    * a running instance of MongoDB

> First, let us create a config file:

    cp config.example.json config.json

> Edit it using your favourite editor.

### Create a virtualenv

    virtualenv -p /usr/bin/python2.7 ./venv
    
    # source it
    source ./venv/bin/activate

### Install nilms
> Run the setup:

    python setup.py develop

### Start the application

    python web.py

> Now visit [http://localhost:5000/admin](http://localhost:5000/admin)  
<img src='screenshots/login.png' width='150px'/>  

> The login credentials is in your `config.json`

## How it works
* 0 Create a theme. [how to create a theme](HOW_TO_CREATE_A_THEME.md)
* 1 In your `config.json`, specify where your theme is by changing the `theme_dir` value.
* 2 Login and start creating pages.
