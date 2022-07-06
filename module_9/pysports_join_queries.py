import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "mysql333",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))



except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)


cursor = db.cursor()

# INNER JOIN query to connect the player and team tables by team_id
cursor.execute("SELECT player_id, first_name, last_name, team_name "
               "FROM player "
               "INNER JOIN team "
               "ON player.team_id = team.team_id;")
players = cursor.fetchall()
print("\n")
print("-- DISPLAYING PLAYER RECORDS --")
for player in players:
    print("Player ID: {}".format(player[0]), "\nFirst Name: {}".format(player[1]), "\nLast Name: {}".format(player[2]),
          "\nTeam Name: {}\n".format(player[3]))

input("\n Press any key to continue...")