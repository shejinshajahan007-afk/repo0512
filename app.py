import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Title
st.title("Olympic Games")
st.write("Data Analysis")

# Video
st.video("https://www.youtube.com/watch?v=rBnJS9pYr58")

# Load dataset
df = pd.read_csv("data.csv")

# Display dataset
st.dataframe(df)

# Sidebar Navigation
st.sidebar.title("Navigation Window")
st.sidebar.write("Explore different sections")

page = st.sidebar.radio(
    "Choose the visual you want:",
    [
        "Medal Count by Country",
        "Performance by Gender",
        "Medal Trend Over Time",
        "Top Medalist",
        "Most Popular Sports",
        "Funfacts"
    ]
)

# Sidebar Filters
st.sidebar.title("Filters")

selected_year = st.sidebar.slider(
    "Select year range",
    min_value=int(df["Year"].min()),
    max_value=int(df["Year"].max()),
    value=(int(df["Year"].min()), int(df["Year"].max()))
)

selected_gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["Sex"].unique(),
    default=df["Sex"].unique()
)

selected_medal = st.sidebar.multiselect(
    "Select Medal",
    options=df["Medal"].unique(),
    default=df["Medal"].unique()
)

selected_country = st.sidebar.multiselect(
    "Select Country",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)

selected_sport = st.sidebar.multiselect(
    "Select Sport",
    options=df["Sport"].unique(),
    default=df["Sport"].unique()
)

# Apply filters
df = df[
    (df["Sex"].isin(selected_gender)) &
    (df["Medal"].isin(selected_medal)) &
    (df["Country"].isin(selected_country)) &
    (df["Sport"].isin(selected_sport)) &
    (df["Year"] >= selected_year[0]) &
    (df["Year"] <= selected_year[1])
]

# Medal Count by Country
if page == "Medal Count by Country":

    st.subheader("Medal Count by Country")

    medal_count = (
        df[df["Medal"] != "No medal"]
        .groupby("Country")["Medal"]
        .count()
        .sort_values(ascending=False)
    )

    fig = px.bar(
        medal_count,
        x=medal_count.index,
        y="Medal",
        labels={
            "x": "Country",
            "y": "Medal Count"
        }
    )

    st.plotly_chart(fig)


# Performance by Gender
elif page == "Performance by Gender":

    st.subheader("Performance by Gender")

    gender_medal_count = (
        df[df["Medal"] != "No medal"]
        .groupby("Sex")["Medal"]
        .count()
    )

    fig2 = px.pie(
        gender_medal_count,
        names=gender_medal_count.index,
        values="Medal"
    )

    st.plotly_chart(fig2)


# Medal Trend Over Time
elif page == "Medal Trend Over Time":

    st.subheader("Medal Trend Over Time")

    trend = (
        df[df["Medal"] != "No medal"]
        .groupby("Year")["Medal"]
        .count()
    )

    fig3 = px.line(
        trend,
        x=trend.index,
        y="Medal",
        labels={
            "x": "Year",
            "y": "Medal Count"
        }
    )

    st.plotly_chart(fig3)


# Top Medalist
elif page == "Top Medalist":

    st.subheader("Top Medalist")

    top_medalist = (
        df[df["Medal"] != "No medal"]
        .groupby("Name")["Medal"]
        .count()
        .sort_values(ascending=False)
        .head(10)
    )

    fig4 = px.bar(
        top_medalist,
        x=top_medalist.index,
        y="Medal",
        labels={
            "x": "Athlete",
            "y": "Medal Count"
        }
    )

    st.plotly_chart(fig4)


# Most Popular Sports
elif page == "Most Popular Sports":

    st.subheader("Most Popular Sports")

    sport_count = (
        df.groupby("Sport")["Event"]
        .count()
        .sort_values(ascending=False)
    )

    fig5 = px.bar(
        sport_count,
        x=sport_count.values,
        y=sport_count.index,
        orientation="h",
        labels={
            "x": "Event Count",
            "y": "Sport"
        }
    )

    st.plotly_chart(fig5)


# Fun Facts
elif page == "Funfacts":

    st.subheader("Fun Facts")

    st.write("Tug of War was one of the Olympic events.")
    st.write("Tug of War first appeared in the Olympics in 1900.")