# The Roadmap

Data Analysis → Machine Learning → Deep Learning → Computer Vision → Robotics,
with an embedded hardware track (ESP32 → STM32 → Pi/Jetson) running alongside.

**Pace:** ~15 h/week · **Rule:** 70% building, 30% courses · **Output:** one public project per phase.

The idea: every hardware project produces data or runs a model from the
software phase you are in. By Phase 5 they merge into one robot.

---

## Phase 0 — Foundations · Month 1

| Track | What to do |
|---|---|
| Software | Python basics, Git/GitHub, VS Code, virtual environments |
| Math | Refresh linear algebra + calculus (3Blue1Brown) |
| Hardware | Order the starter kit (below). Blink an LED on the ESP32-S3; read a pot through the ADC; print to Serial. |

**Projects**
- `week01/torque_preload.py` — simulated torque–preload fit ✅
- Plot one real CSV from the thesis experiments
- ESP32: button → LED → OLED "hello"

**Resources:** Kaggle Learn (Python, Pandas) · 3Blue1Brown · PlatformIO docs

**Done when:** you can write a 50-line script without looking up syntax every line, and flash firmware to the ESP32 on your own.

---

## Phase 1 — Data Analysis · Months 2–3

| Track | What to do |
|---|---|
| Software | pandas, numpy, matplotlib, seaborn, Jupyter; cleaning, grouping, plotting, basic statistics |
| Hardware | ESP32 sensors over I2C/SPI; Wi-Fi streaming to a Python receiver |

**Projects**
1. **Thesis EDA** — clean and analyze the real torque / preload / friction data; nut factor vs. torque with uncertainty bands.
2. **Kaggle dataset report** — e.g. vehicle / engine data; five insights, written up.
3. **⚡ Wireless load-cell logger** — ESP32 + HX711 + load cell → Wi-Fi → Python → CSV → pandas analysis (drift, noise, calibration curve). A mini thesis rig.

**Resources:** *Python for Data Analysis* (Wes McKinney, free online)

**Done when:** you can take a messy CSV to a clean, well-plotted notebook in an afternoon.

---

## Phase 2 — Classical Machine Learning · Months 4–6

| Track | What to do |
|---|---|
| Software | Regression, classification, trees, random forest, gradient boosting, cross-validation, feature engineering (scikit-learn) |
| Hardware | IMU (MPU6050 / BNO085), sampling rates, filtering on-device; FreeRTOS tasks |

**Projects**
4. **ML vs. physics** — predict preload from torque and test variables; compare linear / random forest / XGBoost against your analytical nut-factor model.
5. **Kaggle tabular competition** — Titanic, then a Playground series. Aim for top 50%.
6. **⚡ Motion classifier** — record IMU data for different movements (walking, jumping, judo throws), extract features, classify with scikit-learn.

**Resources:** Andrew Ng's *Machine Learning Specialization* · Géron, *Hands-On Machine Learning* · StatQuest

**Done when:** you can explain overfitting, pick a validation strategy and beat a baseline honestly.

---

## Phase 3 — Deep Learning · Months 7–9

| Track | What to do |
|---|---|
| Software | PyTorch, neural nets, backprop, CNNs, RNN/LSTM, training loops, GPU on Colab/Kaggle |
| Hardware | TinyML: quantize a model, run it on the ESP32-S3 (TFLite Micro / Edge Impulse). Get the XIAO ESP32S3 Sense. |

**Projects**
7. **Dog-breed classifier, from scratch** — rebuild the bootcamp model in PyTorch without the old code.
8. **1D-CNN on sensor signals** — catheter tip prediction, or CWRU bearing fault classification.
9. **⚡ On-device gesture model** — train the Phase 2 IMU task as a small neural net, deploy it on the ESP32-S3, show the prediction on the OLED. No PC.

**Resources:** fast.ai *Practical Deep Learning* · Karpathy *Neural Networks: Zero to Hero*

**Done when:** you can write a PyTorch training loop from memory and debug a model that won't learn.

---

## Phase 4 — Computer Vision · Months 10–12

| Track | What to do |
|---|---|
| Software | OpenCV, camera models + calibration, features, detection (YOLO), segmentation, depth basics |
| Hardware | XIAO ESP32S3 Sense camera; Raspberry Pi 5 + camera for heavier pipelines |

**Projects**
10. **Measure with a camera** — calibrate a camera, then measure real object sizes in mm. Report the accuracy like an instrument.
11. **Custom YOLO** — collect and label your own dataset (bolts / nuts / washers), fine-tune, run live on the Pi.
12. **⚡ Edge vision** — person / object detection on the XIAO; send detections over Wi-Fi.

**Resources:** Shree Nayar, *First Principles of Computer Vision* · Stanford CS231n · OpenCV tutorials

**Done when:** you can calibrate a camera and explain every number in the intrinsic matrix.

---

## Phase 5 — Robotics & State Estimation · Months 13–18

| Track | What to do |
|---|---|
| Software | Kinematics, Kalman / EKF, sensor fusion, ROS 2, SLAM, path planning |
| Hardware | STM32 Nucleo (motor control, timers, encoders); ESP32 as micro-ROS node; Pi 5 (or Jetson Orin Nano) as the brain |

**Projects**
13. **Kalman filter** — fuse IMU + wheel encoders; compare raw vs. filtered.
14. **⚡ Motor controller** — encoder speed PID on STM32 or ESP32, tuned with measured step responses.
15. **🏁 Capstone rover** — rocker-bogie or differential drive:
    - ESP32/STM32: motors, encoders, IMU, Kalman filter → micro-ROS
    - Pi/Jetson: ROS 2, LiDAR SLAM, camera + YOLO detection
    - Everything from Phases 1–4 in one machine.

**Resources:** Labbe, *Kalman and Bayesian Filters in Python* · Lynch & Park, *Modern Robotics* · Thrun, *Probabilistic Robotics* · Cyrill Stachniss SLAM lectures · ROS 2 docs

**Done when:** the rover maps a room, knows where it is and finds an object.

---

## Hardware timeline

| When | Buy | ~Cost |
|---|---|---|
| Phase 0 | ESP32-S3 DevKitC-1, HX711 + 1–5 kg load cell, MPU6050/BNO085, SSD1306 OLED, breadboard, jumpers, USB-C cable | $40–50 |
| Phase 3 | Seeed XIAO ESP32S3 Sense | $15–20 |
| Phase 4 | Raspberry Pi 5 + camera module | $80–110 |
| Phase 5 | STM32 Nucleo-F446RE, motors with encoders, TB6612 driver, chassis, LiDAR (reuse capstone one if possible) | $80–150 |
| Later, only if needed | NVIDIA Jetson Orin Nano | ~$250 |

Buy only when the phase starts. Hardware you are not using yet is a drawer.

---

## Weekly rhythm (~15 h)

| Block | Hours |
|---|---|
| Course / reading | 4–5 |
| Software project | 6 |
| Hardware project | 3–4 |
| Log + README + commit | 1 |

## Habits
- Every project gets a README: problem → approach → results → what's next.
- Three-line daily log: what I did, what confused me, what's next.
- Write the code first, then ask an AI to review it — not the other way around.
- Three videos without writing code = stop and build something.
