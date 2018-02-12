import argparse
import os

print("separateTrainVal.py")

parser = argparse.ArgumentParser()
parser.add_argument('categoryDirectories', nargs='+', type=str,
                    help='The directories where the categories can be found')
parser.add_argument('validationProbability', type=float,
                    help='The probability of putting a file in the validation folder, [0, 1]')
parser.add_argument('destinationDirectory', type=str,
                    help='The destination directory. It must exist. It will contain train/ and val/ which will contain as many directories as the number of classes')
parser.add_argument('removeFilesInDestinationDirectory', type=bool,
                    help='Before copying the files in the destination directories, delete all the files that are already there')


args = parser.parse_args()
numberOfCategories = len(args.categoryDirectories)
if numberOfCategories == 0:
    raise ValueError("separateTrainVal.py: No category directory was specified")
# Check if each category directory exists
for categoryDirectory in args.categoryDirectories:
    if not os.path.isdir(categoryDirectory):
        raise NotADirectoryError("separateTrainVal.py: The category directory '{}' doesn't exist".format(categoryDirectory))

if args.validationProbability < 0 or args.validationProbability > 1:
    raise ValueError("separateTrainVal.py: The probability of putting a file in the validation folder ({}) doesn't belong to [0, 1]".format(args.validationProportion))

# Check if the destination directory exists
if not os.path.isdir(args.destinationDirectory):
    raise NotADirectoryError("separateTrainVal.py: The destination directory '{}' doesn't exist".format(args.destinationDirectory))

# Create train/ and val/ directories
trainDirectory = args.destinationDirectory + '/train'
if not os.path.exists(trainDirectory):
    os.mkdir(trainDirectory)
valDirectory = args.destinationDirectory + '/val'
if not os.path.exists(valDirectory):
    os.mkdir(valDirectory)

# Create train/class0/, train/class1/, ... and val/class0, val/class1, ... directories
for categoryDirectory in args.categoryDirectories:
    # Remove trailing slash
    if categoryDirectory[-1] == '/':
        categoryDirectory = categoryDirectory[:-1]
    categoryName = os.path.basename(categoryDirectory)

    print ("separateTrainVal.py: categoryName = {}".format(categoryName))
    trainCategoryDirectory = trainDirectory + '/' + categoryName
    if not os.path.exists(trainCategoryDirectory):
        os.mkdir(trainCategoryDirectory)

    valCategoryDirectory = valDirectory + '/' + categoryName
    if not os.path.exists(valCategoryDirectory):
        os.mkdir(valCategoryDirectory)
