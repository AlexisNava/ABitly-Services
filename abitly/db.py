import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError

username = os.getenv('POSTGRES_USERNAME')
password = os.getenv('POSTGRES_PASSWORD')
database = os.getenv('POSTGRES_DATABASE')
host = os.getenv('POSTGRES_HOST')
port = os.getenv('POSTGRES_PORT')

postgres_uri = f'postgresql://{username}:{password}@{host}:{port}/{database}'

engine = create_engine(postgres_uri,
                       convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    """Create all tables stored in metadata"""

    # Models

    print(f'Connected successfully to: {postgres_uri}')

    try:
        Base.metadata.create_all(bind=engine)
    except OperationalError as error:
        print(error)
