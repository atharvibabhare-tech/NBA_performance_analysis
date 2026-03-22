# NBA_performance_analysis

##  Project Overview

This project analyzes NBA player statistics to understand performance, scoring patterns, and overall contribution using data visualization and exploratory data analysis (EDA).

---

##  Objectives

* Identify top-performing players
* Analyze scoring (points - pts) and rebounds (trb)
* Evaluate shooting efficiency (fg_pct, 3P%, FT%)
* Understand player contribution (assists, turnovers, etc.)
* Explore trends and distributions in player performance

---

##  Dataset

* Source: NBA player dataset (CSV)
* Contains:

  * Player details (name, age, position, team)
  * Performance stats (pts, trb, ast, etc.)
  * Shooting metrics (fg%, 3P%, FT%)

---

##  Data Preprocessing

* Removed/cleaned column names
* Handled missing values:
* Filled shooting percentages with 0
* Checked duplicates and data types
* Explored categorical columns (player, team, season)

---

## 📊 Key Analysis & Visualizations

###  Distribution Analysis

* KDE plot of points (pts) shows right-skewed data
* Most players score low to moderate points

###  Relationship Analysis

* Scatter plot (trb vs pts) shows a positive trend
* Higher rebounds generally relate to higher scoring

###  Performance Comparison

* Bar charts used to compare top players
* Helps identify high scorers and top rebounders

###  Statistical Insights

* Histograms and count plots used to understand data spread
* Outliers and skewness are clearly visible

---

##  Key Insights

*  More rebounds generally lead to more points
*  Most players have average performance
*  Top players are rare but impactful
*  Data is highly skewed (few high scorers)
*  Performance depends on multiple factors, not just one metric

---

##  Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

---

##  Conclusion

The analysis shows that while rebounds and scoring are related, player performance is multi-dimensional. Most players perform at an average level, while a small group dominates the game statistically.

---

##  Future Improvements

* Add player ranking model
* Use machine learning for performance prediction
* Build Power BI dashboard

---
