-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.
-- USE Drops_of_Jupyter;

CREATE TABLE Individual (
    ID				VARCHAR(12)   	NOT NULL,
    Age 			INT  			        ,
    Gender 			VARCHAR(10)   			,
    Race 			VARCHAR(50)   			,
    Education		VARCHAR(100)   			,
	Poverty_Ratio 	DEC(4,2)		        ,
	Region 			VARCHAR(15)   			,
    CONSTRAINT "pk_Individual" PRIMARY KEY (ID)
);

CREATE TABLE General_Health_Status (
    ID 			    VARCHAR(12)   	NOT NULL,
    Diabetes 	    VARCHAR(10)   	        ,
    Prediabetes     VARCHAR(10)             ,
    Weight 		    INT   			        ,
    Categorical_BMI VARCHAR(50)  	        ,
    CONSTRAINT "pk_General_Health_Status" PRIMARY KEY (ID)
);

