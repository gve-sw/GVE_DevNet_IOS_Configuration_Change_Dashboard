# GVE_DevNet_app_template
Flask template application for GVE DevNet team






| :exclamation:  External repository notice   |
|:---------------------------|
| This repository is now mirrored at "PLEASE UPDATE HERE - add External repo URL after code review is completed"  Please inform a https://github.com/gve-sw/ organization admin of any changes to mirror them to the external repo |
## Contacts
* Jorge Banegas
* Ramona Renner 

## Solution Components
* flask
* python
* javascrpt
* html
* css
* charts.js SDK

## Installation

It is recommend to set up your environment as followed, to use this frontend template:

In the CLI:
1.	Choose a folder, then create and activate a virtual environment for the project
    ```python
    #WINDOWS:
    py -3 -m venv [add name of virtual environment here] 
    source [add name of virtual environment here]/Scripts/activate
    #MAC:
    python3 -m venv [add name of virtual environment here] 
    source [add name of virtual environment here]/bin/activate
    ```

2. Access the created virtual enviroment folder
    ```python
    cd [add name of virtual environment here] 
    ```

3.	Clone this Github repository into the virtual environment folder.
    ```python
    git clone [add github link here]
    ```
    For Github link: 
        In Github, click on the **Clone or download** button in the upper part of the page > click the **copy icon**
        ![/IMAGES/giturl.png](/STATIC/IMAGES/giturl.png)

4. Access the folder **GVE_DevNet_app_template**
    ```python
    cd GVE_DevNet_app_template
    ```

5.	Install dependencies
    ```python
    pip install -r requirements.txt
    ```


## Usage

### Structure of this frontend template

This template provides the basic elements and structure of a Cisco prototype. It includes a basic flask app, a bot token scripts, a UI component library and sample template pages.

* **Masterpage.html:** HTML file that provides header and footer elements for all the template pages.

* **Template Pages:** HTML pages for different use cases. Choose the prefered templates for your own application e.g. login, table, settings, 3 Columns 

* **Helper Templates:** HTML files with elements which are used in multiple templates - define it once and use it multiple times. e.g alert, menu. 

* **App.py:** python script with main function and routes

* **Requirements.txt:** file that lists all used python libraries

* **Collage.html, pie.html, bar.html, line.html:** html pages with UI components as reference


### Customization of the Template

To create you own prototype based on this template. We suggest you to start with the following steps:

### Choose the Template
This frontend template includes different templates. Choose the ones that fit your needs best. Adapt the app.py file to only include the routes you use and feel free to remove the unused Template Page HTML files. 

####  Choose between the Cisco and Meraki Design
This template offers a Cisco and a Meraki style. Thereby please comment or uncommend the Cisco Design or Meraki Design sections depending on the style you want to leverage. The sections that require you to choose are marked with a **"CHOOSE"** comment.
    ![/IMAGES/0image.png](/STATIC/IMAGES/Choose1.png)

#### Add customized Values and Titles
To customize the template based on your use case you can e.g. add a title or customize the menues. The sections that require you to fill in text or customize are marked with a **"CUSTOMIZE"** comment.
    ![/IMAGES/0image.png](/STATIC/IMAGES/Choose2.png)

#### Pass Information to the Template
The frontend template offers the possibility to show, hide or fill elements based on variables passed to the template e.g. hide header links on login page, show/hide error when happening. Elements of this type are marked with a **"PASS INFO"** comment. 
    ![/IMAGES/0image.png](/STATIC/IMAGES/Choose3.png)

### Environment Variables
This project contains a .env file in which you can include any keys or credentials.

e.g. 
![/STATIC/IMAGES/0image.png](/STATIC/IMAGES/env_variable.png)

### Charts javascript libary
Some template html pages contains sample code using Charts javascript library. Change the "type" parameter for different diagrams

e.g. 
![/STATIC/IMAGES/0image.png](/STATIC/IMAGES/js_charts_example.png)

# Screenshots of the Templates

## Line Charts for Data Driven PoVs
![/IMAGES/0image.png](/STATIC/IMAGES/lines.png)

## Bar Charts for Data Driven PoVs
![/IMAGES/0image.png](/STATIC/IMAGES/bars.png)

## Pie charts for Data Driven PoVs
![/IMAGES/0image.png](/STATIC/IMAGES/pies.png)



### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
