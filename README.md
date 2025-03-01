﻿# Phishing-Detector
# ©Vishal Kaveri
## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/chocovish02/Phishing-Detector.git
    cd Phishing-URL-Detection
    ```

2. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Run the application:**

    ```sh
    python app.py
    ```

4. **Open your web browser and go to:**

    ```
    http://127.0.0.1:5000
    ```

## Usage

1. **Navigate to the homepage:**
    - Enter a URL you want to check for phishing.
    - Click on the "Check URL" button.

2. **View the result:**
    - The result page will show whether the URL is predicted to be phishing or not.

## Feature Extraction

The `feature_extraction.py` file contains the logic to extract various features from a given URL. These features include:

- URL length
- Number of digits
- Number of special
