# ubantu - linux server

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
