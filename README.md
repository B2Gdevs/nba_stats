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
