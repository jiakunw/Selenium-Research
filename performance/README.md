To run user.py, need to download locust on local python enviroment to run the programs.

Locust installation: 

Run 'pip3 install locust'. Python 3.7 or later is required. 
Run 'locust -V' to verify installation. 

Running Files:

Run 'locust -f user.py'
Go to localhost:8089. Should see the Locust.io web UI. The web UI binds to port 8089 by default. 
Enter the # of users and the spawn rate and click start. 
user.py will not login correctly until credentials.py is filled with registered usernames and passwords. 
