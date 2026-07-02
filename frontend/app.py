import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/analyze"

st.set_page_config(
    page_title="PropertyIntelAI",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 PropertyIntelAI")
st.subheader("AI Property Listing Quality & SEO Analyzer")

st.write(
    "Paste a real estate listing below. The app compares it against a structured real estate knowledge base and uses AI to generate quality, SEO, and improvement recommendations."
)

listing_text = st.text_area(
    "Property Listing",
    height=220,
    placeholder="Example: Beautiful 3 bedroom home in Ames with updated kitchen and large backyard."
)

if st.button("Analyze Listing"):
    if not listing_text.strip():
        st.warning("Please enter a property listing.")
    else:
        with st.spinner("Analyzing listing..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"listing_text": listing_text}
                )

                if response.status_code == 200:
                    result = response.json()

                    st.success("Analysis completed.")

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.metric("Quality Score", result.get("quality_score", "N/A"))

                    with col2:
                        st.metric("SEO Score", result.get("seo_score", "N/A"))

                    with col3:
                        st.metric("Completeness Score", result.get("completeness_score", "N/A"))

                    st.divider()

                    st.subheader("Missing Fields")
                    missing_fields = result.get("missing_fields", [])
                    if missing_fields:
                        for field in missing_fields:
                            st.write(f"- {field}")
                    else:
                        st.success("No major missing fields detected.")

                    st.subheader("AI Explanation")
                    explanations = result.get("explanation", [])
                    if explanations:
                        for item in explanations:
                            st.write(f"- {item}")
                    else:
                        st.write("No explanation available.")

                    st.subheader("Recommended SEO Keywords")
                    keywords = result.get("seo_keywords", [])
                    if keywords:
                        st.write(", ".join(keywords))
                    else:
                        st.write("No SEO keywords returned.")

                    st.subheader("Improvement Suggestions")
                    suggestions = result.get("improvement_suggestions", [])
                    if suggestions:
                        for suggestion in suggestions:
                            st.write(f"- {suggestion}")
                    else:
                        st.write("No suggestions returned.")

                    st.subheader("Improved SEO-Friendly Listing")
                    st.write(result.get("improved_listing", "No improved listing generated."))

                else:
                    st.error("API request failed. Make sure FastAPI is running.")

            except requests.exceptions.ConnectionError:
                st.error("Could not connect to FastAPI. Start the backend first.")
