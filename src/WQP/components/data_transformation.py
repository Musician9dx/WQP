import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
import os 
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from WQP import logger

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")


class DataTransformation():
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    
    def get_data_transformer_object(self):

        logger.info("Just Started Data Transformation")

        try:
    
            numerical_features=["writing_score","reading_score"]
            categorical_features=[

                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]

            num_pipeline=Pipeline(

                steps=[

                    ("imputer",SimpleImputer(strategy="mean")),
                    ("scaler",StandardScaler())        
                
                ]
            )
            
            
            cat_pipeline=Pipeline(

                steps=[

                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()),
                ])
          
            logger.info("Both Pipelining Code Successfully Executed")
            logger.info("Starting Column Transformation")


            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_features),
                ("cat_pipelines",cat_pipeline,categorical_features)

                ]
            )

            return preprocessor 

        except Exception as e:
            logger.info("Error Occured"+ " "+ str(e))
        
        
    def initialize_data_transformation(self,train_path,test_path):  

        try:
            
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logger.info("Reading of Test and Train Data Successful")
            logger.info("Obtaining Preprocessing Object")

            preprocessor=self.get_data_transformer_object()



            target_column_name=['math_score']
            
            numerical_features=[

                "writing_score",
                "reading_score"
            
            ]
            
            categorical_features=[

                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]

            logger.info("Target and Input Split Initiated")

            input_feature_train=train_df.drop(target_column_name,axis=1)
            target_feature_train=train_df[target_column_name]

            input_feature_test=test_df.drop(target_column_name,axis=1)
            target_feature_test=test_df[target_column_name]

            logger.info("Target Input Split Successfull")

            logger.info("Initializing Transformation")


            input_feature_train=preprocessor.fit_transform(input_feature_train)
            input_feature_test=preprocessor.fit_transform(input_feature_test)

            logger.info("Preprocessing Successfull!!")

            return (

                input_feature_train,
                input_feature_test,
                target_feature_test,
                target_feature_train
            )



        except Exception as e:
            logger.info("Error has Occured In Data Transformation Pipeline" + " " + str(e))

if __name__=="__main__":
    obj=DataTransformation()
    print(obj.initialize_data_transformation("D:/INeuron/WQP/artifact/train.csv","D:/INeuron/WQP/artifact/test.csv"))
