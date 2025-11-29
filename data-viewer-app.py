import streamlit as st
import pandas as pd
import plotly.express as px

# PAGE SETUP
st.set_page_config(
                    page_title="📁 CSV Data Viewer And Chart Generator 📊" , layout="centered" ,                          initial_sidebar_state="expanded"
                    )

# LOCK
st.title("🔐 Secure Currency Converter")
# FOR USER
password = st.text_input("Enter Password:", type="password")
# CORRECT PASSWORD
correct_password = st.secrets["APP_PASSWORD"]

# CONDITION
if password != correct_password:
    st.warning("Please enter the correct password to access the converter.")
    st.stop()   # App yahan ruk jayegi agar password wrong ho
# IF PASSWORD IS CORRECT
st.success("Password Correct! Access Granted ✔️")

# APP TITLE
st.title("📁 CSV Data Viewer And Chart Generator 📊")
st.markdown("📤 Upload Your CSV File To Explore Data And Generate Interactive Charts.")
# FILE UPLOADER
uploaded_file = st.file_uploader("📎 Choose a CSV file" , type=["csv"])

# CONDITION IF FILE OPEN
if uploaded_file:

    # LOAD AND READ CSV FILE
    df = pd.read_csv(uploaded_file)
    st.success("✅ File Uploaded Successfully!")

    # SHOW ONLY 5 TO 6 LINES OF CSV FILE
    st.subheader("🧾 Data Preview")
    st.dataframe(df.head())

    # COLUMN SELECTION
    all_columns = df.columns.tolist()
    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    # Download CSV FILE BUTTON 
    csv = df.to_csv(index=False)
    st.download_button(
    "💾 Download CSV Here",
    csv,
    file_name="filtered_data.csv",
    mime="text/csv"
)

    # CHART SETTING
    with st.expander("⚙️ Chart Settings & Generate Chart"):
        chart_type = st.radio("📊 Choose Chart Type" , ["📘 Bar Chart" , "🥧 Pie Chart" , "📈 Line Chart" , "📉 Scatter Plot" , "🌡️ Heatmap" , "🔥 Histogram" , "📦 Box Plot" , "🌊 Area Chart" , "🎻 Violin Plot"])

        # SELECTBOX FOR X AND Y AXIS
        x_axis = st.selectbox("🔻 Select X-axis (category):" , all_columns)
        y_axis = st.selectbox("🔺 Select Y-axis (numeric):" , numeric_cols)

        # CHART DISPLAY
        # BAR CHART
        if chart_type == "📘 Bar Chart":
            st.subheader("📘 Bar Chart")
            fig = px.bar(df , x = x_axis , y = y_axis , color = x_axis) 
            st.plotly_chart(fig , use_container_width = True)

        # PIE CHART
        elif chart_type == "🥧 Pie Chart":
            st.subheader("🥧 Pie Chart")
            fig = px.pie(df , names = x_axis , values = y_axis , title = f"{y_axis} by {x_axis}")
            st.plotly_chart(fig , use_container_width = True)

        # LINE CHART
        elif chart_type == "📈 Line Chart":
            st.subheader("📈 Line Chart")
            fig = px.line(df, x=x_axis, y=y_axis)
            st.plotly_chart(fig, use_container_width=True)

        # SCATTER PLOT
        elif chart_type == "📉 Scatter Plot":
            st.subheader("📉 Scatter Plot")
            fig = px.scatter(df, x=x_axis, y=y_axis)
            st.plotly_chart(fig, use_container_width=True)
    
        # HISTOGRAM PLOT
        elif chart_type == "🔥 Histogram":
            st.subheader("🔥 Histogram")
            fig = px.histogram(df, x=y_axis, nbins=20)
            st.plotly_chart(fig, use_container_width=True)

        # HEATMAP CHART
        elif chart_type == "🌡️ Heatmap":
            st.subheader("🌡️ Heatmap")
            corr = df.corr(numeric_only=True)
            fig = px.imshow(
            corr,
            text_auto=True,
            color_continuous_scale="RdBu",
            title="Correlation Matrix"
        )
            st.plotly_chart(fig, use_container_width=True)

        # BOX PLOT
        elif chart_type == "📦 Box Plot":
            st.subheader("📦 Box Plot")
            fig = px.box(df, x=x_axis, y=y_axis, color=x_axis)
            st.plotly_chart(fig, use_container_width=True)

        # AREA CHART
        elif chart_type == "🌊 Area Chart":
            st.subheader("🌊 Area Chart")
            fig = px.area(df, x=x_axis, y=y_axis, color=x_axis)
            st.plotly_chart(fig, use_container_width=True)

        # VIOLIN PLOT
        elif chart_type == "🎻 Violin Plot":
            st.subheader("🎻 Violin Plot")
            fig = px.violin(df, y=y_axis, x=x_axis, color=x_axis, box=True, points="all")
            st.plotly_chart(fig, use_container_width=True)
    
        # Download Button
        html_bytes = fig.to_html().encode("utf-8")
        st.download_button(
        label="💾 Download Chart Here",
        data=html_bytes,
        file_name="chart.html",
        mime="text/html"
        )
else:
    st.info("📥 Upload A CSV File To Begin")


