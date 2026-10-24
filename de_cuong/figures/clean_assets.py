from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Load original user image
src_path = r'C:\Users\user\Downloads\Hinh4_So_do_khoi_4_tang_LANDSCAPE_TO_RO.png'
im_src = Image.open(src_path).convert('RGBA')

# 1. Clean Hand element
# Hand is at x: 80 to 860, y: 240 to 1480
# Notice that at the bottom of the hand (y around 1400-1460), there's a dashed line. Let's paint it white.
hand_crop = im_src.crop((90, 240, 850, 1460))
hand_arr = np.array(hand_crop)
# bottom 50 pixels: if there are black/gray dashed pixels, remove them
# Hand only reaches y ~ 1350 on the wrist
hand_crop = hand_crop.crop((0, 0, hand_crop.width, 1220))
hand_crop.save(r'smart-glove-hand-function-monitoring\de_cuong\figures\assets\clean_hand.png')
print('Hand cleaned:', hand_crop.size)

# 2. Clean MUX: The two purple boards
# Top board: x: 1000 to 1230, y: 940 to 1055
# Bottom board: x: 1000 to 1230, y: 1120 to 1235
mux_top = im_src.crop((1000, 940, 1230, 1055))
mux_bot = im_src.crop((1000, 1125, 1230, 1235))
# Combine them with clean space
mux_clean = Image.new('RGBA', (230, 230), (255, 255, 255, 0))
mux_clean.paste(mux_top, (0, 0))
mux_clean.paste(mux_bot, (0, 115))
mux_clean.save(r'smart-glove-hand-function-monitoring\de_cuong\figures\assets\clean_mux.png')
print('MUX cleaned:', mux_clean.size)

# 3. Clean ADS1115
ads_crop = im_src.crop((1340, 1030, 1550, 1195))
ads_crop.save(r'smart-glove-hand-function-monitoring\de_cuong\figures\assets\clean_ads.png')
print('ADS cleaned:', ads_crop.size)

# 4. Clean ESP32: x: 1700 to 1980, y: 1000 to 1205 (avoid bottom ghost text)
esp_crop = im_src.crop((1700, 1000, 1980, 1205))
esp_crop.save(r'smart-glove-hand-function-monitoring\de_cuong\figures\assets\clean_esp.png')
print('ESP cleaned:', esp_crop.size)

# 5. Clean Camera: x: 920 to 1220, y: 220 to 440
cam_crop = im_src.crop((920, 220, 1220, 440))
cam_crop.save(r'smart-glove-hand-function-monitoring\de_cuong\figures\assets\clean_cam.png')
print('Cam cleaned:', cam_crop.size)

# 6. Clean Depth: x: 1640 to 1990, y: 220 to 450
depth_crop = im_src.crop((1640, 220, 1990, 450))
depth_crop.save(r'smart-glove-hand-function-monitoring\de_cuong\figures\assets\clean_depth.png')
print('Depth cleaned:', depth_crop.size)

# 7. Clean Orange Pi: x: 1650 to 1960, y: 470 to 640
opi_crop = im_src.crop((1650, 470, 1960, 640))
opi_crop.save(r'smart-glove-hand-function-monitoring\de_cuong\figures\assets\clean_opi.png')
print('OPI cleaned:', opi_crop.size)

# 8. Clean Monitor: x: 2080 to 2620, y: 235 to 640
mon_crop = im_src.crop((2080, 235, 2620, 640))
mon_crop.save(r'smart-glove-hand-function-monitoring\de_cuong\figures\assets\clean_mon.png')
print('Mon cleaned:', mon_crop.size)

# 9. Clean Brain: x: 2250 to 2550, y: 990 to 1330
brain_crop = im_src.crop((2250, 990, 2550, 1330))
brain_crop.save(r'smart-glove-hand-function-monitoring\de_cuong\figures\assets\clean_brain.png')
print('Brain cleaned:', brain_crop.size)
