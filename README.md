# ✨ Simple Linear Regression Visualizer ✨

This interactive web application provides a hands-on demonstration of **simple linear regression**. Built with Python and Streamlit, it allows users to dynamically generate a dataset, visualize it, and see how a linear regression model fits a line to the data in real-time.

This project follows the **CRISP-DM (Cross-Industry Standard Process for Data Mining)** methodology, from understanding the business need to deploying the final application.

---

## 🚀 Features

*   **Interactive Controls:** Use sliders in the sidebar to instantly change the dataset parameters.
*   **Adjustable Slope (`a`):** Modify the slope of the underlying linear data.
*   **Variable Noise:** Increase or decrease the amount of random noise to see how it affects the model's fit.
*   **Custom Data Size:** Change the number of data points in the set.
*   **Real-time Visualization:** The scatter plot and regression line update instantly as you adjust the parameters.
*   **Model Insights:** See the original parameters alongside the parameters calculated by the regression model.
*   **Data Table:** View the raw generated data in a clear, scrollable table.

---

## 🛠️ Installation

To run this application locally, you'll need Python 3.x installed.

1.  **Clone the repository (or download the files):**
    ```bash
    git clone https://github.com/g114093002/AIOT_HW1.git
    cd AIOT_HW1
    ```

2.  **Install the required dependencies:**
    All necessary libraries are listed in `requirements.txt`. Install them with pip:
    ```bash
    pip install -r requirements.txt
    ```

---

## 🏃‍♀️ How to Run

Once the dependencies are installed, you can start the Streamlit application with a single command:

```bash
streamlit run app.py
```

This will start a local web server and open the application in your default web browser.

---

## 🧠 Applying the CRISP-DM Framework

This project was structured around the CRISP-DM lifecycle:

1.  **Business Understanding:** The goal was to create an educational tool to make the concept of linear regression more tangible and intuitive.
2.  **Data Understanding:** We decided to generate data from a known linear equation (`y = ax + b`) plus noise, as this allows for clear evaluation of the model's performance against a "ground truth".
3.  **Data Preparation:** The application prepares the data by generating X and y coordinates based on the user-defined parameters for slope, noise, and data volume.
4.  **Modeling:** A `LinearRegression` model from the `scikit-learn` library is used to fit a line to the prepared data.
5.  **Evaluation:** The model is evaluated visually. By comparing the red regression line to the scattered data points, users can intuitively judge the "goodness of fit". The displayed model coefficients also provide a quantitative evaluation against the original parameters.
6.  **Deployment:** The final model is deployed as an interactive Streamlit web application, making it accessible to end-users.