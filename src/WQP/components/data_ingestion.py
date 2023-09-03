import os
import sys
from WQP import logger
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path=os.path.join('artifact',"train.csv")
    test_data_path=os.path.join('artifact',"test.csv")
    raw_data_path=os.path.join('artifact',"raw.csv")

class DataIngestion():
    
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logger.info('Entered Data Ingestion Method')
        
        try:
            
            df=pd.read_csv('notebook/data/raw_data.csv')
            logger.info('Data Read Successfully')

            os.makedirs(os.path.join(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logger.info("Initiating Train Test Split")

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_Set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logger.info("Successfully Ingested")

            print( self.ingestion_config.train_data_path)       
            print(self.ingestion_config.test_data_path)
            print(self.ingestion_config.raw_data_path)

            return (

                self.ingestion_config.train_data_path,       
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )


        except Exception as e:
            print(e)
            logger.info("Data Couldn't be read")

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()