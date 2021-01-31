# FEC_dataset_downloader
Dataset downloader for Google Facial Expression Comparison (FEC) dataset

This is the dataset downloader for FEC dataset. The related dataset can be found at https://research.google/tools/datasets/google-facial-expression/.

This repository is an automated downloader that uses the url provided by in the csv files of the dataset and crop it based on the coordinates given.

The code loads the image (from the url), crops it and saves it as jpeg format in designated folder. The image triplets are stored separately. Any errors will be recorded in a separated csv.

# Packages Used
Pandas 1.1.3, Scikit-image 0.17.2

# Disclaimer
It is highly recommended to have a real-time antivirus installed in your system as my antivirus shows alerts for potential malware during the download process.

# License
FEC_dataset_downloader is a downloader for Google Facial Expression Comparison (FEC) dataset.

    Copyright (C) 2021  Chuin Hong Yap

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
