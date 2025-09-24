import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# --- Business Understanding ---
st.set_page_config(page_title="Simple Linear Regression", layout="wide")
st.title("Simple Linear Regression Visualizer")
st.write("""
This application demonstrates a simple linear regression model. 
You can adjust the parameters of the dataset and see how the regression line changes.
This follows the CRISP-DM methodology, from understanding the business problem to deploying a model.
""")

# --- CRISP-DM Steps in Sidebar ---
st.sidebar.header("CRISP-DM Steps")
st.sidebar.markdown("""
1.  **Business Understanding**: Visualize linear regression.
2.  **Data Understanding**: We generate data based on a linear equation with noise.
3.  **Data Preparation**: You set the parameters for data generation below.
4.  **Modeling**: We use `scikit-learn` to fit a linear model.
5.  **Evaluation**: The model is evaluated visually by the plot.
6.  **Deployment**: This Streamlit app is the deployment.
""")


# --- Data Preparation & User Input ---
st.sidebar.header("Adjust Data Parameters")

# Allow user to modify parameters
a_param = st.sidebar.slider("Slope (a) of the line", -10.0, 10.0, 2.5, 0.1)
noise_param = st.sidebar.slider("Noise", 0.0, 50.0, 10.0, 1.0)
num_points_param = st.sidebar.slider("Number of points", 5, 500, 100, 5)
b_param = 5 # Intercept b is fixed for simplicity

# --- Data Generation ---
def generate_data(a, noise, num_points, b):
    X = np.linspace(0, 10, num_points)
    # Add some randomness to X as well to make it more realistic
    X_randomized = X + np.random.normal(0, 0.5, num_points)
    y = a * X_randomized + b + np.random.normal(0, noise, num_points)
    return X_randomized.reshape(-1, 1), y

X, y = generate_data(a_param, noise_param, num_points_param, b_param)
df = pd.DataFrame({'X': X.flatten(), 'y': y})


# --- Modeling ---
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Get model coefficients
a_fit = model.coef_[0]
b_fit = model.intercept_


# --- Evaluation & Visualization ---
st.header("Results")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Data and Regression Line")
    fig, ax = plt.subplots()
    ax.scatter(X, y, label='Generated Data')
    ax.plot(X, y_pred, color='red', linewidth=2, label='Regression Line')
    ax.set_xlabel("X")
    ax.set_ylabel("y")
    ax.set_title("Linear Regression Fit")
    ax.legend()
    st.pyplot(fig)

with col2:
    st.subheader("Model Details")
    st.write(f"Original slope `a`: **{a_param}**")
    st.write(f"Fitted slope `a`: **{a_fit:.2f}**")
    st.write("---")
    st.write(f"Original intercept `b`: **{b_param}**")
    st.write(f"Fitted intercept `b`: **{b_fit:.2f}**")
    st.write("---")
    st.write("The plot on the left shows the generated data points and the red line is the result of the linear regression model. You can see how well the model was able to estimate the original parameters.")
    st.write("Try changing the parameters in the sidebar to see how the model adapts!")

st.header("Generated Data")
st.write(df)
