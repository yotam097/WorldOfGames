import Utils
import pymysql
global points, difficulty, last_score

conn = pymysql.connect(host='192.168.99.100', port=3306, user='root', password='12345', db='Games')


def add_score_db(name, points):
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users_Scores;")
    # cursor.execute("DELETE FROM Games.Users_Scores WHERE User_Name = 'Yotam'")
    # print(cursor.execute("SELECT Score FROM Users_Scores;"))
    for row in cursor:
        if name in row:
            cursor.execute("UPDATE Games.Users_Scores SET Score = %s WHERE User_Name = %s", (points, name))
        else:
            cursor.execute("INSERT into Games.Users_Scores (User_Name, Score) VALUES (%s, %s)", (name, points))
    cursor.close()
    conn.close()


# This function reads the previews score from the Scores file if exist, if not, it creates a new one and adding the
# current score
def add_score(points):
    global last_score
    try:
        Utils.file_read.seek(0)
        last_score = Utils.file_read.read()
        if last_score == '':
            Utils.file_write.write("0")
    except:
        Utils.file_write.write("0")
        Utils.file_read.seek(0)
        current_score = Utils.file_read.read()
        new_score = points + int(current_score)
        print("Your score is: ", new_score)
    else:
        Utils.file_read.seek(0)
        last_score = Utils.file_read.read()
        file_overwrite = open(Utils.SCORES_FILE_NAME, "w")
        outp = int(last_score) + points
        file_overwrite.write(str(outp))
        print("Your score is: ", outp)


if __name__ == '__main__':
    add_score_db("Test", 1)
