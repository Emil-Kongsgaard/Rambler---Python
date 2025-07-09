#Events must be persisted as .txt files in a directory that is part of the game files.
# For now the directory will be a subdirectory under the main project directory. 
# the directory should be named "c:/...../game_events". 
# An event should be given a descriptive name and suffixed by a 4 digit counter that functions as an ID-number eg: "first_event_0001.txt"
# there might be an concurrency issue in the future. It might be worth exploring using a Datebase. For now it will not change.