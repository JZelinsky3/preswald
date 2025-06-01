from preswald import connect, get_df, query, text, table, plotly
import plotly.express as px
import pandas as pd

connect()
df = get_df("personality_dataset")

text("# Personality Trait Exploration App")

table(df, title="Raw Personality Data")

text("## Social Engagement vs Personality")
fig1 = px.box(df, x="Personality", y="Social_event_attendance", color="Personality", title="Social Event Attendance by Personality Type")
plotly(fig1)

text("## Outdoor Activity Trends")
fig2 = px.histogram(df, x="Going_outside", color="Personality", barmode="overlay", nbins=10, title="Frequency of Going Outside")
plotly(fig2)

text("## Online Activity Patterns")

df["Time_spent_Alone"] = pd.to_numeric(df["Time_spent_Alone"], errors="coerce")
df["Post_frequency"] = pd.to_numeric(df["Post_frequency"], errors="coerce")
df["Friends_circle_size"] = pd.to_numeric(df["Friends_circle_size"], errors="coerce")

df = df.dropna(subset=["Post_frequency", "Friends_circle_size", "Time_spent_Alone"])

fig3 = px.scatter(
    df,
    x="Post_frequency",
    y="Friends_circle_size",
    color="Personality",
    size="Time_spent_Alone",
    title="Social Media vs Friend Circle Size"
)
plotly(fig3)


text("## Fatigue After Socializing")
drain_counts = df.groupby(["Drained_after_socializing", "Personality"]).size().reset_index(name="count")
fig4 = px.bar(drain_counts, x="Drained_after_socializing", y="count", color="Personality", barmode="group", title="Fatigue After Socializing by Personality")
plotly(fig4)

text("## Stage Fear Distribution")
fig5 = px.pie(df, names="Stage_fear", title="Stage Fear Distribution in the Population")
plotly(fig5)
