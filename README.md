# AI Course & Python Projects 🚀

Welcome to my repository! This project tracks my learning journey in Artificial Intelligence and Python development.

## 📁 Project Structure
* **python_Projects/** - Contains various Python scripts including the "Python Ka Onion" project.
* **Course Work** - Files and exercises from my AI studies.

## 🚀 Getting Started
To use these files locally:
```bash
git clone [https://github.com/admilucky1-cyber/ai_course.git](https://github.com/admilucky1-cyber/ai_course.git)
cd ai_course
🛠️ Requirements

    Ubuntu 22.04 or 24.04

    Python 3.x

    Git
🏥 Heart Disease Classification Project
Project Overview

This project uses machine learning to predict whether or not someone has heart disease based on their medical attributes. It follows a complete data science workflow, from data exploration to model deployment.
The Goal

Given clinical parameters about a patient, can we predict if they have heart disease?
Data

The data used is the UCI Heart Disease Dataset, which includes features such as:

    Age, Sex, Chest Pain type (cp)

    Resting Blood Pressure (trestbps)

    Cholesterol (chol)

    Max Heart Rate (thalach)

Models & Tools Used

    Language: Python

    Libraries: Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn

    Model: Logistic Regression (Tuned using GridSearchCV)

Key Results

After hyperparameter tuning and 5-fold cross-validation, the model achieved:

    Accuracy: ~82%

    Precision: ~82%

    Recall: ~90% (High recall is vital here to avoid missing sick patients!)

    F1-Score: ~85%

Visualizations

    Confusion Matrix: Helped identify false negatives and false positives.

    ROC Curve: Analyzed the trade-off between true positive and false positive rates.

    Feature Importance: Visualized which medical factors (like chest pain and heart rate) most influenced the model's decision.

How to Run

    Clone the repository.

    Create the environment using the provided environment.yml file:
    conda env create -f environment.yml

    Open the Jupyter Notebook to see the full analysis.

📱 Phone Data Cleaning & Price Prediction

This project uses Machine Learning to predict smartphone prices based on technical specifications. It includes a robust data cleaning pipeline to handle inconsistent units and categorical features.
📊 Project Overview

The goal of this model is to estimate the market value of a mobile device using features like brand, color, and memory capacity.
Key Features

    Make: The manufacturer (e.g., Samsung, Apple, Google).

    Colour: The aesthetic finish of the device.

    Memory (kb): Internal storage capacity, standardized to Kilobytes (KB).

    Sim Cards: Number of supported SIM slots.

🧹 Data Cleaning Pipeline

To ensure the model receives high-quality data, the following steps were taken:

    Unit Standardization: All memory values (MB, GB) were converted to Kilobytes (KB) to ensure a uniform numerical scale.

    Handling Missing Values: Null entries in the 'Make' or 'Price' columns were dropped or imputed.

    Categorical Encoding: Brand and color names were transformed into numerical values using One-Hot Encoding (or Label Encoding).

    Outlier Detection: Removed extreme pricing entries that could skew the regression gradient.

🤖 The Model

We utilized a Linear Regression (or specify your model, e.g., Random Forest) approach.
Current Challenges

    Feature Scaling: Due to the large magnitude of the Memory(kb) feature (e.g., 128,000), the model is highly sensitive to storage capacity.

    Price Extrapolation: Predictions for high-capacity modern phones may result in high price estimates if not properly normalized.

🚀 How to Use

    Clone the repo: git clone https://github.com/yourusername/phone-price-prediction.git

    Install dependencies: pip install pandas scikit-learn

    Run the prediction script:

Python

# Example snippet from your code
test_phone = pd.DataFrame({
    "Make": ["Samsung"],
    "Colour": ["White"],
    "Memory(kb)": [128000.0],
    "Sim Cards": [2]
})
model.predict(test_phone)

🛠 Future Improvements

    Implement StandardScaler to handle the large KB integer values more effectively.

    Add more features like Battery Capacity (mAh) and Screen Size.

    Incorporate a Web UI using Streamlit for real-time price estimation.
