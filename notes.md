# Digital Ocean
    - provider of servers
    - rent a server for a small amount of money each money
    - we can change users, we own the server that is running our app

# ubantu - linux server
    - your unix server

# We have created a cluster a new server running postgresql

# Its running locally on the default port 5432

# command to login as the postgres user `sudo -i -u postgres`
    - `psql` - The user connects a postgressql database
    - `\conninfo` - get information on what database you are connected to
    # `\q` - exit the out of being a postgres user

# Logging in and out of the server

# PostgresSQL User Login Security Configuration File = `sudo vi /etc/postgresql/9.5/main/pg_hba.conf`
# if we are a postgres users
    # peer means we can have access to all databases
# local
    - Connection coming from the server
    - local connections were going to ask for password
# host
    - Connecting via IP or an URL (from the interest)

# xginx
    - acts as a gateway for our applications and our users
    - multi
    - give xginx access

# Domain name is just a string
## The location of the server is determined by the ip address
# WhoisGuard
# systemctl - system control
# default - port 80

# Unit - defines a section
# Service - this is the area where we define properities for our Service
    - We want to define an environment to run before running the service
    - The uwsgi app runs our app
    - ExecStart: if it crashes it will restart but we have to tell it to start what program, we are telling it the run the uwsgi app that runs our app, so we give a location and tell it to run the master process
        - bin = binary folder
        - uwsgi = runs the uwsgi process
    -Restart: Restart so the site won't be down for a certain about of time
    -
# How Domain Name Systems (DNS) Works
- Checks if the operating system knows the IP address
- If not a DNS query begins
    - Because there are so many domains there is not a single server that knows the IP related to a single domain
        - First we go to a root server (serveral hundreds)
        which will tell us I don't know anything about blahblah.com (that is too specific) but I do know about the .com
        - Goes to the .com servers (TLD servers) Okay it ask do you know the IP address of example.com it responds not knowing the IP address but knows a server that knows the IP address example.com and returns that
        - Last step goes to the server (Authoritative Name servers - know the IP address) that has example.com and gets the IP address then the browser loads the IP address

# The connection between your computer and Cloudfare is encrypted using your private key.

# Left off video 154 code recap
