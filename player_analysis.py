project_title = "Premier League Player Analysis"

subsection_title1 = "Player Details"
player_name = "Anthony Lawanson"
player_number = 17
age = 21
date_of_birth = "26th May, 2005"
country_of_origin = "Nigeria"
position = "Centre Forward"
preferred_foot = "Left"
height = "6 foot 0 inches"

subsection_title2 = "Performance against Aston Villa (H)"
minutes_played = 75
goals = 2
assists = 0
big_chances_created = 4
goal_contributions = goals + assists
passes_attempted = 34
passes_completed = 30
pass_accuracy = (passes_completed/passes_attempted)*100
total_shots = 6
shots_on_target = 4
shooting_accuracy = (shots_on_target/total_shots)*100
conversion_rate = (goals/total_shots)*100
match_result = "WIN"
game_score = "3-2"
# use if statement to make metric of Match performance


print(project_title)
print()
print(subsection_title1.upper())
print("Player Name:", player_name)
print("Age:", age)
print("Date of Birth:", date_of_birth)
print("Country of Origin:", country_of_origin)
print("Position:", position)
print("Preferred Foot:", preferred_foot)
print("Height:", height)
print()
print(subsection_title2.upper())
print("Minutes Played:", minutes_played)
print("Goals:", goals)
print("Assists:", assists)
print("Big Chances Created:", big_chances_created)
print("Goal Contributions:", goal_contributions)
print("Passes Attempted:", passes_attempted)
print("Passes Completed:", passes_completed)
print("Pass Accuracy:", f"{pass_accuracy:.2f}%")
print("Total Shots:", total_shots)
print("Shots on Target:", shots_on_target)
print("Shooting Accuracy:", f"{shooting_accuracy:.2f}%")
print("Conversion Rate:", f"{conversion_rate:.2f}%")
print("Match Result:", match_result)
print("Game Score:", game_score)

if pass_accuracy >= 80 and shooting_accuracy >= 50 and conversion_rate >= 10:
    print("Performance: Excellent")
