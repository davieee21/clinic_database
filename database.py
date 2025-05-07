from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL configuration (adjust this URL for your database setup)
# For MySQL: 'mysql+mysqlconnector://root:yourpassword@localhost/yourdatabase'
DATABASE_URL = "mysql+mysqlconnector://root:tokyo20.25@127.0.0.1:3306/clinic_db"

# Creating the SQLAlchemy engine. This is the core interface to the database.
# It will be used to create connections to the database.
# If you're using MySQL, `mysql+mysqlconnector` is the correct dialect and driver.
engine = create_engine(
    DATABASE_URL,
    connect_args={"charset": "utf8mb4"}  # Recommended for MySQL to handle special characters
)

# This Base class will be the base for all your models.
# All models (Patient, Doctor, Appointment, etc.) will inherit from this class.
Base = declarative_base()

# SessionLocal will serve as a factory for creating new database sessions.
# Each time you need to interact with the database, you will use this session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to create all tables in the database
# You should call this function once to create all your tables based on your models
def init_db():
    try:
        # Importing the models here to ensure that the database tables are created
        # These models are imported here to avoid circular imports.
        import models
        
        # Log that the database initialization is starting
        print("Initializing the database...")

        # Creating all tables in the database based on the models
        Base.metadata.create_all(bind=engine)

        # Log that the database has been initialized successfully
        print("Database initialized successfully!")
    except Exception as e:
        # Log any errors that occur during the database initialization
        print(f"Error initializing the database: {e}")


# Dependency to get the database session
# This function is used in FastAPI routes to provide the session to your endpoints.
# It will automatically manage the lifecycle of the database session for each request.
def get_db():
    db = SessionLocal()  # Create a new session
    try:
        yield db  # Yield the session for use in the route handlers
    finally:
        db.close()  # Ensure that the session is closed after the request is completed
