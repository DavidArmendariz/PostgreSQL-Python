# KPI
## PostgreSQL
To install Postgres in Ubuntu:
```
sudo apt update
sudo apt install postgresql postgresql-contrib
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
