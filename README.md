# FEC_dataset_downloader
Dataset downloader for Google Facial Expression Comparison (FEC) dataset

This is the dataset downloader for FEC dataset. The related dataset can be found at https://research.google/tools/datasets/google-facial-expression/.

This repository is an automated downloader that uses the url provided by in the csv files of the dataset and crop it based on the coordinates given.

The code loads the image (from the url), crops it and saves it as jpeg format in designated folder. The image triplets are stored separately. Any errors will be recorded in a separated csv.

# Packages Used
Pandas 1.1.3, Scikit-image 0.17.2

# Disclaimer
It is highly recommended to have a real-time antivirus installed in your system as my antivirus shows alerts for potential malware during the download process.
