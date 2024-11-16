# Objective

Create a prediction model that will predict how many bike rentals will be there based on features like season, holiday, weathersit, temp, atemp, and hum.

# Stages of the Project

- Data Collection
- Data Pre-Processing
- Model Selection
- Model Training
- Model Testing
- Result Analysis

# Data Collection

Used the pre-existing dataset from UCI: [Bike Sharing Dataset from UCI](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset)


# Data Pre-Processing

- Dropping columns casual, instant, dteday, registered, workingday, weekday, yr, month.
- Converting season column to One-Hot Encoding.

# Model Selection

- Poisson's Regression
- Random Forest Regressor

# Model Training and Testing

- Trained both Models on 80-20 split.
- Random State 42 for both of the models.

# Model Result Analysis

- Printing all the stats parametes for both models.
- Observing weightage of both the models.

# Sources

- https://files.eric.ed.gov/fulltext/EJ1173275.pdf
- https://medium.com/@theclickreader/random-forest-regression-explained-with-implementation-in-python-3dad88caf165
- https://medium.com/@kunalchhablani14/predicting-stock-prices-using-machine-learning-338ab2fe4e5b
- https://neptune.ai/blog/random-forest-regression-when-does-it-fail-and-why
- https://medium.com/@data-overload/understanding-poisson-regression-a-powerful-tool-for-count-data-analysis-b7184c61bfde
- https://bookdown.org/roback/bookdown-BeyondMLR/ch-poissonreg.html#introduction-to-poisson-regression
- https://education.illinois.edu/docs/default-source/carolyn-anderson/edpsy589/lectures/4_glm/4glm_3_beamer_post.pdf

# Videos

- https://www.youtube.com/watch?v=Obpz_Uvo2rQ
- https://www.youtube.com/watch?v=fClxnUwUFJE
- https://www.youtube.com/watch?v=v6VJ2RO66Ag
- https://www.youtube.com/watch?v=nxFG5xdpDto