"""
This script creates and saves the models as well as data used.

Author: Benjamin Garrard
"""
import pandas as pd
from sklearn.svm import SVC
from utils import save_binary


def create_quarter_under_20_model(data_path='data/data.csv',
                                  save_data=False, save_model=True,
                                  shorten_data=False, train=True):
    """
    Create the quarter prediction model for nba games.

    This method creates an SVM that is trained on nba stats data focusing
    on finding out which teams will fall under 20 points in a quarter against
    other teams.

    Parameters
    ----------
    data_path : str (default = 'data/data.csv)
        Path to the data used to train the SVM.

    save_data : bool (default = False)
        Boolean that if true will pickle the data in to a binary format.
        This creates mutliple data files, 'unique_teams.pkl',
        'nba_X_training_data.pkl' or 'shortened_X_data.pkl',
        'nba_Y_training_data.pkl'.

    save_model : bool (default = save_model)
        Boolean that if true will pickle the SVM model and save it as
        'nba_quarter_under_20_SVM.pkl'.

    shorten_data : bool (default = shorten_data)
        Boolean that if true will shorten the X data used in training to be
        read in the rest of the application more quickly.
    
    train : bool (default = True)
        Boolean just in case someone forgot to save the data, but made the 
        model and don't want to have to do it again.  Set this to false if that
        is the case.

    Returns
    -------
    svm : SVC
        The model that has been trained to detect whether a team will score
        under 20 points within a quarter.

    """
    nba_stats = pd.read_csv(data_path)

    # get all rows from cols data and beyond
    nba_stats = nba_stats.loc[:, 'data':] 

    unique_teams = nba_stats['opponent_names'].unique().tolist()

    if save_data:
        save_binary('data/unique_teams.pkl', unique_teams)

    # removing the final score and date.  just want quarters
    nba_stats = nba_stats.drop(['date', 'final_score', 'opponent_points',
                                'diff_points'], axis=1)

    nba_stats = pd.get_dummies(nba_stats)
    nba_stats.loc[nba_stats['points'] < 20, 'points'] = 1
    nba_stats.loc[nba_stats['points'] >= 20, 'points'] = 0
    y_values = nba_stats['points']
    nba_stats = nba_stats.drop('points', axis=1)

    svm = SVC()
    print("Training in session!")
    svm = svm.fit(nba_stats, y_values)

    if save_data:
        if not shorten_data:
            save_binary('data/nba_X_training_data.pkl', nba_stats) 
        else:
            shortened_data = nba_stats.iloc[0:2, :]
            save_binary('data/shortened_X_data.pkl', shortened_data)

        save_binary('data/nba_Y_training_data.pkl', y_values)

    if save_model:
        save_binary("models/nba_quarter_under_20_SVM.pkl", svm)

    return svm


if __name__ == "__main__":
    create_quarter_under_20_model(save_data=True, save_model=True,
                                  shorten_data=True)