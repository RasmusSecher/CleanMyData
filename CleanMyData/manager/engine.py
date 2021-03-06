#Fix to Spark error
import os
os.environ["PYARROW_IGNORE_TIMEZONE"] = "1"

from pyspark.sql import DataFrame
import pyspark.pandas as pan
from clean.models import Upload, Document, Header
from .fileReader import *
from .fileWriter import *
from .modules.simpleUnitConversion import *
from .modules.module import *


class Engine:
    def __init__(self, spark, fileModel):
        self.spark = spark
        
        self.document = fileModel

        self.dataframe = fileReader(self.spark, self.document.file_path, self.document.file_extension)


    def getColumnNames(self):
        return self.dataframe.columns


    def getSchema(self):
        return self.dataframe.schema


    def cleanMyData(self):
        #TODO: add logic when modules can be merged
        file_headers = Header.objects.filter(document=self.document)
        panDataframe = self.dataframe.toPandas()
        for header in file_headers:
            if header.selected == True:
                currentType = header.header_preference.current_type
                desiredType = header.header_preference.desired_type
                if currentType == 'NON':
                    genericCleaner = Module(header, panDataframe)
                    panDataframe = genericCleaner.runCleaner()
                elif currentType == 'C' or currentType == 'K' or currentType == 'F':
                    uc = SimpleUnitConversion(header, panDataframe)
                    panDataframe = uc.temperatureConversion()
                elif currentType == 'KM' or currentType == 'MI':
                    uc = SimpleUnitConversion(header, panDataframe)
                    panDataframe = uc.distanceConversion()
                elif currentType == 'KG' or currentType == 'LB':
                    uc = SimpleUnitConversion(header, panDataframe)
                    panDataframe = uc.weightConversion()
                else:
                    pass
        self.dataframe = self.spark.createDataFrame(panDataframe)
        fileWriter(self.spark, self.document.file_path, self.document.file_extension, self.dataframe)


    #Add rows
    def unifyDataframes(self, firstFile, secondFile):
        if isinstance(firstFile, DataFrame):
            firstDataframe = firstFile
        elif firstFile != None:    
            firstDataframe = fileReader(self.spark, firstFile.file_path, firstFile.file_extension)

        if isinstance(secondFile, DataFrame):
            secondDataframe = secondFile
        elif firstFile != None:
            secondDataframe = fileReader(self.spark, secondFile.file_path, secondFile.file_extension)

        if len(firstDataframe.columns) == len(secondDataframe.columns):
            return firstDataframe.union(secondDataframe)

    #Add columns
    def joinDataframes(self, firstFile, secondFile, joinOn):
        if isinstance(firstFile, DataFrame):
            firstDataframe = firstFile
        elif firstFile != None:    
            firstDataframe = fileReader(self.spark, firstFile.file_path, firstFile.file_extension)

        if isinstance(secondFile, DataFrame):
            secondDataframe = secondFile
        elif firstFile != None:
            secondDataframe = fileReader(self.spark, secondFile.file_path, secondFile.file_extension)

        return firstDataframe.join(secondDataframe, on=joinOn, how='fullouter')

