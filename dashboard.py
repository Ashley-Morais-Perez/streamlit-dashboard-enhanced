import streamlit as st
import pandas as pd
import plotly.express as px

st.header("School Learning Modalities Dashboard")
st.text("The 2020-2021 School Learning Modalities dataset provides weekly estimates of learning modalities for U.S. K-12 public and independent charter school districts during the 2020-2021 school year. In this Streamlit dashboard, we will focus on the distribution of learning modalities among school districts, with an emphasis on the states that had the highest levels of in-person instruction.")

## https://healthdata.gov/National/School-Learning-Modalities-2020-2021/a8v3-a3m3/about_data
df = pd.read_csv("https://healthdata.gov/resource/a8v3-a3m3.csv?$limit=50000") ## first 1k 

# Data cleaning
df['week_recoded'] = pd.to_datetime(df['week'])
df['zip_code'] = df['zip_code'].astype(str)

# Sidebar Configuration
with st.sidebar:
    st.title('🎓 School Modalities Filters')
    
    # State Selector
    state_list = sorted(df['state'].unique())
    selected_states = st.multiselect('Select States', state_list, default=state_list)
    
    # Learning Modalities Selector
    modality_list = sorted(df['learning_modality'].unique())
    selected_modalities = st.multiselect('Select Learning Modalities', modality_list, default=modality_list)

    #Color Theme
    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)

# Apply Filters
filtered_df = df[
    (df['state'].isin(selected_states)) &
    (df['learning_modality'].isin(selected_modalities))
]

# Donut Chart Data
modality_counts = filtered_df['learning_modality'].value_counts().reset_index()
modality_counts.columns = ['Learning Modality', 'Count']

# Donut Chart Visualization
colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA']  # Assign custom colors for each modality
fig = px.pie(
    modality_counts,
    values='Count',
    names='Learning Modality',
    color='Learning Modality',
    color_discrete_sequence=colors,
    hole=0.5,
    title="Learning Modality Distribution"
)

# Display Chart and Description
st.plotly_chart(fig, use_container_width=True)
st.caption("The distribution of learning modalities in school districts across the US.")
st.text("According to the chart, only 24% of school districts during the 2020-2021 school year were remote. 41.2% of school districts were hybrid, offering a combination of in-person and remote learning either to the entire district or only to a subset of students. Additionally, 34.8% of school districts chose to remain open and provide in-person instruction.")

# Bar Chart: In-Person Learning by State
in_person_data = (
    filtered_df[filtered_df['learning_modality'] == "In Person"]
    .groupby('state', as_index=False)['student_count']
    .sum()
    .sort_values(by='student_count', ascending=False)
)


bar_fig = px.bar(
    in_person_data,
    x='state',
    y='student_count',
    title="In-Person Learning by State",
    labels={'state': 'State', 'student_count': 'Number of Students'},
    color='student_count',
    color_continuous_scale='Blues'
)

# Display Bar Chart
st.plotly_chart(bar_fig, use_container_width=True)
st.caption("States that continued with in-person learning during 2020-2021")
st.text("The bar chart displays the states that continued in-person learning during the 2020-2021 school year. While many states ordered school closures, others allowed districts to decide whether to close or remain open. As shown in the previous graph, about 35% of school districts continued with in-person learning. Based on the bar graph, Texas appears to have the most school districts that opted for in-person learning.")


# Table of the Filtered Data
st.subheader("Data Table")
st.text("Explore the full dataset by using the filters on the sidebar.")
st.dataframe(filtered_df, use_container_width=True)
