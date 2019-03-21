# nba_stats
This repo houses a program made for a friend.  It is a small sorta ad-hoc program found in the nba scrape folder that is used to identify when a team will score < 20
points in any given quarter.  In the same folder you will find scripts using the scrapy library.

### Model Disclaimer
The model used is an SVM which has an 85% accuracy rating, but I would take that with a grain of salt as that does not mean much in this case.
The precision and recall is very good for predicting when a team will NOT be < 20.  Though it has very good precision (100%) for detecting
when a team will be < 20 points,  it doesn't have good recall (11%) thus meaning that it would be hard pressed to actually say that a team
will be < 20.

### Usage
Just run, 

```python

python main_nba.py
```

and it will start up the main menu. It uses an old style of menu that one would fine in a classroom made by students just learning.
This was made this was due to time constraints.

##### Main Menu
![Image of Main Menu](https://github.com/B2Gdevs/nba_stats/blob/master/main_nba.py)

### Retraining

To retrain a model look at the training.py file.  The file will search for the
data.csv file within the data folder.  Replace that with data that is similar
and adjust the parsing and training accordingly.  The documentation in the
training.py file should be enough to help you create a different model.  However,
if you do create a new model with different columns that will likely cause the application
to fail and a partial rewrite of the application will be necessary.

## Disclaimer
This program has an 85% accuracy based on data gathered since 2012. While it is
good, there is always a chance it might not model current teams well!

Also this application was not built for reuse and is basically a one use only. 
There were and are no plans to make this application do more than what it is able to do now.
Therefore, the code is not a modular.

