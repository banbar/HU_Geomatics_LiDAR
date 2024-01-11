# HU_Geomatics_LiDAR

This repository contains the source code for the paper submitted to GeoAdvances 2024 "A Reproducible Approach for Estimating Indoor Space Area on Mobile Lidar Dataset Using DBSCAN".

[Dataset](https://figshare.com/articles/dataset/Hacettepe_University_Department_of_Geomatics_Engineering_LiDAR_Scan/24866175/1)

The task is to estimate the indoor space area on the handheld LiDAR dataset by using the image timings.

The 'indoor_area.py' file contains the functions and library imports used. The 'test_indoor_area.py' file contains the code that needs to be run to replicate the experiment. The 'configuration.yaml' file contains the parameters used in the experiment. if the experiment is to be run with different parameters, the 'test_indoor_area.py' file can be run again by changing the parameters in this file.

When the 'test_indoor_area.py' file is executed: the point cloud data for the time interval specified in the configuration.yaml file will appear on the screen.
