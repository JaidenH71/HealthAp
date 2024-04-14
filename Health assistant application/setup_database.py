import sqlite3

def create_database():
    # Establish connection to SQLite database (or create if not exists)
    conn = sqlite3.connect('responses.db')
    cursor = conn.cursor()

    # Create responses table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY,
            query TEXT NOT NULL,
            response TEXT NOT NULL
        )
    ''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
    print("Database setup completed successfully.")
