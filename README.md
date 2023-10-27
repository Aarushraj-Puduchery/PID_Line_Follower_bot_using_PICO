# PID-Line_Follower_Bot_using_PICO
A line follower bot is a type of autonomous robotic vehicle designed to follow a predefined path or track marked with contrasting lines, typically black on a light-coloured surface or vice versa. These robots employ a combination of sensors, such as infrared or optical sensors, to detect the contrast between the line and the surrounding area. By continuously analyzing the sensor data, the bot makes real-time decisions on how to adjust its wheels or propulsion system to stay centred on the line.

Line follower bots are popular in robotics competitions and educational settings, as they provide an engaging way to introduce students and enthusiasts to basic robotics principles, sensor technology, and programming. They serve as a fundamental example of closed-loop control systems and can be customized with various features, like obstacle avoidance and speed adjustments, to make them more versatile and adaptable to different scenarios. Line follower bots can be a great starting point for those interested in exploring the world of robotics and automation.

## Bot Pictures
|  | |
| --- | --- |
| ![IMG20231027135525](https://github.com/Aarushraj-Puduchery/PID_Line_Follower_bot_using_PICO/assets/97360295/5c04262d-78d9-4172-8f0d-b44616bd9ad4) | ![IMG20231027135332](https://github.com/Aarushraj-Puduchery/PID_Line_Follower_bot_using_PICO/assets/97360295/83722c8c-ebff-4084-beae-64003ab25b88) |
| ![IMG_20231027_135621](https://github.com/Aarushraj-Puduchery/PID_Line_Follower_bot_using_PICO/assets/97360295/30b0534c-8fbc-4949-879f-53dd342a5c3a) | ![IMG_20231027_180301](https://github.com/Aarushraj-Puduchery/PID_Line_Follower_bot_using_PICO/assets/97360295/e9020c8f-7a85-4b3b-b446-2115c92f46a5) |

## Components List
|  Name  | Cost | Quantity | Total Cost | Link |
| --- | --- | --- | --- | --- |
| Raspberry Pi Pico | ₹349.00 | 1 | ₹349.00 | https://robu.in/product/raspberry-pi-pico/?gclid=CjwKCAjwv-2pBhB-EiwAtsQZFKvp_N6wg1myDh3ZrxYuYITGakSPuR7BEPZ8T_HpXla4VJIWYvDOhxoCeMYQAvD_BwE |
| 7 IR Sensor Array- Analog | ₹749.00 | 1 | ₹749.00 | https://www.robojunkies.com/products/7-sensor-array-analog |
| Single IR Tracking Sensor Module | ₹33.00 | 2 | ₹66.00 | https://robu.in/product/tcrt5000-ir-reflex-tracking-sensor-module/ |
| N20-12V-600 Rpm Micro Metal Gear Motor | ₹269.00 | 2 | ₹538.00 | https://robu.in/product/n20-12v-600-rpm-micro-metal-gear-motor/ |
| TB6612FNG Dual Channel Motor Driver | ₹349.00 | 1 | ₹349.00 | https://www.robojunkies.com/products/tb6612fng-dual-channel-motor-driver-breakout |
| Mounting Bracket for N20 Micro Gear motors | ₹29.00 | 2 | ₹58.00 | https://robu.in/product/mounting-bracket-n20-micro-gear-motors/?gclid=CjwKCAjwv-2pBhB-EiwAtsQZFMyVAIrgacEo3SnLeiZb_c0rmLDukQiCUuQzv2EGzwINDnRaVgi07hoCHJsQAvD_BwE |
| Mini MP1584 DC-DC 3A Adjustable Buck module | ₹48.00 | 1 | ₹48.00 | https://robu.in/product/mini-mp1584-dc-dc-adjustable-buck-module-3a/ |
| N20 mini-vacuum steel-ball caster wheel | ₹75.00 | 1 | ₹75.00 | https://robu.in/product/ball-castors/?gclid=CjwKCAjwv-2pBhB-EiwAtsQZFJapkUm2pvyraM-fcvEbIFXAwsW7BcBFXMhT8CuGdiMnjmRCqo3y5RoCfbwQAvD_BwE |
| Orange 850mah 3S 30C/60C (11.1V) Lithium Polymer Battery Pack | ₹999.00 | 1 | ₹999.00 | https://robu.in/product/orange-850mah-3s-30c-60c-lithium-polymer-battery-pack-lipo/ |
| Nylon XT60 Connectors Male/Female (1 pairs) | ₹69.00 | 1 | ₹69.00 | https://robu.in/product/amass-nylon-xt60-connectors-male-female-pair/ |
| N20 wheel + tyre combo | ₹200.00 | 1 | ₹200.00 | https://www.robojunkies.com/products/n20-wheel-tyre-combo |
| 0.91 inch 128×32 Blue OLED Display | ₹183.00 | 1 | ₹183.00 | https://robu.in/product/0-91-inch-128x32-i2c-iic-serial-blue-oled-lcd-display-module/ |
| 5 x 7 cm Universal PCB Prototype Board Single-Sided 2.54mm Hole Pitch | ₹33.00 | 2 | ₹66.00 | https://robu.in/product/5-x-7-cm-universal-pcb-prototype-board-single-sided-2-54mm-hole-pitch/?gclid=CjwKCAjwv-2pBhB-EiwAtsQZFE5b9qHKxeqy_LWVFsEkEtWvAuZyjGFokjC_KK8nJEzkA3N0C3TE_xoCRrgQAvD_BwE | 
| 3 Pin SPDT Toggle switch | ₹70.00 | 1 | ₹70.00 | https://robu.in/product/5a-3-pin-spdt-toggle-switch/ |
| Tactile Push Button | ₹5.00 | 6 | ₹30.00 | https://robu.in/product/12x12x7-3mm-tactile-push-button-switch-round/ |
| Female Header pins | ₹20.00 | 5 | ₹100.00 | https://robu.in/product/2-54mm-1x40-pin-female-single-row-header-strip-pack-of-10/?gclid=CjwKCAjwv-2pBhB-EiwAtsQZFAtwQ3ul10GUEYZ4OoZSfY7DK1FfVSDdqT6manq-n7lpXNj7vYUe9xoCQpQQAvD_BwE |

> [!NOTE]
> Components price may vary.

## Schematic Diagram
![Schematic_PID Line Follower Bot](https://github.com/Aarushraj-Puduchery/PID_Line_Follower_bot_using_PICO/assets/97360295/bc085160-06fa-44f5-8fd1-ff6981a09144)

## CODE
1. `main.py` file which contains the basic setup and selection of the code according to the width of the line.
2. `PID_LF_3cm.py` file contains code for a 3cm width line which uses only 7 sensors.
3. `PID_LF_2cm.py` file contains code for a 2cm width line which uses all 9 sensors.
4. `KpValue.csv`, `KiValue.csv` and `KdValue.csv` are files which store the kp, ki and kd values.
5. `ssd1306.py` file is the library used for oled display.

> [!IMPORTANT]
> All the above files must be saved in the PICO.
## Chassis Design
> [!NOTE]
> Need To Update.

### References
https://www.instructables.com/Line-Follower-Robot-PID-Control-Android-Setup/
