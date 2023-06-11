#Md Hussain
#Day 6
#Use of lists, tuples and dictionaries

Info_about_friends = [{"Name" : "Ishmam", "Age": 19, "Favorite_Food" : "chicken", "Hobbies" : ["workouts", "driving"]},
                      {"Name" : "Sameer", "Age": 19, "Favorite_Food" : "curry",
                       "Hobbies" : ["Swimming", "workouts", "driving", "cooking", "gaming",
                                    "watching movies", "stargazing", "reading", "hunting"]}]

#for Ishmam
print(Info_about_friends[0]["Name"], "is", Info_about_friends[0]["Age"],
      "years old and his favorite food is", Info_about_friends[0]["Favorite_Food"],".")
print("Okay need a way to print so the period isn't spaced")
print("Using \".format\"...")
print("{} is {} years old and his favorite food is {}. His hobbies are {} and {}."
      .format(Info_about_friends[0]["Name"], Info_about_friends[0]["Age"], Info_about_friends[0]["Favorite_Food"],
              Info_about_friends[0]["Hobbies"][0], Info_about_friends[0]["Hobbies"][1]))
print("\n")
#For Sameer
Hobbies_string = ", " .join(Info_about_friends[1]["Hobbies"])

print("{} is {} years old and his favorite food is {}. His hobbies are {}."
      .format(Info_about_friends[1]["Name"], Info_about_friends[1]["Age"], Info_about_friends[1]["Favorite_Food"],
              Hobbies_string))
print("Need to add \"and\" before last hobby of Sameer")

if len(Info_about_friends[1]["Hobbies"]) > 1:
    last_hobby = Info_about_friends[1]["Hobbies"][-1]
    other_hobbies = ", ".join(Info_about_friends[1]["Hobbies"][:-1])
    hobbies = "{} and {}".format(other_hobbies, last_hobby)
else:
    hobbies = Info_about_friends[1]["Hobbies"]
print("{} is {} years old and his favorite food is {}. His hobbies are {}."
      .format(Info_about_friends[1]["Name"], Info_about_friends[1]["Age"], Info_about_friends[1]["Favorite_Food"],
              hobbies))
