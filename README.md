# Maids_Task
## The API Divided into the following:
### First Download the model from this link: https://drive.google.com/file/d/1iUF7kjiiVlRdpYVvkhNS1HgoXu7Z6OpB/view?usp=sharing
- [GET] /api/devices/id: Retrieve the specs of this ID
- [POST] /api/devices/add: Takes battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time, three_g, touch_screen, wifi As key and value in json in such order and Add it to the dataset (test.csv) .
- [POST] /api/devices/get: Retrieve all data in the dataset
- [POST] /api/predict/id: Predict the Price Range of this ID
- [POST] /api/predict/ten: Predict random 10 samples from the test set
