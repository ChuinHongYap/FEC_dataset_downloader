"""
FEC dataset downloader:
1. Download and crop based on log file.
2. Store separately in jpeg files.
3. There are lots of errors, unavailable etc which is recorded in a separate csv.
4. START_ROW is used to resume the dataset download (when error occurs).

"""
import pandas as pd
import csv
import os

from skimage import io

START_ROW = 0
INPUT_PATH = r""	# input path of FEC ground truth
TRAIN_FILE = r"faceexp-comparison-data-train-public.csv"
TEST_FILE = r"faceexp-comparison-data-test-public.csv"

OUTPUT_PATH = r"train"
# OUTPUT_PATH = r"test"

# make output folder
if os.path.exists(OUTPUT_PATH):
    print("Output folder exist")
    pass
else:
    os.mkdir(OUTPUT_PATH)

TOTAL_PATH = INPUT_PATH+TRAIN_FILE
# TOTAL_PATH = INPUT_PATH+TEST_FILE

csv_err = r'url_error_train.csv'
# csv_err = r'url_error_test.csv'

if os.path.isfile(csv_err):
	print("Error log exist")
	pass
else:
    with open(csv_err, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["subject","subcount","error"])

csv_file = pd.read_csv(TOTAL_PATH, header=None, error_bad_lines=False).to_numpy()

# labels of the dataset triplets
subcounts = ["1", "2", "3"]

for i in range(START_ROW, len(csv_file)):
    for j, subcount in enumerate(subcounts):
        try:
            url = csv_file[i,0+j*5]
            im = io.imread(url)
			
            height, width, _ = im.shape
            
            left = round(csv_file[i,1+j*5]*width)
            top = round(csv_file[i,3+j*5]*height)
            right = round(csv_file[i,2+j*5]*width)
            bottom = round(csv_file[i,4+j*5]*height)
            
            im = im[top:bottom:, left:right]
            
            output_name = (str(i+1)).zfill(6) + "_" + subcount + ".jpeg"
            io.imsave(OUTPUT_PATH + output_name, im)
			
		# Record error in a csv
        except Exception as err:
            print(err)
            ERR = str(err)
            with open(csv_err,'a', newline='') as f:
                writer = csv.writer(f, delimiter=',')
                writer.writerow([str(i+1),subcount,ERR])
            pass  
