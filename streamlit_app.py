import streamlit as st
import snowflake.connector
import pandas as pd


# Write directly to the app
st.title("Active Staff Training Counts")
st.write(
    """Counts
    """
)

conn = snowflake.connector.connect(
        user='DEPUTYUSER',
        password='wm$4Zh62',
        account='dfzqycb-tz75056',
        warehouse='COMPUTE_WH',
        database='DEPUTY',
        schema='FACT')

cursor = conn.cursor()

query = '''
select * from mod_commission
qualify cycle_num = max(cycle_num) over()
order by total_commission desc;
'''

cursor.execute(query)
result = cursor.fetchall()

df = pd.DataFrame(result,
                      columns=['MoD', 'Cycle', 'Commission Type', 'Total Sales', 'Total Commission']).sort_values(by='Total Commission')

# Create a simple bar chart
# See docs.streamlit.io for more types of charts
st.subheader("MoD Commission")
st.bar_chart(data=df, x="MoD", y = "Total Commission")

st.subheader("Underlying data")
st.dataframe(df, use_container_width=True)