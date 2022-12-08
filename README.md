# Bible Data Database generator

This is a generator for [Brady Stephenson's bible-data files](https://github.com/BradyStephenson/bible-data)

It generates databases and populates them via [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy)

* Any database should work that's supported by SQLAlchemy
  * Default is to create a sqlite3 database called bible-data.db in the current working directory.

## Simple install and use

```bash
pip install git+https://github.com/elliotd123/bibledatadb.git
git clone https://github.com/BradyStephenson/bible-data
bibledatadb
