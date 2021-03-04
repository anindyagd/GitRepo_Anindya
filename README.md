# GitRepo_Anindya
This is a new repository which holds a webservice which take address as input and return the state name as output.
This repository has a file called Web_API_Address_to_State.py. This is an web service which takes an endpoint that accepts an address, converts it to a lat/long (using Google API), and finds which state contains that point. So this webservice take address as input and return the state name as output.

Steps to run the webservice from shell 
1. Save the file in a unix/windows location. update the script with google key in the given place. Then Go to that path then run the command "python Web_API_Address_to_State.py", and if you are running it in your default host you will get output like below.

 //Serving Flask app "Web_API_Address_to_State" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) //
 
 So the webservice is runnin on the host 127.0.0.1 and port 5000. Now if you go the host http://127.0.0.1:5000/ and pass any addrsess like http://127.0.0.1:5000/30004 or http://127.0.0.1:5000/<any address>, it will retun the state name of that address. Apart from address you can retun information like zipcode, lat/long etc. Go to the below image to view how the result will come. i have passed a zip code only but this api can take any type of address and return the State name. 
  
  ![image](https://user-images.githubusercontent.com/80070091/110030355-9c902b80-7d03-11eb-9ecb-49c999f2ce07.png
  
  This is the way this application can be run in a stand alone mode.
  
  Running the Application from Docker Container:
  
  We can run the application from docker engine as well. To do so install the Docker based on the OS platform. once it is ready check docker service is running properly or not.If it is working fine. Create the dockerfile in the same location where the script is preent. I have added the dockerfile file in the repostitory. For dependancise we have to create a requirements.txt file. This file will have all the dependancies. Once it is completed go to shell and execute the below steps in the same location where these files are present.
  
  docker build . <One the image is build>
  docker run <image_name> ....<to execute the application from docker. Now there are few run options are present in docker to set the ip, port and other details so those options can be used>
  
  once the run is executed it will give the similar output when the script executed seperately and in the same output will come in the localhost when any address will be passed and State will be returned. Check the below screenshot to see how the docker image was build and how it execute the wbe service.
  
  ![image](https://user-images.githubusercontent.com/80070091/110031978-9ac76780-7d05-11eb-9c5f-07e8c1848f7b.png)

  So Webservice is created with Python and running with Docker.
  
  Apart from that I have created one more table in postgresql from a shapefile. The file has few geo location details. To load the file in postgresql in step 1. I installed the postgresql in my local mechine. 
  Then create a account with username and password. 
  Then create database schema in postgresql with that smae account. 
  Then import the shapefile in that database server with file import utility and while import the file selete the option to create it as a table in postgresql schema with same name as the file name. 
  Once the import it done, go to PGAdmin and do login to the acount and database with same username and password. 
  Now go to query_tool from tool and execute the select statment over that table to get the data. Now this table can be integrated with webservice to insert new or extract existing data from that table. The below screenshot is from my local mechine wheren a select query over that table in PG Admin with query_tool.
  
  ![image](https://user-images.githubusercontent.com/80070091/110034463-7c16a000-7d08-11eb-918d-37e8cbc4d7bd.png)
