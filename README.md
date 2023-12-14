# Flask Demo Web App with Auth0

This application is a sample on how to integrate Auth0 for authentication in a Flask web application using APIRouter and module separation.

## How to run the server

1. Clone this repository
    ```
    git clone https://github.com/jtemporal/minimal-flask-webapp-auth0.git && cd minimal-flask-webapp-auth0
    ```
2. Create a `.config` file from `.config.example` and populate the values from your Auth0 Application. Here is 
   ```
   cp .config.example .config
   ```

3. Create a virtual environment and install dependencies
   
   ```
   # Create a venv
   python3 -m venv .env 
   
   # Activate
   source .env/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

4. Start the server

   ```
   flask --app app run --port 8000
   ```
   
5. Visit [`http://localhost:4040/`](http://localhost:4040/) to access the starter web application.

----

Where to find us: 
• Jess' LinkedIn: http://linkedin.com/in/jessicatemporal/
• Juan's LinkedIn: https://www.linkedin.com/in/bajcmartinez/

Sign up for Auth0's developer newsletter here: https://a0.to/nl-signup/python