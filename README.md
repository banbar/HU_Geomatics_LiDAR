# HU_Geomatics_LiDAR

This repository contains the source code for the paper submitted to GeoAdvances 2024 **A Reproducible Approach for Estimating Indoor Space Area on Mobile Lidar Dataset Using DBSCAN**.

[Dataset](https://figshare.com/articles/dataset/Hacettepe_University_Department_of_Geomatics_Engineering_LiDAR_Scan/24866175/1)

The required packages are as follows:
* open3d - `pip3 install open3d`
* markupsafe - `pip install markupsafe==2.0.1`
* werkzeug - `pip install werkzeug==2.0.3`

The task is to estimate the indoor space area on the handheld LiDAR dataset by using the image timings.

This repo consists of three files:
1. **indoor_area.py**: This is the main library that has the data to process the mobile LiDAR dataset.
2. **configuration.yaml**: This is the configuration file. The contents of this configuration file are as follows:
<img src="/img/conf.jpg" alt="Configuration File" style="height: 200px; width:200px;"/>


The 'indoor_area.py' file contains the functions and library imports used. The 'test_indoor_area.py' file contains the code that needs to be run to replicate the experiment. The 'configuration.yaml' file contains the parameters used in the experiment. if the experiment is to be run with different parameters, the 'test_indoor_area.py' file can be run again by changing the parameters in this file.

When the 'test_indoor_area.py' file is executed: the point cloud data for the time interval specified in the configuration.yaml file will appear on the screen.
