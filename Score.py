import Utils
global points, difficulty, last_score


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