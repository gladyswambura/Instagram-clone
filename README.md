## Instagram-Clone

 ## By 
 - Gladys Wambura 

 ## Description 

 This is a clone ofthe popular app instagram!.

![image](https://user-images.githubusercontent.com/97955649/172501535-d19e210d-45cc-4376-b6ed-f28f1858106a.png)


 ## User Story
- Users need to Sign in to the application to start using.

- Users can view various posts.

- Users can search for other users using the username.

- Users can add their posts to the application.

- Users can see their full profile via the dropdown on the navbar.


### Installion and Setup instructions

*** To view the app.Visit -> [GlaGram](https://gladysgram.herokuapp.com/)

1. Clone this repo: git clone [Github](https://github.com/gladyswambura/Instagram-clone)
2. The repo comes in a zipped or compressed format. Extract to your prefered location and open it.
3. open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer  [here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
3. To run the app, you'll have to run the following commands in your terminal:

     
    i). On your terminal,Create database gallery using the command below.
         
           CREATE DATABASE instagram; 
           **if you opt to use your own database name, replace instagram your preferred name, then also update settings.py variable DATABASES > NAME

    ii). Migrate the database using the command below
      
           python3 manage.py makemigrations 
           python3.8 manage.py migrate
       
    iii). Then serve the app, so that the app will be available on localhost:8000, to do this run the command below
    
           python3 manage.py runserver
           
4 Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.

## TECHNOLOGIES Used

* [Django](https://www.djangoproject.com/) - web framework used
* Javascript - For DOM(Document Object Manipulation) scripts
* HTML - For building Mark Up pages/User Interface
* CSS - For Styling User Interface

## Contacts
**gladyswahito7@gmail.com**

## live link : https://gladysgram.herokuapp.com/

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
