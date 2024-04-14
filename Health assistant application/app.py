from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection helper function
def get_db_connection():
    conn = sqlite3.connect('responses.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database
def init_db():
    with app.app_context():
        conn = get_db_connection()
        with app.open_resource('schema.sql', mode='r') as f:
            conn.cursor().executescript(f.read())
        conn.commit()

# Initialize the database when the app starts
init_db()

# Home route - display form and handle response storage
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['user_input']
        response = generate_response(query)  # Function to generate AI response
        store_response(query, response)  # Store query and response in the database
        return redirect(url_for('index'))  # Redirect to clear form
    return render_template('index.html')

# Function to generate AI response (mock implementation)
def generate_response(query):
    # Implement AI logic here (mock response for demonstration)
    return f"This is the response to '{query}'."

# Function to store query and response in the database
def store_response(query, response):
    conn = get_db_connection()
    conn.execute('INSERT INTO responses (query, response) VALUES (?, ?)', (query, response))
    conn.commit()
    conn.close()

# Route to view all stored responses
@app.route('/responses')
def view_responses():
    conn = get_db_connection()
    responses = conn.execute('SELECT * FROM responses').fetchall()
    conn.close()
    return render_template('responses.html', responses=responses)

if __name__ == '__main__':
    app.run(debug=True)
