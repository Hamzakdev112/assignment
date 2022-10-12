# Tutorial assignment to implement a blog using vue and django

The django has been written, and there is one template for you to fill in to make a one page CRUD application by use of the Django APIs.

Once you have cloned this project, fork it and push the solution to your own repo. Send me the link so I can clone it and test your solution

**NOTE: DO NOT PUSH YOUR SOLUTION BACK TO THE ORIGINAL REPOSITORY. THE REPOSITORY IS PUBLIC, BUT NOT READ ONLY. YOU MUST MAKE A NEW REPOSITORY IN YOUR OWN ACCOUNT THAT I CAN PULL YOUR SOLUTION FROM**



# Local Installation #
Running the API is all done through launching their respective container using the [Docker](https://www.docker.com/) 
configuration files in the application root, Dockerfile and docker-compose.yml

These instructions assume a unix based platform running a bash console from the project root directory.

#### Requirements ####

Running the server requires the following to be installed on your computer, and I believe behave the same way on Linux/MacOS/Windows:  

* ***Docker***  
* ***docker-compose***  

#### Building the project

First copy the database sql lite file to the application directory:

```bash
project-root$ cp initial_database.sqlite3 django_vue/db.sqlite3
```

To build the container

```bash
# Local build
host$ docker-compose up
# In another terminal
host$ docker exec -it $(docker ps | awk '/django_vue/ && !/awk/ {print $1}') bash
root@bc511b4275ea:/app$ runserver
# Exposes "http://localhost:8080/" with an index page which will explain the tutorial, and show links to the API endpoints
```

#### Usage ####
On localhost, the root page shows all the information you need for this assignment:
http://localhost:8000/
You can also log in to django admin where you can see and update the data.
http://localhost:8000/admin/
with username 'admin' and password 'password'. 

#### Endpoints ####
The endpoints are listed in the root page. You can also view the yaml file of API endpoints here
http://localhost:8000/schema.yml
