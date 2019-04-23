"""
Created on Mon Jan  7 15:42:59 2019

@author: ben

This file is the main application where the user will interact with the console
"""

import nba_methods
# from pyfiglet import Figlet

def pick_a_team():

    teams = nba_methods.load_binary("unique_teams.pkl")
    selection = None
    team_ = None

    while selection == None:

        print("\n\n=== Team Menu ===")
        selections = []
        count = 1
        for team in teams:
            selections.append(str(count))
            print("{}. {}".format(count, team))
            count += 1

        selections.append(str(count))
        print('{}. Go back to Main Menu'.format(count))
        print("\nRemember if you want to cancel the program press ctrl + C on the keyboard.\n")
        selection = input("Please select a number from the menu: ")

        if selection not in selections:
            input("Your selection was not in the Menu. Press Enter to go back to the Menu...")
            continue

        if selection == str(count):
            return team_

        team_ = teams[int(selection)-1]
        print("\n\n\n\nYou have picked [{}]".format(team_))
        print("Returning to main menu...")
        
        return team_

def pick_a_quarter():
    quarters = nba_methods.load_binary('quarters.pkl')

    selection = None
    quarter_ = None

    while selection == None:

        print("\n\n=== Team Menu ===")
        selections = []
        count = 1
        for quarter in quarters:
            selections.append(str(count))
            print("{}. {}".format(count, quarter))
            count += 1

        selections.append(str(count))
        print('{}. Go back to Main Menu'.format(count))
        print("\nRemember if you want to cancel the program press ctrl + C on the keyboard.\n\n")
        selection = input("Please select a number from the menu: ")

        if selection not in selections:
            input("Your selection was not in the Menu. Press Enter to go back to the Menu...")
            continue

        if selection == str(count):
            return quarter_

        quarter_ = quarters[int(selection)-1]
        print("\nYou have picked {}\n".format(quarter_))
        
        return quarter_

def predict(team, opposing_team, quarter):
    data = nba_methods.load_binary('shortened_X_data.pkl')
    model = nba_methods.load_binary('nba_svm_model.pkl')
    row = nba_methods.create_row(team, opposing_team, quarter, data)

    prediction = model.predict([row])[0]

    if prediction == 1:
        print("Congrats Homie!! You found out that your team [{}] will score less than 20 points in the [{}] quarter"\
              " against the team [{}]".format(team, quarter, opposing_team))
    else:
        print("Sorry man!! But your team [{}] won't be under 20 points in [{}] quarter against [{}]".format(team, quarter, opposing_team))

    return prediction

def main():

    team = None
    opposing_team = None
    quarter = None

    # figlet = Figlet(font="big")
    # print(figlet.renderText("HECTOR'S NBA QUARTER PREDICTION ENGINE"))
    print("HECTOR'S NBA QUARTER PREDICTION ENGINE")

    print("This engine predicts if your team will be under 20 points in a give quarter.\n"\
          "All that is needed for this is what team you want to know about\n"
          "who they are playing against, and what quarter do you look at.")

    print("\nDISCLAIMER:  This program has an 85% accuracy based on data gathered since 2012.\n"\
          "While it is good, there is always a chance it might not model current teams well!")

    selections = ['1','2', '3', '4', '5', '6']
    stop = False
    while stop != True:

        print("\n\n=== Main Menu ===")
        print("1. Pick your Team \n"\
              "2. Pick opposing Team\n"\
              "3. Pick a Quarter\n"\
              "4. View your picks\n"\
              "5. Predict\n"\
              "6. Quit Program\n")

        selection = input("Select a number from the menu: ")
        print("\nRemember if you want to cancel the program press ctrl + C on the keyboard.\n\n")
        
        if selection not in selections:
            input("Your selection was not in the Menu. Press Enter to go back to the Menu...")
            continue


        # Switch like statement
        if selection == '1':
            team = pick_a_team()
        elif selection == '2':
            opposing_team = pick_a_team()
        elif selection == '3':
            quarter = pick_a_quarter()
        elif selection == '4':
            print("Your team: {}".format(team))
            print("Opposing team: {}".format(opposing_team))
            print("The Quarter: {}".format(quarter))
        elif selection == '5':
            predict(team, opposing_team, quarter)
        elif selection == '6':
            stop = True
            

            



if __name__.endswith('__main__'):
    main()