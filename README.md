# ABitly-Services

## Requirements

1. Install the following dependencies:

- [Python](https://www.python.org/downloads/) >= *v*3.6.8
- [Pip](https://pip.pypa.io/en/stable/installing/) >= *v*9.0.1
- [venv](https://virtualenv.pypa.io/en/latest/installation/)
- [Docker](https://docs.docker.com/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

2. Create a virtual environment in the root directory of the project.

```sh

python3 -m venv env

```

3. Create a `.env` file with the following variables:

**Note**: All the **POSTGRES\_\*** variables should correspond to the configuration of the `docker-compose.yml` file.

```dotenv

FLASK_APP = 'abitly'
POSTGRES_USERNAME = 'abitly'
POSTGRES_PASSWORD = 'abitly2019'
POSTGRES_DATABASE = 'abitlydb'
POSTGRES_HOST = '0.0.0.0'
POSTGRES_PORT = 5432
HOST = '0.0.0.0'
PORT = 5000

```

## Installation

1. Activate the virtual environment.

```sh

source env/bin/activate

```

2. Install dependencies.

```sh

pip install -r requirements.txt

```

## Usage

**Note**: Before running the app you must have running a Postgres instance in a Docker container or in local.

### Run Postgres Container with Docker Compose

```sh

docker compose up -d

```

### Run the app in the production mode

```sh

make run:production

```

### Run the app in the development mode

```sh

make run

```

### Run the tests

```sh

make run:tests

```

## License

**ABitly-Services** is licensed under Apache License, Version 2.0.
