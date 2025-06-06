import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Introduction ---
st.title("AI-Powered Marketing with Free WiFi Analytics")
st.write("""
This showcase demonstrates how Artificial Intelligence can be leveraged by data scientists to improve marketing strategies using data from free WiFi analytics in various physical locations.
We'll explore examples from a general perspective and then delve into more specific scenarios with a Nigerian Restaurant and a Supermarket.
""")

# --- 2. Data from Free WiFi Analytics ---
st.subheader("2. Data from Free WiFi Analytics")
st.write("""
Free WiFi analytics can provide valuable insights into customer behavior in physical spaces. This includes:
- Visit frequency (new vs. returning visitors).
- Visit duration.
- Foot traffic within the venue.
- Dwell time in specific zones.
- Path analysis.
- Potentially demographic data (if collected during login) and preferences (if surveys are used).
""")

# --- 3. How AI Enhances Marketing ---
st.subheader("3. How AI Enhances Marketing")
st.write("""
AI techniques can analyze this data to provide deeper insights and enable more effective marketing:
- **Customer Segmentation:** Identifying groups of customers with similar behaviors or preferences.
- **Personalized Promotions:** Delivering targeted offers and recommendations.
- **Optimizing Operations:** Informing decisions about layout, product placement, and staffing.
- **Predictive Analytics:** Forecasting future customer behavior.
- **Automated Campaigns:** Triggering marketing messages based on real-time behavior.
""")

st.markdown("---")

# --- Advanced Use Case: Nigerian Restaurant ---
st.subheader("Advanced Use Case: Nigerian Restaurant")
st.write("Let's consider a Nigerian restaurant with local and continental dishes.")

@st.cache_data
def generate_restaurant_data():
    np.random.seed(42)
    num_restaurant_visitors = 300
    return pd.DataFrame({
        'Visitor ID': range(1, num_restaurant_visitors + 1),
        'Arrival Time': pd.to_datetime(['2025-05-25 10:00:00'] * num_restaurant_visitors) + pd.to_timedelta(np.random.randint(0, 540, num_restaurant_visitors), unit='min'),
        'Duration (minutes)': np.random.randint(15, 90, num_restaurant_visitors),
        'Frequent Visitor': np.random.choice(['Yes', 'No'], num_restaurant_visitors, p=[0.4, 0.6]),
        'Meal Type Preference': np.random.choice(['Local', 'Continental', 'Both'], num_restaurant_visitors, p=[0.4, 0.3, 0.3]),
        'Time of Visit': np.random.choice(['Lunch', 'Dinner', 'Breakfast'], num_restaurant_visitors, p=[0.5, 0.3, 0.2])
    })

restaurant_df = generate_restaurant_data()
st.dataframe(restaurant_df.head())

st.subheader("AI-Driven Segmentation: Restaurant")
st.write("AI clustering can segment customers. Here's a conceptual segmentation:")

def assign_restaurant_segment(row):
    if row['Frequent Visitor'] == 'Yes' and row['Time of Visit'] == 'Lunch' and row['Meal Type Preference'] in ['Local', 'Both']:
        return "Loyal Local Lunch Goers"
    elif row['Time of Visit'] == 'Dinner' and row['Meal Type Preference'] in ['Continental', 'Both']:
        return "Continental Dinner Enthusiasts"
    elif row['Time of Visit'] == 'Breakfast' and row['Frequent Visitor'] == 'Yes':
        return "Regular Breakfast Crowd"
    else:
        return "General Patrons"

restaurant_df['Segment'] = restaurant_df.apply(assign_restaurant_segment, axis=1)
restaurant_segment_counts = restaurant_df['Segment'].value_counts().reset_index()
restaurant_segment_counts.columns = ['Segment', 'Count']

fig_pie_rest = px.pie(restaurant_segment_counts, names='Segment', values='Count', title='Restaurant Customer Segments')
st.plotly_chart(fig_pie_rest, use_container_width=True)

# --- Visualization: Meal Preferences ---
meal_preference_counts = restaurant_df['Meal Type Preference'].value_counts().reset_index()
meal_preference_counts.columns = ['Meal Type', 'Count']
fig_bar_meal = px.bar(meal_preference_counts, x='Meal Type', y='Count', title='Restaurant Meal Type Preferences')
st.plotly_chart(fig_bar_meal, use_container_width=True)

# --- Matplotlib Example ---
st.subheader("Meal Duration Distribution")
fig, ax = plt.subplots()
sns.histplot(restaurant_df['Duration (minutes)'], ax=ax)
st.pyplot(fig)

st.subheader("5. Privacy Considerations")
st.warning("""
Remember, ethical data handling is crucial. Real-world applications must prioritize:
- Anonymization of user data.
- Transparency about data collection.
- Compliance with privacy regulations.
""")

st.write("This showcase illustrates how AI can be a powerful tool for data scientists to enhance marketing using free WiFi analytics.")
