import mysql.connector as msq
import os

from dotenv import load_dotenv


load_dotenv()



def connect():
    """Connect to the database using the parameters from the .env file."""
    return msq.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_DATABASE"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )




def create_tables():
    """Create the tables in the database."""
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL REFERENCES users(id),
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT NOW(),
            updated_at TIMESTAMP DEFAULT NOW()
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS files (
            id SERIAL PRIMARY KEY,
            project_id INTEGER NOT NULL REFERENCES projects(id),
            name TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT NOW(),
            updated_at TIMESTAMP DEFAULT NOW()
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS web_searches (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL REFERENCES users(id),
            query TEXT NOT NULL,
            results JSONB NOT NULL,
            created_at TIMESTAMP DEFAULT NOW()
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS codes (
            id SERIAL PRIMARY KEY,
            web_search_id INTEGER NOT NULL REFERENCES web_searches(id),
            code TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT NOW()
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL REFERENCES users(id),
            ai_message TEXT NOT NULL,
            user_message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT NOW()
        );
    """)
    conn.commit()
    conn.close()



def save_user(username, password):
    """Save a new user to the database."""
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, password)
    )
    conn.commit()
    conn.close()



def get_user(username):
    """Get a user from the database."""
    
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM users WHERE username = %s",
        (username,)
    )
    user = cur.fetchone()
    conn.close()
    
    return user



def save_project(user_id, name, description):
    """Save a new project to the database."""
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO projects (user_id, name, description) VALUES (%s, %s, %s)",
        (user_id, name, description)
    )
    conn.commit()
    conn.close()


# def get_projects(user_id):
#    """Get the projects for a user from the