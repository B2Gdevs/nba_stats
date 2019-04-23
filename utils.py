"""
This script houses useful methods for analysis and the main application.

Author: Benjamin Garrard
"""
import pickle 
import os


def create_row(team, opposing_team, quarter,
               data_path='data/shortened_X_data.pkl'):
    """
    Create the row in the correct format for prediction.

    This method formats the entries of the user into a format that the
    SVM model can understand since teams are categorical and the model
    needed to be trained on numbers.

    Possible quarter names are 1st, 2nd, 3rd, 4th, OT, 2OT, 3OT, 4OT.

    Example Usage
    -------------
    create_row('Houston Rockets','Portland Trail Blazers', 'OT')

    Parameters
    ----------
    team : str
        Team is just the name of the team that you are trying to predict for.

    opposing_team : str
        This parameter is the team that the model is predicting against.

    quarter: str
        This parameter is the quarter you are trying to predict to be under
        20 points when using the under 20 points svm model.

    data_path: str (default = ../data/shortened_X_data.pkl)
        The data_path is set to the data that is wanted to be used to create
        the row.  The larger the data the longer the load time, therefore using
        a shortened version of the X training data is encouraged.

    Returns
    -------
    row : list
        The row is a list of binary values that correspond to the categorical
        data that was trained within the model.

    """
    opponent_column = 'opponent_names_' + opposing_team
    team_column = 'team_names_' + team
    quarter_column = 'quarters_' + quarter

    # check data folder and if doesn't exist get the bigger version of data
    if os.path.exists(data_path):
        dataframe = load_binary(data_path)
    else:
        data_path = "../data/nba_X_training_data.pkl"
        if os.path.exists(data_path):
            dataframe = load_binary(data_path)
        else:
            print("There is no data found to create the rows needed to predict"
                  + ". Please create the data and place it in the data folder"
                  + ". You can create the binary files needed using the file"
                  + " training.py")
            print("Program is now EXITING...")
            import sys
            sys.exit()
    columns = dataframe.columns
    row = []

    for column in columns:
        if column == opponent_column:
            row.append(1)
        elif column == team_column:
            row.append(1)
        elif column == quarter_column:
            row.append(1)
        else:
            row.append(0)

    return row


def save_binary(path, obj):
    """
    Save a given object as binary at the path given.

    Parameters
    ----------
    path : str
        Path to save the object at.

    obj : object
        This variable could be anything as long as it's base class is a python
        object.

    Returns
    -------
    obj : object
        The object that was saved.

    """
    with open(path, 'wb') as file:
        pickle.dump(obj, file)

    print("{} has been saved at {}.".format(os.path.basename(path), path))
    return obj


def load_binary(path, verbose=False):
    """
    Load a given object as binary at the path given.

    Parameters
    ----------
    path : str
        Path to the pickled object.

    verbose : bool
        Boolean that if true will display where something was loaded from.

    Returns
    -------
    obj : object
        The object that was loaded from the path.

    """
    with open(path, 'rb') as file:
        obj = pickle.load(file)

    if verbose:
        print("{} has been loaded from {}.".format(os.path.basename(path),
                                                   path))
    return obj
