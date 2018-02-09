# Ikonos
Backend setup for project AG

* Note use Python 3.6 for this repo.

## Devbox setup

1. Clone the repo
2. Make sure you are using a virtualenv with Python 3.6.x. Follow [this](http://virtualenvwrapper.readthedocs.io/en/latest/install.html) for setting up virtualenv
3. Install the python packages needed for the repo `pip install -r requirements.txt`
4. Install [PostgreSQL](http://postgresapp.com/)
    * Remember to add psql into your PATH
5. Once Postgres is installed and running, create database named `landsat_dev`
```bash
$ psql
# create database wordcount_dev;
CREATE DATABASE
# \q
```
6. Run the followings to set up the database
```bash
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```
7. Install Redis via Homebrew `brew install redis`

8. Add the followings environment variables
```bash
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://localhost/landsat_dev"
export REDISTOGO_URL="redis://localhost:6379"
export PYTHONPATH=$PYTHONPATH:$PWD/ikonos
```
9. Open up three terminal windows
    * In the first, run `redis-server`
        * If your redis server is not running on port `6379`, please update the `REDISTOGO_URL` variable accordingly
    * In the second, run `python ikonos/worker.py`
    * In the third, run `python manage.py runserver`

10. If there is any changes to the `models.py` file, an upgrade to the database is needed
```bash
$ python manage.py db upgrade
```


## CONTRIBUTION

#### General guide
* All the logical code resides under ikonos/utils package inside this repo
* All the HTML code resides under ikonos/templates folder
* And the CSS, Javacripts or images reside under ikonos/static folder


#### Branch naming guidelines:

We use the following naming convention for branches:

* Bug fixes: `fix/some-error`
* New feature: `feature/something-cool`
* Temporary / Nasty hacks / emergency: `something-something`


### Coding Guidelines

We follow [PEP8 styleguide](https://www.python.org/dev/peps/pep-0008/) using the [Flake8](http://flake8.pycqa.org/en/latest/) tool.


### Pull request process
* Create a new branch to work on new codes/features.
* Submit a PR from the branch created.
* Upon review approval, merge to master.


## To Deploy
                   
Currently deployment to Heroku is only possible with Jack's Heroku account and credentials.
Please work with Jack on Heroku deployment.
