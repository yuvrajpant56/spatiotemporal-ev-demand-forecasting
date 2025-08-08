# 🔋 EV Charging Station Energy Usage Prediction using LSTM

This project predicts the energy consumption (`Energy (kWh)`) at electric vehicle (EV) charging stations using a deep learning model based on LSTM (Long Short-Term Memory) networks. The dataset contains real-world EV charging station logs from the City of Palo Alto, California.

---

## 🧱 Proposed LSTM Architecture
![LSTM Architecture] (Porposed_LSTM_)Architecture.png)

## 📌 Project Overview

- ✅ **Goal**: Predict the `Energy (kWh)` used during a charging session based on features like session duration, charging time, fee, and environmental savings.
- 🧠 **Model**: LSTM-based regression model built using TensorFlow/Keras.
- 📈 **Performance**:
  - **MAE**: `0.37`
  - **RMSE**: `0.57`
  - **R² Score**: `0.99`

---

## 📂 Dataset

- **File**: `EVChargingStationUsage.csv`
- **Size**: 33 columns × 259,415 rows


### Selected Features
- `Total Duration (hh:mm:ss)`
- `Charging Time (hh:mm:ss)`
- `Fee`
- `Gasoline Savings (gallons)`
- `GHG Savings (kg)`

### Target Variable
- `Energy (kWh)`

---

## 🛠️ Setup & Installation

This project is designed to run in **Google Colab**.

### Mount Google Drive

```python
from google.colab import drive
drive.mount('/content/drive')

