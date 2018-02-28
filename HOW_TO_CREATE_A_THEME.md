# How to create a theme

## The directory structure
> Your directory structure should look something like this:

    example_theme/
    ├── db.json ----------------------------- # not really needed
        ├── static/ ------------------------- # static files goes here
        │   ├── css/
        │   │   ├── font-awesome.min.css
        │   │   ├── main.css
        │   │   ├── noscript.css
        │   │   ├── style.css
        │   │   ├── style.css.map
        │   │   └── style.scss
        │   ├── image/
        │   │   ├── bg.jpg
        │   │   ├── overlay.png
        │   │   ├── pic01.jpg
        │   │   └── pic09.jpg
        │   └── js/
        │       ├── main.js
        │       ├── skel.min.js
        │       └── util.js
        └── templates/ ---------------------- # the system will look for templates here
            ├── generic.html
            ├── index.html
            └── layout.html

> Please checkout the [example theme](example_theme) for more information  
> about the structure.

## Writing templates
> Templates are written using Jinja2 and html.
> please look at the [Jinja2 documentation](http://jinja.pocoo.org/docs/2.10/templates/)  
> for more information.

### Making your website editable
> In your layout, insert the admin navigation right after yout `<body>` tag:

    <body>
        {{ admin_navigation(post, page) }}

        ...

> __EXACTLY__ like above and you will be all set!

### editable areas in templates
> We are using the medium editor for editable areas, to make an area editable
> while singed in, we do this:

    <!-- my-startpage.html -->

    
    <h1 class='editable' id='important-text'>about page</h1>

* Add the class `editable` to your element
* Add an `id`.
* Add a default value.

> The data will be stored along with it's ID, the value of the element
> and the page ID.

> All ids per page needs to be unique.

> This element is now editable:  
![editable gif](screenshots/editable.gif)

## Global variables
> Here are some global variables that can be accessed in your template:

* post - only accessable if a post is using the template
* page - only accessable if a page is using the template
* PageFacade - used to query pages
* PostFacade - used to query posts

## Accessing static files
> Accessing static files is easy, here is an example:

    <!-- my-template.html -->
    
    
    <img src='/theme/static/image/bg.jpg'/>

## Listing posts in your template
> Use the `PostFacade` to query posts.

    {% for post in PostFacade.get_all(offset=3, limit=100) %}
        <div class='post'>
            <h1>{{ post.name }}</h1>
            <p>{{ post.content }}</h1>
        </div>
    {% endfor %}

> This was just an example!

> The `post` object has some accessible fields, such as `name` and `content`  
> for more fields [click here](FIELDS_POST.md).

## Listing pages
> The same as above, but use the `PageFacade` instead!

## Custom page fields
> Pages can have custom fields, to enable them, add a `<template-name>.json` file
> next to the `<template-name>`.html file in your templates directory.

> The `.json` file can look something like this:

    {
        "fields": {
            "bannerImage": {
                "type": "asset"
            }
        }
    }

> And then in your `<template-name>.html` you can access that field like this:

    <div class='my-cool-container'>
        <img src='/uploads/{{ page.get_field('bannerImage').filename }}'/> 
    </div>

> When creating a page using this template, the CMS user will be able to upload
> a file to the `bannerImage` field.

> We currently only support fileds with the type `asset`.

## db.json
> This is where theme-specific data is stored, can be accessed in themplates
> by using the global `db` variable, like this:
    
    <!-- my-template.html -->
    

    <div>
        <span>{{ db['my-cool-text'] }}</span>
    </div>


> It is recommended to store all default values in db.json when creating it.
