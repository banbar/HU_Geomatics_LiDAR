from indoor_area import *
import json

# Navigate to the panoromas folder
# Find the images that enter/exit a room
# Specify its last meaningful digits 

# Classroom 4:
image_enter = [690] #enter time
image_exit = [723] #exit time


configuration_file = 'configuration.yaml'
conf = read_configuration(configuration_file)
f = open(conf['image_timings_path']) # obtain the image timings
data = json.load(f)

for i in range(len(image_enter)):
    print("***   Processing Indoor Space - ", i+1)

    conf['time_start'] = return_image_time(data, image_enter[i])
    conf['time_end'] = return_image_time(data, image_exit[i])
    
    rowskip_enter, time_enter = find_time(conf) 
    
    if(rowskip_enter != -1):
        rowskip_exit, time_exit = find_time(conf, enter = rowskip_enter)  
        
        pcd = visualise_pcd(conf, 
                            rowskip_enter, 
                            rowskip_exit, 
                            time_enter, 
                            time_exit)
        
        cleaned_pcd = run_dbscan(conf, pcd)
    
        draw_histogram(conf,cleaned_pcd)
        calculate_area(cleaned_pcd)

# Closing file
f.close()
