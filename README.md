# ml-journey

My path from mechanical engineer to data analysis, ML, deep learning, computer vision and robotics.

## Roadmap

Full plan with resources and checkpoints: [ROADMAP.md](ROADMAP.md)

| Phase | Months | Software | Hardware (⚡) | Key projects |
|---|---|---|---|---|
| 0 | 1 | Python, Git, math refresh | ESP32-S3 basics | Plot lab data; ESP32 hello |
| 1 | 2–3 | Data analysis | ESP32 sensors + Wi-Fi | Thesis EDA; ⚡ wireless load-cell logger |
| 2 | 4–6 | Classical ML | IMU, FreeRTOS | ML vs. physics model; ⚡ motion classifier |
| 3 | 7–9 | Deep learning | TinyML on ESP32-S3 | Dog breeds from scratch; ⚡ on-device gesture model |
| 4 | 10–12 | Computer vision | XIAO camera, Pi 5 | Camera measurement; custom YOLO; ⚡ edge vision |
| 5 | 13–18 | Robotics & state estimation | STM32, micro-ROS, Pi/Jetson | Kalman filter; ⚡ motor PID; 🏁 capstone rover |

Rule: 70% building, 30% courses.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Log

- **Week 1:** environment set up, first plot (`week01/`).
