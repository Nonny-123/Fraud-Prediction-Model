# FraudSense: Real-time Transaction Fraud Detection

---

## Overview

FraudSense is a robust machine learning-powered application designed to detect fraudulent financial transactions in real-time. Leveraging a pre-trained classification model, it provides instant predictions on whether a transaction is legitimate or fraudulent, helping to mitigate financial risks and secure assets.

This project demonstrates a practical application of machine learning in cybersecurity and finance, wrapped in an intuitive web interface built with Streamlit for easy interaction.

## Features

* **Real-time Prediction:** Get instant fraud predictions for individual transactions.
* **Intuitive User Interface:** A simple and clean Streamlit interface for inputting transaction details.
* **Key Transaction Features:** Utilizes critical features like `step` (time), `type` (payment method), `amount`, `transaction_type`, `net_sender`, and `net_receiver` for prediction.
* **Pre-trained Model:** Employs a pre-trained `fraud_cb.pkl` model, likely a CatBoost or similar gradient boosting model, for high accuracy.
* **Clear Output:** Clearly indicates "NOT FRAUD" or "FRAUD" status.

## Installation

To get FraudSense up and running on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourGitHubUsername/FraudSense.git](https://github.com/YourGitHubUsername/FraudSense.git)
    cd FraudSense
    ```
    *(Replace `YourGitHubUsername/FraudSense.git` with the actual URL of your repository)*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install pandas joblib streamlit
    ```
    *Ensure you have `joblib` installed, as the model is loaded using it.*

4.  **Place your trained model:**
    Make sure your pre-trained model file, named `fraud_cb.pkl`, is located in the root directory of the project. If your model has a different name or path, update the `model = joblib.load("fraud_cb.pkl")` line in `app.py` accordingly.

## Usage

Once you have installed the dependencies and placed the model file, you can run the Streamlit application:

1.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
    *(Assuming your Streamlit application code is in a file named `app.py`)*

2.  **Access the application:**
    Your web browser should automatically open to the Streamlit application (usually at `http://localhost:8501`).

3.  **Enter transaction details:**
    Use the input fields in the Streamlit interface to enter the relevant details for a transaction:
    * **Time (step):** Time in hours.
    * **Payment Type:** Type of payment (e.g., PAYMENT, TRANSFER, CASH\_OUT).
    * **Amount:** Transaction amount.
    * **Kind of transaction:** CM or CC (likely referring to transaction categories).
    * **Net amount sent:** Net amount sent by the sender.
    * **Net amount received:** Net amount received by the receiver.

4.  **Get Prediction:**
    Click the **"Predict Fraud"** button to see the transaction status: "NOT FRAUD" or "FRAUD".

## Model Details

The core of this application is a pre-trained classification model stored in `fraud_cb.pkl`. This model was trained on historical transaction data to learn patterns indicative of fraudulent activities. While the specific algorithm isn't explicitly defined in the provided code, the `joblib` loading suggests it's a scikit-learn compatible model, often used for powerful tree-based ensemble methods like CatBoost, LightGBM, or XGBoost, which are highly effective in fraud detection.

## Contributing

Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/YourFeature`).
6.  Open a Pull Request.

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

## Contact

For any questions or inquiries, please open an issue on this repository or contact [nonnyokonji@gmail.com].

## Author

Okonji Chukwunonyelim

Data Scientist|ML Engineer
