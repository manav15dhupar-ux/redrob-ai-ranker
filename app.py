import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Redrob AI Ranker",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Redrob AI Candidate Ranker")
st.subheader("V9 Candidate Ranking System")

st.markdown("""
This dashboard showcases our final candidate ranking system.

### Features
- Top 100 ranked candidates
- Ranking score
- Candidate reasoning
- Download submission CSV
""")

try:
    df = pd.read_csv("submission.csv")

    st.success(f"Loaded {len(df)} ranked candidates")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Candidates Ranked", len(df))

    with col2:
        st.metric("Top Score", df["score"].max())

    with col3:
        st.metric("Lowest Top-100 Score", df["score"].min())

    st.divider()

    st.subheader("🏆 Top 10 Candidates")

    st.dataframe(
        df.head(10),
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("📋 Top 100 Candidates")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    with open("submission.csv", "rb") as file:
        st.download_button(
            "⬇ Download Submission CSV",
            file,
            file_name="submission.csv",
            mime="text/csv"
        )

except Exception as e:
    st.error(f"Could not load submission.csv\n\n{e}")