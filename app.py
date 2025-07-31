import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
import shap
import matplotlib.pyplot as plt

# Title
st.title("🛡️ Real-Time Fraud Detection Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("Upload Transaction Log CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("📄 Sample Data", df.head())

    # Split features and labels
    if 'Class' in df.columns:
        X = df.drop(columns=['Class'])
        y = df['Class']
    else:
        X = df
        y = None

    # Fit Isolation Forest
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(X)
    preds = model.predict(X)
    preds = [1 if x == -1 else 0 for x in preds]  # -1 = anomaly

    df['Predicted_Fraud'] = preds

    st.subheader("🔍 Predictions")
    st.write(df[['Amount', 'Predicted_Fraud']])

    # Evaluate if true labels exist
    if y is not None:
        st.subheader("📊 Evaluation Metrics")
        st.text(classification_report(y, preds))
        st.write("ROC AUC Score:", roc_auc_score(y, preds))

        cm = confusion_matrix(y, preds)
        st.write("Confusion Matrix")
        st.write(cm)

    # SHAP Explainability
    st.subheader("🧠 Explainability (SHAP)")
    explainer = shap.Explainer(model, X)
    shap_values = explainer(X)

    # st.set_option('deprecation.showPyplotGlobalUse', False)
    shap.summary_plot(shap_values, X, plot_type="bar", show=False)
    st.pyplot(plt.gcf())
