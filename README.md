# Scale a Django application using a modular architecture  - OpenClassrooms project 13

This project is about scaling a django application using a modular architecture in order to help 
"Orange County Lettings", a real estate start-up , in its growth. Here are the areas of the site and its deployment 
that have been improved or added:
- Reduction of various technical debts on the project (Linting and admin pluralisation)
- Redesign of the modular architecture (monolithic to microservices)
- Addition of a CI/CD pipeline and site deployment
- Application monitoring and error tracking via Sentry.

## Local development

### Prerequisite

- GitHub account with access to this repository - read only
- Sentry account
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.10

For the rest of this documentation, it is supposed that the python command of your OS shell 
executes the python interpreter aforementioned (unless a virtual environment is activated)

### macOS / Linux

#### Clone the repository

Clone [the repository](https://github.com/Bricevne/P13_lettings.git) on your computer.

```
git clone https://github.com/Bricevne/P13_lettings.git
```

#### Create the virtual environment

Enter your project directory `cd /path/to/P13_lettings`

Set your virtual environment under [python 3.10](https://www.python.org/downloads/release/python-3100/)

```bash
python -m venv venv # Create your virtual environment
apt-get install python3-venv # If the previous step has a package error not found on Ubuntu
source venv/bin/activate # Activate the virtual environment
```

You can then check your virtual environment with:

```bash
which python # Confirm that the `python` command executes the Python interpreter in your virtual environment
python --version # Confirm that the python interpreter version is 3.10
which pip # Confirm that the `pip` command executes the pip executable in your virtual environment
```

To deactivate your virtual environment:

```bash
deactivate
```

#### Site execution

Enter your project directory `cd /path/to/P13_lettings`

Install the requirements in your virtual environment:

```bash
source venv/bin/activate # Activate the virtual environment
pip install --requirement requirements.txt # Install the requirements
```

Create a file where you'll put the django secret key and sentry dsn:

```bash
touch .env # File for environment variables
```

Insert your hidden parameters:

```bash
DJANGO_SECRET_KEY="YOUR_DJANGO_SECRET_KEY"
SENTRY_DSN="SENTRY_DSN"
```

Launch the local server

```bash
python manage.py runserver
```

Go to `http://localhost:8000` in your navigator.

#### Linting

Enter your project directory `cd /path/to/P13_lettings`

Lint check your project

```bash
source venv/bin/activate
flake8
```

#### Unit tests

Enter your project directory `cd /path/to/P13_lettings`

Launch your unit tests with pytest

```bash
source venv/bin/activate
pytest
```

#### Database

Enter your project directory `cd /path/to/P13_lettings`

Connect to the database:

```bash
sqlite3 # Open a shell
.open oc-lettings-site.sqlite3 # Connect to the oc-lettings-site database
```

Check the database information:

```bash
.tables # Display the database tables
pragma table_info(profiles_profile); # display the profile's table columns
select user_id, favorite_city from profiles_profile where favorite_city like 'B%'; # Launch a request on the profiles table
```

Quit the shell

```bash
.quit
```

#### Administration panel

Go to `http://localhost:8000/admin`

Sign in with:
- username: `admin`
- password: `Abc1234!`

### Windows

With PowerShell, do as above except:

- To activate the virtual environment: `.\venv\Scripts\Activate.ps1` 
- Replace `which <my-command>` by `(Get-Command <my-command>).Path`

## CI/CD pipeline via CircleCI and deployment on Heroku

When a branch is pushed to GitHub, CircleCI launches a pipeline whose actions differ depending on the branch:
- Master branch: (1) linting and unit testing, (2) dockerizing and pushing a tagged image to DockerHub if (1) succeeds, (3) deployment on Heroku if (2) succeeds.
- Other branches: only (1) as only the code on the master branch needs to be dockerized and deployed.

### Prerequisite

The following accounts are necessary:

- [CircleCI](https://circleci.com/signup/)
- [DockerHub](https://hub.docker.com/)
- [Heroku](https://signup.heroku.com/) You can interact with Heroku by installing its [CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) .

### Installation

- Create a CircleCI project and link it to your GitHub repository.
- Create a DockerHub project
- Create a Heroku project

You need to set up the environment variables in your CircleCI project. Those will be passed to Heroku through the config.yml file.

- DJANGO_SECRET_KEY
- DEBUG: 0 to pass it in production mode
- DOCKER_USERNAME: your DockerHub username
- DOCKER_PASSWORD: your DockerHub password
- HEROKU_APP_NAME: the name you want to give to your application
- HEROKU_TOKEN: authentication token
- SENTRY_DSN

### Use

Once the master branch is pushed to Github, if the linting and testing processes work, dockerizing and 
deployment processes will proceed.
You can then access the website through https://<HEROKU_APP_NAME>.herokuapp.com/.
For educational purposes, the deployed site can be reached through https://bve-oc-lettings-site.herokuapp.com/.

## Sentry

Sentry is used to manage caught exceptions in your project.

### Prerequisite

- [Sentry account](https://sentry.io/signup/)

### Use

Create a sentry project. A sentry dsn value will then be provided, value that has to be assigned in the SENTRY_DSN variable mentionned previously (.env and CircleCI environment variables)

## Local docker execution

You can execute the corresponding docker directly on your computer

### Prerequisite

- [DockerHub account](https://hub.docker.com/)
- Docker (Docker engine for Linux/Ubuntu, Doker Desktop for Windows/Mac)
- Create an .env file with the following variables:

```bash
DJANGO_SECRET_KEY="YOUR_DJANGO_SECRET_KEY"
SENTRY_DSN="SENTRY_DSN"
```

### Use


On a terminal:

```bash
docker pull bricevne/oc-lettings-site:tag # Pull the image
docker run -d -p 8000:8000 --env-file .env bricevne/oc-lettings-site:tag # Run the docker container
```

The tag can be the following:
- latest to get the last version of the image
- SHA1: the unique ID of the last commit pushed to GitHub (last tag version: 456d85f97dc26d6f6ec44668dc14b1d3a2396f25) Example : `docker run -d -p 8000:8000 --env-file .env bricevne/oc-lettings-site:456d85f97dc26d6f6ec44668dc14b1d3a2396f25`

You can access the website with: localhost:8000 or O.0.0.0:8000

## License

[MIT](https://choosealicense.com/licenses/mit/)