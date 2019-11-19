# KPI
## PostgreSQL
To install Postgres in Ubuntu:
```
sudo apt update
sudo apt install postgresql postgresql-contrib python-psycopg2 libpq-dev
```
Switching Over to the postgres Account
```
sudo -i -u postgres
```
Accessing to the Postgres prompt:
```
psql
```
Exiting the Postgres prompt:
```
\q
```
Create a new user:
```
sudo -u postgres createuser --interactive -P
```
Deleting a user:
```
sudo -i -u postgres
dropuser <username>
```
Create a new database:
```
sudo -u postgres createdb <db>
```
To list all databases (in the Postgres prompt):
```
\l
```
To connect to another database (in the Postgres prompt):
```
\c <db>
```
To view information about the current database connection 
(in the Postgres prompt):
```
\conninfo
```
To see all the tables of the current database (in the Postgres prompt):
```
\dt
```
## Connecting with another user
Instead of connecting with ```postgres```, we can connect with the users
we create. But first, we need to add an user to Linux and give permissions
to use ```sudo```:
```
sudo adduser <newuser>
usermod -aG sudo <newuser>
```
Then we switch to this new user and connect to the database we want to connect
to:
```
sudo -i -u <newuser>
psql -d <db>
```


## Python environment
```
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
```


