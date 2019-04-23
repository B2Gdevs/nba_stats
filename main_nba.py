"""
This script is the main application for predicting the outcomes of a team.

This script as of 3/21/2019 only predicts if a team witll be under 20 points
in the specified quarter.

Author: Benjamin Garrard
"""


import utils


def pick_a_team():
    """
    Display the team menu for the user to pick a team.

    Returns
    -------
    team_ : str
        The selected team by the end user.

    """
    teams = utils.load_binary("data/unique_teams.pkl")
    selection = None
    team_ = None

    while selection is None:

        print("\n\n=== Team Menu ===")
        selections = []
        count = 1
        for team in teams:
            selections.append(str(count))
            print("{}. {}".format(count, team))
            count += 1

        selections.append(str(count))
        print('{}. Go back to Main Menu'.format(count))
        selection = input("Please select a number from the menu: ")

        if selection not in selections:
            input("Your selection was not in the Menu. Press Enter to go back"
                  + " to the Menu...")
            continue

        if selection == str(count):
            return team_

        team_ = teams[int(selection)-1]
        print("\n\n\n\nYou have picked [{}]".format(team_))
        print("Returning to main menu...")

        return team_


def pick_a_quarter():
    """
    Display the quarter menu for the user to pick a quarter.

    Returns
    -------
    quarter_ : str
        The selected quarter by the end user.

    """
    quarters = utils.load_binary('data/quarters.pkl')

    selection = None
    quarter_ = None

    while selection is None:
        print("\n\n=== Team Menu ===")
        selections = []
        count = 1
        for quarter in quarters:
            selections.append(str(count))
            print("{}. {}".format(count, quarter))
            count += 1

        selections.append(str(count))
        print('{}. Go back to Main Menu'.format(count))
        selection = input("Please select a number from the menu: ")

        if selection not in selections:
            input("Your selection was not in the Menu. Press Enter to go back"
                  + " to the Menu...")

            # reset selection since the selection could be off the menu
            selection = None
            continue

        if selection == str(count):
            return quarter_

        quarter_ = quarters[int(selection)-1]
        print("\nYou have picked {}\n".format(quarter_))

        return quarter_


def predict(team, opposing_team, quarter):
    """
    Predict if the team will be under 20 points.

    Parameters
    ----------
    team : str
        The team that will the prediction will be for. Example would be
        Houston Rockets

    opposing_team : str
        The team that will be predicted against. Possible quarter names are
        1st, 2nd, 3rd, 4th, OT, 2OT, 3OT, 4OT.

    quarter : str
        The quarter that should be predicted to be under twenty or not.

    """
    model = utils.load_binary('models/nba_quarter_under_20_SVM.pkl')
    row = utils.create_row(team, opposing_team, quarter)

    prediction = model.predict([row])[0]

    if prediction == 1:
        print("Congrats Homie!! You found out that your team [{}] will score"
              .format(team)
              + " less than 20 points in the [{}] quarter".format(quarter)
              + " against the team [{}]".format(opposing_team))
    else:
        print("Sorry man!! But your team [{}] won't be under 20 points in [{}]"
              .format(team, quarter)
              + " quarter against [{}]".format(opposing_team))

    return prediction


def main():
    """
    Run the application.

    This method is the main program similar to that of c++'s main function. 
    This is where everything works in unison.
    """
    team = None
    opposing_team = None
    quarter = None

    # figlet = Figlet(font="big")
    # print(figlet.renderText("HECTOR'S NBA QUARTER PREDICTION ENGINE"))
    print("HECTOR'S NBA QUARTER PREDICTION ENGINE")

    print("This engine predicts if your team will be under 20 points in a give"
          + " quarter.\n"
          "All that is needed for this is what team you want to know about\n"
          "who they are playing against, and what quarter do you look at.")

    print("\nDISCLAIMER:  This program has an 85% accuracy based on data"
          + " gathered since 2012.\n"
          + " While it is good, there is always a chance it might not model"
          + " current teams well!")

    selections = ['1', '2', '3', '4', '5', '6']
    stop = False
    while stop is not True:

        print("\n\n=== Main Menu ===")
        print("1. Pick your Team \n"
              "2. Pick opposing Team\n"
              "3. Pick a Quarter\n"
              "4. View your picks\n"
              "5. Predict\n"
              "6. Quit Program\n")

        selection = input("Select a number from the menu: ")
        if selection not in selections:
            input("Your selection was not in the Menu. Press Enter to go back"
                  + " to the Menu...")
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