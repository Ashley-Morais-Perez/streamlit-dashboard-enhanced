# 507-streamlit-demo

Link to Streamlit 🎓: https://app-dashboard-enhanced-nmljtzascwigx2cf7dodqf.streamlit.app/ 


## Dashboard Explanation 

I've provided screenshots of what the dashboard looks like below. I decided to explore learning modality in terms of its general distribution across school districts in the U.S. and how it compares to different states. The first thing I changed in the code was implementing a widget. I found a Python code on one of the Streamlit sites and used that template to create a sidebar to filter out states and learning modalities. I also included a 'color theme' (which was in the suggested template) but didn't notice any difference in the dashboard.

I have three figures on the dashboard: a donut chart, bar graph, and a table. I added another requirement file called plotly.express to create the donut chart. 

1) The donut chart shows the learning modality distribution across all reported school districts. You can click on the legend and filter out each learning modality, which will change the chart's distribution. 
2) The bar graph shows each state that reported in-person learning. The measurement in this case was the number of students in each state that had been reported to be in a school district with in-person learning. The darker the bar graph, the higher the state had in-person learning.
3) The data table uses the filters on the sidebar to view whatever data you'd like

Overall, this was an interesting experience setting up a dashboard and exploring other ways to showcase data. I used the virtual environment in GitHub Codespaces to connect to Streamlit. Interestingly, I wasn't able to connect the first time following the steps from the class. However, once I copied the dashboard.py file into Streamlit and connected to GitHub via the Streamlit editing button, I had no issue going back and forth between my virtual environment and Streamlit to view my work.

<img width="944" alt="image" src="https://github.com/user-attachments/assets/98c230d2-8010-46b6-83fe-d4a69fab27c5">

<img width="896" alt="image" src="https://github.com/user-attachments/assets/02a7e627-21ec-4279-9a21-3a3dc0be5c1f">

<img width="854" alt="image" src="https://github.com/user-attachments/assets/147f33bd-9b6c-4dec-a02e-98d4e6d18e82">

