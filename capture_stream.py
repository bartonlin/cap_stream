import pafy
import cv2
import time
import os

url = "https://youtu.be/CNoYzsQrShw"
save_folder = './img/'
video = pafy.new(url)
best = video.getbest(preftype="mp4")

pre_day = 0
pre_string = '18_18_1_'
# format: pre_string + year-month-day_hourmin.log
while True:
    time_tag = time.time()
    if int(time_tag) % 60 == 0:
        try:
            capture = cv2.VideoCapture(best.url)
            grabbed, frame = capture.read()

            struct_time = time.localtime(time_tag)
            year = struct_time.tm_year
            month = struct_time.tm_mon + 1  # [0, 11] + 1
            day = struct_time.tm_mday
            hour = struct_time.tm_hour
            now_min = struct_time.tm_min

            save_path = save_folder + str(year) + '/' + str(month).zfill(2) + '/' + str(day).zfill(2) + '/'

            if pre_day != day:
                # check save folder exist
                if os.path.isdir(save_path):
                    pass
                else:
                    os.makedirs(save_path)

            # save between 5 am to 7 pm
            if 5 <= hour <= 18:
                # format: pre_string + year-month-day_hourmin.log
                save_file_name = pre_string + str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2) + '_' + str(
                    hour).zfill(2) + str(now_min).zfill(2)
                try:
                    cv2.imwrite(save_path + save_file_name + '.png', frame)
                    print('save ', save_file_name + '.png')
                except:
                    pass
            pre_day = day
        except:
            pass
