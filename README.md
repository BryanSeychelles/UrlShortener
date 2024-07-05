# UrlShortener

# UrlShortener

To install the requirements for the app, follow these steps:

1. Install Python and pip if you haven't already.
2. Navigate to the project directory: `/Users/bryanseychelles/dev/UrlShortener`.
3. Install the Python dependencies by running the following command:
    ```
    pip install -r requirements.txt
    ```

    To configure the environment variables for the app, create a file named `.env` in the project directory (`/Users/bryanseychelles/dev/UrlShortener`) and add the following variables:

    ```
    DB_HOST=
    DB_PORT=
    DB_NAME=
    DB_USER=
    DATABASE_OWNER_PASSWORD=
    ```

    Make sure to replace `your_username` and `your_password` with the appropriate values for your database configuration.

 Run the docker container for the DB: 
    ```
    docker compose up
    ```

To run the FastAPI backend:

1. Open a terminal and navigate to the project directory.
2. Run the followings commands:
    ```
    cd API/
    fastapi dev main.py 
    ```

To run the React frontend:

1. Open another terminal and navigate to the project directory.
2. Change to the `frontend` directory:
    ```
    cd gui
    ```
3. Install the Node.js dependencies:
    ```
    npm install
    ```
4. Start the React development server:
    ```
    npm start
    ```

Make sure to have Docker installed if you want to run the application in a container.
