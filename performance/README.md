To run user.py or nonloginuser.py, need to download locust on local python enviroment to run the programs.

Locust installation: 

Run 'pip3 install locust'. Python 3.7 or later is required. 
Run 'locust -V' to verify installation. 



Running user.py: 

Run 'locust -f user.py'
Go to localhost:8089. Should see the Locust.io web UI. The web UI binds to port 8089 by default. 
Enter the # of users and the spawn rate and click start. Because there are two user classes: LoginUser and CreateAccountUser, there needs to be at least 2 users entered for them to work. For each user, the probability of them belonging to LoginUser or CreateAccountUser is 50-50. 

user.py will not login correctly without credentials.py, which is filled with registered usernames and passwords. 

Run in distributed mode to avoid high locust CPU usage. 
Run 'locust -f user.py --master'. 
Open new terminal tabs and run 'locust -f user.py --worker'. Recommended to run at least three separate termainsl with the worker tab. 



Running loadmarket_timestamps.py:

Run 'locust -f loadmarket_timestamps.py'
Go to localhost:8089. Should see the Locust.io web UI. The web UI binds to port 8089 by default. 
Enter the # of users and the spawn rate and click start. 