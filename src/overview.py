import streamlit as st

def render():
    # Top "hero" card
    topCols = st.columns(1)
    with topCols[0]:
        with st.container(border=True):
            st.markdown(
               "<h1 style='text-align: center; margin-bottom: 0; text-transform: uppercase;'>Doncaster Rovers - Season 25/26</h1>",
                unsafe_allow_html=True
            )
            st.markdown(
               "<h3 style='text-align: center; margin-bottom: 0; text-transform: uppercase;'>Analysis Dashboard</h1>",
                unsafe_allow_html=True
            )
            # Add a bit of vertical space
            st.write("")

    # Add a bit of vertical space
    st.write("")

    # Two cards in a row
    middleCols = st.columns(2)

    with middleCols[0]:
        with st.container(border=True):
            st.markdown(
               "<h3 style='margin-bottom: 0; text-transform: uppercase;'>About</h3>",
                unsafe_allow_html=True
            )

            st.markdown(
                """
                This dashboard analyses Doncaster Rovers’
                <span style="color:#00cc44; font-weight:600;">underlying performance</span>
                and compares it with the
                <span style="color:#00cc44; font-weight:600;">results</span> achieved on the pitch. By examining the
                frequency and quality of chances created and conceded, and comparing these measures with goals
                scored and conceded, the dashboard shows whether outcomes reflect underlying performance or diverge
                from it.
                </p>
                """,
                unsafe_allow_html=True
            )
            # Add a bit of vertical space
            st.write("")

    with middleCols[1]:
        with st.container(border=True):
            st.markdown(
               "<h3 style='margin-bottom: 0; text-transform: uppercase;'>Plot Chart Information</h3>",
                unsafe_allow_html=True
            )

            st.markdown(
                """
                Where plot charts are used, they are divided into four quadrants.
                The <span style="color:#00cc44; font-weight:600;">bottom-right</span> generally indicates the
                strongest position, combining positive attacking output with solid defensive performance.
                The <span style="color:#00cc44; font-weight:600;">top-right</span> and
                <span style="color:#00cc44; font-weight:600;">bottom-left</span> can still represent effective
                styles, while the <span style="color:#00cc44; font-weight:600;">top-left</span> typically
                highlights teams struggling at both ends of the pitch.
                </p>
                """,
                unsafe_allow_html=True
            )
            # Add a bit of vertical space
            st.write("")

    # Add a bit of vertical space
    st.write("")

    # Bottom card
    bottomCols = st.columns(1)
    with bottomCols[0]:
        with st.container(border=True):
            st.markdown(
               "<h3 style='margin-bottom: 0; text-transform: uppercase;'>Tab Contents:</h3>",
                unsafe_allow_html=True
            )

            st.markdown(
                """
                - <span style="color:#00cc44; font-weight:800; text-transform: uppercase;">Performance: </span>
                Explore Doncaster Rovers’ underlying performance through the frequency and quality of
                chances created and conceded, revealing attacking and defensive strengths & weaknesses.

                - <span style="color:#00cc44; font-weight:800; text-transform: uppercase;">Outcomes: </span>
                See how goals scored and goals conceded compare with expected
                performance to show where results align with, or diverge from, underlying play.
                """,
                unsafe_allow_html=True
            )

            # Add a bit of vertical space
            st.write("")
