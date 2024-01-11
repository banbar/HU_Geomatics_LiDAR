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
<img src="/img/conf.jpg" alt="Configuration File" style="height: 300px"/>

3. **test_indoor_area.py**: This is the file to find the indoor space area of an input indoor space area. It could operate on multiple indoor space areas by extending the list `image_enter` and `image_exit lists`. Once the `visualize` and `writeout` parameters have been turned on, the following operations will be carried out with the attached images:

First, the points collected within the specified time frame would be obtained. The code would display the total number of points to be analysed as well as the number of points within  the downsampled dataset.
<img src="/img/all_points_room.png" alt="All points" style="height: 300px"/>

Second, DBSCAN algorithm would cluster points on the downsampled dataset.
<img src="/img/dbscan_clusters.png" alt="Clustered points" style="height: 300px"/>

Finally, the cluster with the highest number of points -main cluster- would be selected. This cluster is assumed to represent the points representing the indoor space. The number of points used to represent this cluster is also displayed on Python.

<img src="/img/main_cluster.png" alt="Indoor space points" style="height: 300px"/>

The histogram of the *x-*, *y-* and *z*-values of the main cluster are also saved as a file for further investigation.

<p float="left">
  <img src="/img/x_values.svg" width="256" />
  <img src="/img/y_values.svg" width="256" />
  <img src="/img/z_values.svg" width="256" />
</p>

The image timings for different indoor spaces (ranked based on the image enter time) are noted as follows:
| Room Name      | Image Enter      | Image Exit |
| ----------- | ----------- | ----------- |
| Classroom 1 (C1) | 463 | 498       |
| Classroom 2 (C2) | 504 | 541       |
| Men's Restroom | 551 | 564       |
| Utility Room | 572 | 576       |
| Women's Restroom | 583 | 598       |
| Classroom 3 (C3) | 606 | 643       |
| Security Room | 660 | 666       |
| Classroom 4 (C4) | 690 | 723       |
| Men's Restroom | 745 | 757       |
| Utility Room | 762 | 766       |
| Women's Restroom | 771 | 782       |
| GIS Lab | 814 | 832       |
| Office  | 839 | 864       |
| PhD Meeting Room | 868 | 883       |
| Kitchen | 957 | 966       |
