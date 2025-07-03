# Beneath-The-Waves-Unraveling-Coral-Mysteries-Through-Deep-Learning

Beneath the Waves is an ambitious project that employs deep learning techniques to unravel mysteries surrounding coral reefs. By leveraging advanced algorithms and neural networks, this initiative aims to analyze and understand various aspects of coral ecosystems, contributing to conservation efforts and ecological research.

[Project Demo Video](https://drive.google.com/file/d/1Si7FWjB008F7ctPIKwVTpn8kut-opvpp/view?usp=drive_link)

---

## Table of Contents

- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Data](#data)
- [Web Application](#web-application)
- [Contributing](#contributing)

---

## Project Structure

```
.
├── 1. Project Initialization and Planning Phase/
├── 2. Data Collection and Preprocessing Phase/
├── 3. Model Development Phase/
├── 4. Model Optimization and Tuning Phase/
├── 5. Project Executable Files/
│   ├── Flask/
│   │   ├── app.py
│   │   ├── static/
│   │   └── templates/
│   └── Traing and Testing/
├── 6. Documentation and Demonstration/
├── README.md
└── ...
```

- **Flask/app.py**: Main web application for coral image classification.
- **Traing and Testing/**: Jupyter notebooks and scripts for model training and evaluation.
- **Data folders**: Contain images of healthy and bleached corals (excluded from GitHub for size).

---

## Setup & Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/Beneath-The-Waves-Unraveling-Coral-Mysteries-Through-Deep-Learning.git
   cd Beneath-The-Waves-Unraveling-Coral-Mysteries-Through-Deep-Learning/5. Project Executable Files/Flask
   ```

2. **Create a virtual environment (recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   Create a `requirements.txt` with the following content:
   ```
   flask
   tensorflow
   numpy
   ```
   Then run:
   ```sh
   pip install -r requirements.txt
   ```

4. **Model Weights:**
   - Download or place your trained model file (`waves_img.h5`) in the `Flask/` directory.
   - **Note:** The model file is excluded from the repository due to size.

---

## Usage

1. **Run the Flask app:**
   ```sh
   python app.py
   ```
   The app will start on [http://localhost:2222](http://localhost:2222).

2. **Web Interface:**
   - Go to the home page.
   - Upload a coral image to get a prediction (Bleached or Healthy).

---

## Data

- **Training and test images** are organized in `train/` and `test/` folders, each with `bleached/` and `healthy/` subfolders.
- **CSV files** (`train.csv`, `test.csv`) contain metadata or labels.
- **Note:** Datasets are excluded from the repository. Please contact the authors or use your own coral image datasets.

---

## Web Application

- Built with Flask and TensorFlow.
- Accepts image uploads and predicts coral health status using a trained deep learning model.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
