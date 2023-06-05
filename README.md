# Phase 3, Lecture 8: SQLAlchemy & Alembic, and SQLAlchemy Associations

## Lecture Topics

- SQLAlchemy
- Alembic
- SQLAlchemy Associations

## Introduction

In today's lecture, we will discuss about SQLAlchemy, Alembic, and SQLAlchemy Associations

## Setup

1. Fork and then Clone this repository.
2. Make sure that you are in the correct directory (folder) that contains a `Pipfile`, then run `pipenv install` in your terminal to install the required libraries.
3. Now that your `pipenv` virtual environment is ready to use, enter `pipenv shell` to enter the virtual environment.
4. Enter the command `cd lib/db` in the terminal to move into the db directory.
5. Enter the command `python cli.py` in the terminal to start running my Python CLI.
6. Run `alembic init migrations` to set up Alembic.
7. Modify line 63 in `alembic.ini`, where it says `sqlalchemy.url = driver://user:pass@localhost/dbname`, to `sqlalchemy.url = sqlite:///hotels.db`
8. Replace line 21 in `migrations/env.py`, where it says `target_metadata = None`, with the following:

```py
from models import Base
target_metadata = Base.metadata
```

9. Navigate to `models.py` and we will start creating models.
10. We will regularly run `alembic revision --autogenerate -m 'descriptive message'` (where we will replace `descriptive message` with an actual descriptive message of our own) and `alembic upgrade head` to track the modifications to the database and create checkpoints in case we ever need to roll those modifications back.

## Other Alembic terminal commands we will use

- `alembic downgrade <version_number>` where `<version_number>` represents the ID of the migration that we want to downgrade / rollback to.
- `alembic current` to find the last migration applied. This will return the ID of the current migration, as well as information on whether it is the most recent migration, or head.
- `alembic history` to see the full history of migrations applied to the database.
