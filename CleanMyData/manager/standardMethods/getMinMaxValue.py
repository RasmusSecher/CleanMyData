import pyspark.pandas as pan
#Calculate median from column values

def getMinimumValue(dataFrame: pan.DataFrame):
    return dataFrame.min()

def getMaximumValue(dataFrame: pan.DataFrame):
    return dataFrame.max()
