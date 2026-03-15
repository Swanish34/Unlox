import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

st.title("EDA Dashboard")

# Upload dataset
file = st.file_uploader("Upload CSV File", type=["csv"])

if file is not None:
    df = pd.read_csv(file)

    st.subheader("Dataset Preview")
    st.dataframe(df)

    st.write("Dataset Shape:", df.shape)
    st.write("Columns:", df.columns)

    st.subheader("Summary Statistics")
    st.write(df.describe())

    numeric_cols = df.select_dtypes(include='number').columns
    st.sidebar.header("Visualization Controls")
    col = st.sidebar.selectbox("Select column for Histogram", numeric_cols)
    # Histogram
    # col = st.selectbox("Select column for Histogram", numeric_cols)

    fig, ax = plt.subplots()
    sns.histplot(df[col], kde=True, ax=ax)
    st.pyplot(fig)

    # Scatter Plot
    x = st.selectbox("Select X column", numeric_cols)
    y = st.selectbox("Select Y column", numeric_cols)

    fig2, ax2 = plt.subplots()
    sns.scatterplot(x=df[x], y=df[y], ax=ax2)
    st.pyplot(fig2)

    # Heatmap
    st.subheader("Correlation Heatmap")

    numeric_df = df.select_dtypes(include=['number'])

    fig3, ax3 = plt.subplots()
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax3)
    st.pyplot(fig3)