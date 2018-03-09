import argparse
import os
import random
import pandas
import numpy

print("separateTrainValWithCsv.py")
random.seed(0)

parser = argparse.ArgumentParser()
parser.add_argument('labelsFile', help='The csv file showing the labels in two columns: filename,class')
parser.add_argument('generatedFile', help='The generated file in three columns: filename,class,[train or valid]')
parser.add_argument('validationProbability', type=float,
                    help='The probability of putting a file in the validation set, [0, 1]')

args = parser.parse_args()

dataFrame = pandas.read_csv(args.labelsFile)
numberOfRows = len(dataFrame.index)
randomDraws = numpy.random.rand(numberOfRows)

trainOrValidList = []
for row in range(numberOfRows):
    if randomDraws[row] < args.validationProbability:
        trainOrValidList.append('valid')
    else:
        trainOrValidList.append('train')
dataFrame['usage'] = pandas.Series(trainOrValidList, index=dataFrame.index)

# Save generated file
dataFrame.to_csv(args.generatedFile, index=False)