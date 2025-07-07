# SmartMatch-Resource-Allocation-Bot
AI-powered smart resource allocation bot for matching employees to projects using embeddings and contextual intelligence.

---

## 🚀 Overview

Manual resource allocation is time-consuming, error-prone, and often overlooks key employee and project attributes. This solution leverages AI and Snowflake Cortex embeddings to intelligently match employees to the right projects based on skills, experience, preferences, and more.

---

## ⚙️ How It Works

1. **Data Preparation**
   - Two tables: `PROJECT` and `EMPLOYEE` contain relevant metadata.
   - Embeddings generated using `SNOWFLAKE.CORTEX.EMBED_TEXT_768`.

2. **Matching Logic**
   - Cosine similarity between project and employee embeddings.

3. **Streamlit Dashboard**
   - Select a project
   - View ranked employee recommendations

---

## 📦 Tech Stack

- 🧠 **Snowflake Cortex** for embeddings
- 🐍 **Python** for backend logic
- 🌐 **Streamlit** for interactive UI
- ❄️ **Snowflake SQL** for data querying and processing

---

## ⚙️ Getting started

Run below files in sequence
1. project.sql
2. employee.sql
3. project_embeddings.sql
4. employee_embeddings.sql
5. StreamlitUI.py
     
---

## 📌 Future Enhancements

- Recommend training or new hiring if no match is found.
- Add intelligent allocation logic that holistically considers experience, project complexity, team size, and employee performance to drive more effective and strategic resource assignments.
- Natural Language Interface for RM: Use conversational agents:  “Show me top 5 available backend developers for Bangalore with good project ratings.”
- Feedback Loop from Project Closure.

---

## 🏁 Conclusion

This project demonstrates a scalable, AI-driven approach to optimize workforce allocation. By automating complex decision-making, it reduces bench time, improves project delivery, and empowers resource managers with actionable insights.


