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

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))



except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

cursor = db.cursor()


# Insert new record into player table for Team Gandalf
new_player = ("INSERT INTO player (first_name, last_name, team_id)"
              "VALUES ('Smeagol', 'Shire Folk', 1)")
cursor.execute(new_player)

print("\n")
print("-- DISPLAYING PLAYERS AFTER INSERT --")


# INNER JOIN query to connect the player and team tables by team_id
cursor.execute("SELECT player_id, first_name, last_name, team_name "
               "FROM player "
               "INNER JOIN team "
               "ON player.team_id = team.team_id "
               "ORDER BY player_id;")
players = cursor.fetchall()

for player in players:
    print("Player ID: {}".format(player[0]), "\nFirst Name: {}".format(player[1]), "\nLast Name: {}".format(player[2]),
          "\nTeam Name: {}\n".format(player[3]))


# Update newly inserted record
update_player = ("UPDATE player "
                 "SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer'"
                 "WHERE first_name = 'Smeagol';")
cursor.execute(update_player)

print("\n")
print("--DISPLAYING PLAYERS AFTER UPDATE--")


# INNER JOIN query to connect the player and team tables by team_id
cursor.execute("SELECT player_id, first_name, last_name, team_name "
               "FROM player "
               "INNER JOIN team "
               "ON player.team_id = team.team_id "
               "ORDER BY player_id;")
players = cursor.fetchall()

for player in players:
    print("Player ID: {}".format(player[0]), "\nFirst Name: {}".format(player[1]), "\nLast Name: {}".format(player[2]),
          "\nTeam Name: {}\n".format(player[3]))


# Delete newly inserted record
delete_player = ("DELETE FROM player "
                 "WHERE first_name = 'Gollum';")
cursor.execute(delete_player)

print("\n")
print("--DISPLAYING PLAYERS AFTER DELETE--")

# INNER JOIN query to connect the player and team tables by team_id
cursor.execute("SELECT player_id, first_name, last_name, team_name "
               "FROM player "
               "INNER JOIN team "
               "ON player.team_id = team.team_id "
               "ORDER BY player_id;")
players = cursor.fetchall()

for player in players:
    print("Player ID: {}".format(player[0]), "\nFirst Name: {}".format(player[1]), "\nLast Name: {}".format(player[2]),
          "\nTeam Name: {}\n".format(player[3]))

input("\n Press any key to continue...")
