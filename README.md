# The Access Dilemma
An analysis on the diabetic and non-diabetic population in the United States regarding socioeconomic status. 

Drops of Jupyter group - [Amy Ying Lin](https://github.com/amyylin1), [Elina Dart](https://github.com/DartElina), [Manny Linares](https://github.com/MRLinares), [Kevin Daniliuk](https://github.com/DaniliukK95).
_________________________________________
## Overview
### Topic
Our topic is on diabetes in the United States and the correlation of socioeconomic factors to this disease.  

### Background
_Diabetes_ is a chronic condition that affects the way the body processes blood sugar (glucose). It occurs when the body does not produce enough insulin, or when the body's cells do not properly use the insulin it has produced. Insulin is a hormone that helps regulate blood sugar levels but if not properly managed, diabetes can lead to serious health complications, including heart disease, stroke, kidney damage, blindness, and nerve damage.

Some Statistics:
- Diabetes is a leading cause of death and disability, and it is the seventh leading cause of death globally.
- Type 2 diabetes is the most common form of diabetes, accounting for around 90% of all cases (The one you can develop).
- In 2021, an estimated 34.2 million people in the United States, or 10.5% of the population, had diabetes.
- The prevalence of diabetes has been increasing in recent years, with the number of people with the condition increasing by 2 million per year since 2014.
- African Americans, Hispanic/Latino Americans, American Indians, and Alaska Natives have a higher prevalence of diabetes than non-Hispanic whites.

_Socioeconomic factors_ are social and economic conditions that can influence an individual's or group's health, well-being, and access to resources and opportunities. These factors can include things like income, education, occupation, housing, and access to healthcare and social services.

### Objective
The objective of this analysis is to understand the relationship between socioeconomic status and diabetes.  The article mentioned from “The World Bank” has identified a link between poverty and disease. The other article mentioned “Diabetes Journal” reported that those with lower socioeconomic status have higher diabetes mortality. These articles indicate a relationship between low socioeconomic status and barriers to quality healthcare access. The number one way for people with lower socioeconomic status to achieve better results is to catch their diabetes early. Individuals may not see the value in regular physicals, or struggle to afford them. The result is a late diagnosis.

We chose this topic because of our common knowledge and interest in the disease with our previous experience and medical history. Diabetes is very common and there is a high probability that everyone in this room knows at least one person affected by it. This also means that we would be able to access vast amounts of data related to the topic. Knowing that communities of lower socioeconomic status are more heavily impacted, we wanted to learn why? 

### Questions to address with this study 
- What demographics and socioeconomic factors are correlated with diabetes?
   - Based on these factors, who will likely get diabetes? 
   - How successfully can demographics and socioeconomic status predict diabetes?
- What are changes/solutions that can be made to positively impact this issue?

### Description of the data sources
The NHIS tracks the health status and health care access of Americans and has been doing so since 1957. Using this data which tackles national health objectives, they work to identify and bring more information to significant health problems. The data size we extracted from the NHIS contains about 30,000 rows (individuals) and 622 columns (variables). The variables we are focusing on include demographics, health status, insurance, and income. 

- Data Source: [2021 National Health Interview Survey (NHIS) from the Centers for Disease Control and Prevention (CDC)](https://www.cdc.gov/nchs/nhis/2021nhis.htm)
- adult21.csv (https://github.com/DaniliukK95/Drops_Of_Jupyter/blob/Kevin_D_Week4/1_Raw_data/adult21.csv)
   - This CSV is the RAW data of everything.
- adult-summary.pdf (https://github.com/DaniliukK95/Drops_Of_Jupyter/blob/Kevin_D_Week4/1_Raw_data/adult-summary.pdf)
   - This PDF contains the descriptions of the variables.
- adult-codebook.pdf (https://github.com/DaniliukK95/Drops_Of_Jupyter/blob/Kevin_D_Week4/1_Raw_data/adult-codebook.pdf)
   - This PDF explains the meanings of the numerical values. 
- readme.txt (https://github.com/DaniliukK95/Drops_Of_Jupyter/blob/Kevin_D_Week4/1_Raw_data/readme.txt)
   - It is important to read this text file for running the code. 
_________________________________________
## Data Cleaning and Analysis
The team used Jupyter Notebook, Python, Pandas and Numpy to extract, transform the data and load to SQL database. In this process we explored the data with the support of the data Summary and Codebook to translate the coded categorical data. Then using Tableau we visualized the data in a series of pie charts and graphs. Further analysis was completed using Machine Learning and Logistic Regression. 

### Database Storage
PGAdmin is the tool we used for our database. We imported, cleaned, and transformed CSVs using Pandas and integrated the data into our other analysis tools. PgAdmin4 was also used to perform analysis. The images below include first: the ERD, which illustrates the structure of th database. Then, the second image is presented to depict a join query that joins our tables so a user can compare socioeconomic demographics alongside an individual's health status. 

![ERD](https://github.com/DaniliukK95/Drops_Of_Jupyter/blob/e1182de36d7d52bbcd8f819ee655abede02891bf/images/ERD_12_21_22.png)

![Join](https://github.com/DaniliukK95/Drops_Of_Jupyter/blob/29c761926660afb86efdce3850198d08b267529b/images/Join%20Query%20.png)

#### Our Sample Data contains:
  - Over 29,000 observations.
  - 3,134 individuals with Diabetes.
  - This is just over 10% and comparable with population estimates. 
  - 45% of our sample is male.
  - 75% White, 11% African American, 6% Asian.
  - Average Poverty Ratio is 4 (meaning income is 4 times the national poverty threshold).
  - 39% have attained at least a bachelor's degree.
_________________________________________
## Dashboard
The following link connects to our [Tableau](https://public.tableau.com/app/profile/amy8818/viz/finalproject_16711568635250/Story2?publish=yes) which houses our exploration of the data and tells the story we learned from it. We have also integrated D3.js for a fully functioning and interactive dashboard website. It is hosted on a local server while we are in development of our flask app.

### How to navigate through the dashboard website 
![Dashboard](https://github.com/DaniliukK95/Drops_Of_Jupyter/blob/17bd6c2227b9fb99b1b23f48c49b2dfbeec67dd7/images/dashboard.png)
Our dashboard website integrates our Data, Prediction app, and Tableau in one location. Along the top we have a navigation bar that can take you through the different elements of the dashboard. The home button will show the user the top portion of the page which has our basic information. The predict button will bring the user to second area of the page which allows the user to input their information to then predict a score of their chances of having diabetes. When the user presses the predict button after filling in the required fields, it will redirect them to a new page with the results. The dashboard button will take users to the Tableau website which has our storyboard highlighting the visualizations we created through the data. Finally, the data button will bring users to the end of the page which has a filterable table that allows users to navigate through the sample data. 
To run the dashboard website, the user must navigate to the dashboard folder of this repository in terminal. Once in the folder, activating the machine learning environment (mlenv) is crucial. With the mlenv active and our terminal in the proper folder, the code `python app.py` is ran and the http link generated can be opened in a browser. 

### Exploring Data with Visualizations in Tableau
These visualizations demonstrate the variables against the total sample size of individuals with (brown) and without (blue) diabetes.

- Fig. BMI and diabetes. This bar chart shows the correlation between BMI and Diabetes. It is a linear relationship, so as the BMI increases, the incidence of diabetes increases. 

![BMI_diabetes.png](https://github.com/DaniliukK95/Drops_Of_Jupyter/blob/main/images/BMI_diabetes.png)

- Fig. Race and diabetes. This bar chart shows the correlation between race and diabetes. Here we can assume that certain racial groups have higher incidences  of diabetes which are hispanics, black/african american, and american indian/alaskan native. 

![race_diabetes.png](https://github.com/DaniliukK95/Drops_Of_Jupyter/blob/main/images/race_diabetes.png)

- Fig. Education and diabetes. This bar chart shows the correlation between education and diabetes. We can see that the higher the education, the lower the incidences of diabetes. 

![tableau_ed.png](https://github.com/DaniliukK95/Drops_Of_Jupyter/blob/main/images/tableau_ed.png)

- Fig. Poverty ratio and diabetes. This bar chart shows the correlation between poverty ratio and diabetes. The higher the poverty ratio (the more wealthy you are) is, the lower the incidence of diabetes is. 

![tableau_pov_rat.png](https://github.com/DaniliukK95/Drops_Of_Jupyter/blob/main/images/tableau_pov_rat.png)

- Fig. Example of our json dataset in VSCode.

![dataset_example](https://user-images.githubusercontent.com/108758105/211934080-6ad9cf15-77f2-4ac0-b4d0-a351f5adf410.png)

- Fig. Snippet of json data extrator using d3.select

![dataframe_extractor](https://user-images.githubusercontent.com/108758105/211934383-8a29215f-c2f1-49c4-8d5f-e41d332dcb97.png)

- Fig. saveDataToPickle function using javascript.  Eventually we moved to a Flask app, but this code successfully pulls the data and creates a list to push to a pickle file.

![predictor_function](https://user-images.githubusercontent.com/108758105/211934725-e12d6fa8-5ba3-4d47-aeba-cc8990da9eaf.png)

- Fig. HTML example of our header.

![html_example_header](https://user-images.githubusercontent.com/108758105/211934814-fcd8d65b-053b-4563-808b-81aab340a523.png)

- Fig. HTML snippet of our Tableau Dashboard code embedded from Tableau website.

![tableau_html](https://user-images.githubusercontent.com/108758105/211934975-b9475a05-3a16-40ba-8957-1e0ef7c94518.png)

- Fig. HTML code of our Predictor interactive chart.

![html_predictor_example](https://user-images.githubusercontent.com/108758105/211935133-ad4c536f-4e4d-43f2-810e-f1db92efa394.png)


_________________________
### Machine Learning
#### Description of preliminary data processing with Machine Learning
- First, all data is imported from the database into the Google Colab Notebook that implements the Machine Learning.
- [scikit-Learn](https://scikit-learn.org/stable/) is the machine learning data analysis library we used to create our supervised models.
- We converted categorical attributes with pandas `get dummies` code.

#### Description of data features selection
- We used a logit function to identify which of our variables were statistically significant. We dropped variables that were insignificant to diabetes such as Region, and General Health Status. General Health Status was a self-selecting variable, individuals rated their health, and this was not relevant to the outcome of diabetes. 
- Features:  variables of demographics/socioeconomic status (sex, race, education, poverty ratio), diabetic-related health status (weight, age, and BMI). 
- Target: Diabetes.
- Preprocessing data was essential due to the high number of categorical variables from our data set.  
- All variables (except for weight, age, and poverty_ratio) are categorical variables.
- Data is pre-processed with [preprocessing module](https://scikit-learn.org/stable/modules/preprocessing.html.).

#### Description of how data is split into the training and testing sets
- Data is split into random training and testing subsets with [the model_selection module](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html).
- We end up with four sets:  X is split into X_train and X_test sets, and y is split into y_train and y_test sets. 
- We have an unbalanced data set (22,000 without diabetes vs 2500 with diabetes) so training and testing subsets are scaled using [Standard Scaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler.fit_transform). 
- Samples are then oversampled using RandomOverSampler as the last step before training the model. 

#### Model Explanation: Logistic regression 
- We chose logistic regression to predict diabetes based on the socioeconomical factors listed above.
- The target variable only has two possible values, whether a person has been diagnosed with diabetes before or not. When this classification model encounters new data, it predicts whether the individual has diabetes.
- Logistic Regression is then trained on the scaled oversampled training data and tested for accuracy on the testing data.
- Accuracy score: 82.5%
- Precision Score: 35.5%
- Recall Score: 81.7%
- Benefit: logistic regression is relatively simple to execute and understand.
- Limitation: Due to so many categorical variables possible models to train and test in the future could be a Support Vector Machine model, or Random Forest Classifier. 
_________________________________________
## Results and Conclusion
Our machine learning model is highly accurate, and highly sensitive, so it may result in a false positive. However, since our aim is to catch diabetes earlier, we believe this is a positive outcome. 

We used this trained logistic model and integrated it into a flash app. In the end we have produced an app that takes in user input (weight, height, age, income, household size, education background, gender, and race) transforms their data, scales it to fit our machine learning predictive model and produces the probability that an individual has diabetes. This allows users to measure the probability of diabetes from the comfort of their own homes. Our model has an 82.5% accuracy score, 35.5% precision, and 81.7% recall score. 

This app is a solution that helps individuals take matters into their own hands. The app cannot replace visiting your primary care doctor. However, if you we are unable to see a doctor, this tool allows you to measure your probability of having diabetes. It aims to help people get diagnosed as early as possible, so people can live longer with better health outcomes. 

### Things we would have done differently and problems we encountered
- Our project was aimed at addressing access of care for low socioeconomic status individuals. So, when we began the project and downloaded the NHIS data we were initially overwhelmed by 30,000 rows and 600+ columns. We reduced our sample columns to our variables of interest. We still have over 40 columns but perhaps we should have analyzed the correlations of the initial variables from our data set. In the future we would run a correlation function on the entire data set to identify variables of interest in addition to the SES variables. We do have three team members with medical/bio-science backgrounds and used their background knowledge to identify the health indicators most correlated with diabetes. Therefore, we kept variables such BMI, Weight, and Age. 
- There is a difficulty with accessing health data because of privacy issues and lack of volunteers.  Some information is kept private because of the individual’s preference for privacy. Other information is inaccessible because of databases that are owned by private institutions or require payment for access. In terms of lack of volunteers, there are many Americans who do not want to participate in these studies which leaves out a lot of data that can be used. If we had access to the private data or had the chance to get more Americans to participate in these surveys, we could have created a more robust model with even more intimate data.
- Another issue we encountered is the type of variables in our dataset. Because this data has a vast number of categorical variables, we could test the SVM and RFC machine learning models which are better suited for this type of dataset. 
- For potential future investors, with our given framework we could build in an API that connects to the CDC database to keep adding more data as the CDC releases it. We can then load new data into our database and retrain our model. With more data being implemented, the model can create stronger predictions. Also with more time and information, we could start implementing this same approach to other demographics, and even the same workaround for other diseases. 
_________________________________________
## Tools, Languages and Resources

>**Languages:** <br>
>Python, JavaScript, PostgreSQL <br> 

>**Software:** <br>
> Flask, VS Code, JupyterNotebook, Pandas, Numpy, Scikit-Learn, pgAdmin4, GoogleCollab, TableauPublic, Github, Bootstrap, HTML, CSS, QBD (for ERD image generation)<br>

>**Resources:** <br>
>[2021 National Health Interview Survey (NHIS)](https://www.cdc.gov/nchs/nhis/index.htm), [Centers for Disease Control and Prevention](https://www.cdc.gov/), [Google](https://www.google.com/), [Stack Overflow](https://stackoverflow.com/), [Columbia Engineering BCS](https://courses.bootcampspot.com/), [The World Bank - link between poverty and disease](https://www.worldbank.org/en/topic/health/brief/poverty-health), [Diabetes Journal - lower socioeconomic status have higher diabetes mortality](https://diabetesjournals.org/care/article/36/1/49/38282/Socioeconomic-Status-and-MortalityContribution-of), [population rate of diabetes](https://ourworldindata.org/grapher/diabetes-prevalence)

>**Google Slide Presentation:** <br> 
>[Link to Slide Presentation](https://docs.google.com/presentation/d/1frQCFUMLjLESFChDFPRKfrWDBDM_eeRc/edit?usp=sharing&ouid=114235229897805055862&rtpof=true&sd=true)
>[Link to presentation Script](https://docs.google.com/document/d/1FlnguPvooM4zVVRG-qw5w-PT04YKLdCi99K6-zTubSg/edit?usp=sharing)
