import streamlit as st
import pandas as pd
import snowflake.snowpark as snowpark

st.set_page_config(page_title="Project-Employee Matcher", layout="wide")
st.title("🔍 SmartMatch")

# Start Snowpark session
session = snowpark.Session.builder.getOrCreate()

# Get list of project IDs and names
projects_df = session.sql("""
    SELECT PROJECT_ID, PROJECT_NAME FROM RESOURCE_ALLOCATION.SCH.PROJECT_EMBEDDINGS
""").to_pandas()

# Dropdown to select a Project ID
selected_project_id = st.selectbox("Select a PROJECT_ID", projects_df['PROJECT_ID'])

# Fetch and show full project details
project_details_df = session.sql(f"""
    SELECT 
        PROJECT_ID,
        PROJECT_NAME,
        SKILLS_REQUIRED,
        DURATION_MONTHS,
        START_DATE,
        COMPLEXITY,
        DOMAIN,
        LOCATION,
        TEAM_SIZE,
        PREFERRED_EXPERIENCE
    FROM RESOURCE_ALLOCATION.SCH.PROJECT
    WHERE PROJECT_ID = {selected_project_id}
""").to_pandas()

project = project_details_df.iloc[0]

with st.expander(f"📁 {project['PROJECT_NAME']}"):
    st.markdown(f"""
    **🧠 SKILLS REQUIRED:** {project['SKILLS_REQUIRED']}  
    **🏷️ DOMAIN:** {project['DOMAIN']}  
    **⚙️ COMPLEXITY:** {project['COMPLEXITY']}  
    **📍 LOCATION:** {project['LOCATION']}  
    **📅 START DATE:** {project['START_DATE']}  
    **⏳ DURATION (Months):** {project['DURATION_MONTHS']}  
    **👥 TEAM SIZE:** {project['TEAM_SIZE']}  
    **📈 PREFERRED EXPERIENCE (Years):** {project['PREFERRED_EXPERIENCE']}  
    """)


# Compute similarity directly using VECTOR_COSINE_SIMILARITY
query = f"""
    SELECT 
    e.EMPLOYEE_ID,
    e.EMPLOYEE_NAME,
    VECTOR_COSINE_SIMILARITY(p.PROJECT_EMBEDDING, e.EMPLOYEE_EMBEDDING) AS SIMILARITY_SCORE,
    emp.SKILLS,
    emp.CURRENT_PROJECT_END,
    emp.PREFERRED_DOMAIN,
    emp.PREFERRED_LOCATION,
    emp.PERFORMANCE_RATING,
    emp.EXPERIENCE_YEARS
FROM RESOURCE_ALLOCATION.SCH.PROJECT_EMBEDDINGS p
JOIN RESOURCE_ALLOCATION.SCH.EMPLOYEE_EMBEDDINGS e
  ON TRUE
JOIN RESOURCE_ALLOCATION.SCH.EMPLOYEE emp
  ON emp.EMPLOYEE_ID = e.EMPLOYEE_ID
WHERE p.PROJECT_ID = {selected_project_id}
AND emp.CURRENT_PROJECT_END <= DATE('{project['START_DATE']}')
ORDER BY SIMILARITY_SCORE DESC
LIMIT 5
"""

matches_df = session.sql(query).to_pandas()

# Show results
st.subheader("👥 Top Matching Employees")
st.dataframe(matches_df, use_container_width=True)
