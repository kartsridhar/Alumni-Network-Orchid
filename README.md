# Alumni-Network-Orchid

A social network for connecting students to alumni of Orchid School.

## Setup
*   Open XAMPP and start the ```Apache``` and ```MySQL``` server
*   **Add the MySQL database**:
    *   Navigate to ```http://localhost/phpMyAdmin```
    *   Create a new database called ```alumini_network```
    *   Import the ```alumini_network.sql``` file inside the database to set up the tables.
*   **Start the MongoDB server**
    *   After setting up MongoDB on your system, if the server isn't running automatically, open a command prompt/terminal and type in ```mongod```. 
*   **Open 2 terminals**
    *   **Terminal 1** - To run the API
        *   ```cd alumini_network_api```
        *   ```pip install -r requirements.txt```
        *   ```python server.py```
        *   API should run on ```localhost:5000```
    *   **Terminal 2** - To run the front end
        *   ```cd alumni_network_frontend```
        *   ```npm install```
        *   ```npm run serve```
        *   App should run on ```localhost:8080```