# AI Health assistant
This is a web application that can help automate the feedback process for people looking for diagnoses, help understanding medical documents, and providing advice and health tips to users. This health application can help people with all their medical needs and provide sold advice to users. This can help users to get quality and accurate health advice to help users faster than older methods.

## Table of Contents
- [Attributes](# Attributes)
- [requirements.txt](# requirements.txt)
- [templates](# templates)
- [static](# static)
- [__pycache__](# __pycache__)
- [app.py](# app.py)
- [setup_database.py](# setup_database.py)
- [responses.db](# responses.db)
- [schema.sql](# schema.sql)
- [Licence.txt](# Licence.txt)

# Attributes 
The main attributes of this web application include its prompt response, AI text-to-speech, and document reader functionalities. This allows users to be able to ask the system health related questions while also allowing them to upload their medical documents and give advice on how someone should proceed. In addition, the AI text-to-speech functionality can be used to assist disabled users to navigate the app. Finally responses and documents will be saved on the responses.html page for future viewing by users.

# requirements.txt
The requirements.txt file serves as a manifest that outlines the specific Python packages and their corresponding versions essential for running this Flask-based health assistant web application. This file is instrumental in managing project dependencies and ensuring the consistency and reproducibility of the development environment. Each listed package plays a crucial role in the functionality and features of the application. The file includes essential packages like Flask (2.0.2.) This lightweight and versatile web framework for Python forms the foundation of the application, facilitating the development of server-side logic, routing, and request handling.

# Front End

# templates
index.html
The index.html file serves as the primary user interface for a personalized health assistant web application, offering a user-friendly design for accessing users personalized health assistence through entering their username and email. Users can input health-related questions or topics via the text area or upload medical documents for more detailed inquiries. Notably, the integration of text-to-speech functionality allows users to listen to AI-generated responses by clicking the "Speak Response" button, enhancing accessibility. Additionally, the interface provides a link to view stored responses for continuity in health guidance. Potential improvements could focus on enhancing user experience with real-time feedback during form submission, optimizing document handling for various file types, ensuring accessibility features for all users, and refining the UI layout for improved usability across devices. 

Responses.html
This file is used to store and contain prompt responses and questions. It is also used to view any documents that have been stored within the application. 

# static
Doctor_image.png
This is an image file that provides the image for the index.html file. This image is used to help provide some visual appeal to the main UI of the web application.

main.css, styles.css
The styles.css file complements the global styles set in main.css to enhance the appearance and functionality of the health assistant web application. It establishes consistent font styling using 'Arial', a light gray background (#f9f9f9), and a default text color (#333) for improved readability. The .container class centers content within a defined width (800px), featuring a white background (#fff), subtle box shadow, and rounded corners for a clean layout. Form elements like textured, input[type="text"], and buttons are uniformly styled with appropriate padding, borders, and sizing for usability. Interactive elements such as buttons (input[type="submit"], button) have a blue background (#007bff) with white text, transitioning to a darker shade on hover (#0056b3) for added interactivity. The .ai-response class defines styling for response sections with padding, a light gray background (#f0f0f0), and bottom margin. 

# Back End 

# __pycache__
This file contains the documents called app.cpython-39.pyc and app.cpython-312.pyc. These files are bytecode files compiled from the python source code files named app.py. The suffix 'cpython-39 and cpython-312 indicate the python version for which the bytecode was compiled. 

# app.py
The app.py file serves as the back end logic for a personalized health assistant web application, leveraging Flask to handle user interactions and manage data. Upon initialization, Flask creates an instance of the application (app) and integrates a RESTful API (api) with Swagger documentation for managing endpoints and specifying API operations. The application utilizes a SQLite database (responses.db) to persist user queries, documents, and AI-generated responses. The init_db() function initializes the database schema by executing SQL scripts from schema.sql when the app starts.

A pivotal feature of the back end is the Document Processing class, which manages the upload and processing of medical documents. This class employs temporary file storage (tempfile) and file manipulation (os) to handle document uploads, extracting text content for analysis. The generate_response() function implements mock AI logic to generate personalized responses based on user queries. Upon processing, responses can be converted to speech using the text_to_speech() function, which could potentially leverage external services for text-to-speech conversion.

The back end also defines routes (/ and /responses) to render HTML templates (index.html and responses.html) for user interaction and viewing stored responses. The index() route displays a form for submitting health-related questions, while the view_responses() route queries the database to display stored responses. The application can be executed locally (__name__ == '__main__') with debug mode enabled for testing and development purposes. 

# Database

# setup_database.py
The setup_database.py file serves the purpose of initializing and setting up the SQLite database (responses.db) for the personalized health assistant web application. Its functionality revolves around creating the necessary database schema if it doesn't already exist, ensuring that the application has the required structure to store user queries, document content, and AI-generated responses. The script defines a create_database() function that establishes a connection to SQLite, executes SQL commands to create the responses table with specific column definitions (id, query, document_content, response), and commits the changes. 

# responses.db
This SQLite database file contains two tables: prompts and documents, designed to store medical-related data. The prompts table serves as a repository for medical prompts. It includes fields such as PromptID (unique identifier), UserName, UserEmail, Created (timestamp of creation), Consent (consent form title), and Msg (the actual research prompt). The documents table is intended for storing uploaded documents related to the research. It includes fields like DocumentID (unique identifier), UserName, UserEmail, Uploaded (timestamp of upload), DocumentName (name of the document), and DocumentData (binary data of the document). Together, these tables facilitate the management of research projects by enabling researchers to record study details (prompts) and associate relevant documents (documents) directly within the database. The structure supports data integrity and organization, providing a comprehensive framework for research data management and analysis.

# schema.sql
The schema.sql file defines the database schema for the responses table within the personalized health assistant web application. This table structure includes columns for storing unique identifiers (id), user queries (query), binary large objects representing document content (document_content), and AI-generated responses (response). The schema ensures that the responses table is properly defined with necessary constraints, allowing the application to organize and manage user-generated data effectively.

# Licence.txt
This file contains the MIT license test as a permissive open-source license. It is used to grant users the freedom to use, modify, distribute, and sublicense the software without restrictions. In this case the MIT licence holds no legal value but shows the application of copyright licenses within web applictions.










