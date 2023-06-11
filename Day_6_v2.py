#Md Hussain
#Day 6
#Use of lists, tuples and dictionaries

def print_friend_info(data):
#so the loop at the bottom is iterating over the two dictionaries, so... it passes over the first one and I'm
#using "data" to refer to the data it passed.. that's what i understand 
    #hobby string
    if len(data["Hobbies"]) > 1:#so off the data that just got passed, if there are more than one hobbies... yea?
        last_hobby = data["Hobbies"][-1]
        other_hobbies = ", ".join(data["Hobbies"][:-1])
        hobbies = "{} and {}".format(other_hobbies, last_hobby)
    else:
        hobbies = data["Hobbies"]

    print("{} is {} years old and their favorite food is {}. Their hobbies are {}."
      .format(data["Name"], data["Age"], data["Favorite_Food"],
              hobbies))

Info_about_friends = [{"Name" : "Ishmam", "Age": 19, "Favorite_Food" : "chicken", "Hobbies" : ["workouts", "driving"]},
                      {"Name" : "Sameer", "Age": 19, "Favorite_Food" : "curry",
                       "Hobbies" : ["Swimming", "workouts", "driving", "cooking", "gaming",
                                    "watching movies", "stargazing", "reading", "hunting"]}]

for x in Info_about_friends:
    print_friend_info(x)
    print("\n")
