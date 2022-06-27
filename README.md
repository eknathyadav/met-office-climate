# Met Office Climate API

Created a Django application to parse summarised weather data from UK MetOffice and serve it via Django Rest API





## Technologies

**Django:** The web framework for perfectionists with deadlines (Django builds better web apps with less code).

**Django Rest Framework:** A powerful and flexible toolkit for building Web APIs




## Overview

In this project, I have extracted climate related data of all the regions in UK with all the temperature parameters from met Office. And then I have loaded the extracted Data into sqlite using Django ORM. For serving the data, I have created Django REST APIs. For now the API will server data, starting from 2012 to 2021

For Extraction, I have used beautifullsoup4. You can view the whole extraction code in core/views.py/. 
I have commented the extraction part since I have already extracted the data.

To run the extraction from scratch,Uncomment the extraction code, clear the db and run the server. Visit http://127.0.0.1:8000/ and click "Extract Data". Extraction will take few minutes.



## API Reference

API will accept two parameters, region_name and parameter_name.

Valid **Regions : [UK,  England, Wales, Scotland, Northern_Ireland,
                   England_and_Wales, England_N, England_S, Scotland_N,
                   Scotland_E, Scotland_W, England_E_and_NE, England_NW_and_N_Wales,
                   Midlands, East_Anglia, England_SW_and_S_Wales, England_SE_and_Central_S]**

Valid **Parameters : ["Tmax", "Tmin", "Tmean", "Sunshine",
                      "Rainfall", "Raindays1mm", "AirFrost"]**


#### API Endpoints


| API | Required Parameter     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `http://127.0.0.1:8000/api/regions-list/`      | None | To get all the climate related data of all the regions|
| `http://127.0.0.1:8000/api/regions-list/${parameter_name}/`      | parameter_name | To get climate related data of all the regions with parameter of choice|
| `http://127.0.0.1:8000/api/region-climate/${region_name}/`      | region_name | To get climate related data of a particular region|
| `http://127.0.0.1:8000/api/region-climate/${region_name}/${parameter_name}/`      | parameter_name, region_name | To get climate related data of a particular region with parameter of choice|

## Installation

1. Clone the project
    ```
    git clone https://github.com/eknathyadav/met-office-climate.git
    ```
2. Install required packages
    ```python
    pip install Django
    pip install djangorestframework
    pip install beautifulsoup4
    ```
3. Access the met-office-climate folder

4. Run the Django Server
    ```
    python manage.py runserver
    ```
5. Copy http://127.0.0.1:8000/ and paste it on your browser.

6. Use the API Endpoints By referring to API Reference.

## Screenshots
![regions-list](https://user-images.githubusercontent.com/48616375/176000583-729fbfb5-a801-4a49-94cb-de87116b1895.PNG)

![regions-parameter](https://user-images.githubusercontent.com/48616375/176000606-96dc2f87-2de6-419a-aacb-f1e3912a4a36.PNG)

![get-region](https://user-images.githubusercontent.com/48616375/176000616-845428f2-ffd4-4b78-9bcd-6c0e4d8ce095.PNG)
![get-region-parameter](https://user-images.githubusercontent.com/48616375/176000637-1815396f-1400-45b3-a377-f01bf6969392.PNG)




    
