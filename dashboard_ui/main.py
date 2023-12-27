#import libraries
import streamlit as st # ui
import pandas as pd  # analysis
import numpy as np # numerical analysis
import plotly.express as px # interactive graph
#run app
# open cmd (ctrl + j) in vs code
# run these comands:
#.........cd folder_name
#.........streamlit run main.py

#load dataset
def load_data():
    df = pd.read_csv('data/pokemon.csv', index_col=0)
    return df

#add ui elements
st.set_page_config(
    layout= "wide",
    page_title="Pokemon Analysis Dashboard",
    page_icon="👻"
)
st.title('pokemon Analysis Dashboard')
st.subheader('Gotta Catch Them All')
with st.spinner("Loading data..."):
    df = load_data()
    st.success("pokemon Dataset Loaded!")

c1, c2, c3 = st.columns(3)
c1.header("Raw Dataset")
c1.dataframe(df)
c2.header("statictical summary")
c2.dataframe(df.describe())
c2.info("Display the statistical summary of the numerical data in database")
c3.header("columns")
c3.write(", ".join(df.columns.tolist()))
#make interactive graph
c1,c2,c3, = st.columns(3)
c1.image('images\pokemon.jpg', use_column_width=True)
df_type_1 =df['Type_1'].value_counts()
c2.dataframe(df_type_1,use_container_width=True)

fig=px.pie(df_type_1,values=df_type_1.values,
           names=df_type_1.index,title='pokemon type')
c3.plotly_chart(fig,use_container_width=True)

# scaller plot
num_cols = df.select_dtypes(include=np.number).columns.tolist()
cat_cols = df.select_dtypes(exclude=np.number).columns.tolist()
c1,c2 = st.columns(2)
c1.header("2D scatter plot")
c1.subheader("select X and Y to plot")
x = c1.selectbox("x", num_cols, key='scatterr1')
y = c1.selectbox("y", num_cols, key='scatterr2')
color = c1.selectbox("color", cat_cols, key='scatterr3')
fig = px.scatter(df,x=x, y=y, color=color)
c1.plotly_chart(fig,use_container_width=True)

c2.header("Trivariate plot")
c2.subheader("selectx,yand z to plot")
x= c2.selectbox("x",num_cols, key ='scatter3d_1')
y = c2.selectbox("y",num_cols, key='scatter3d_2')
z = c2.selectbox("z",num_cols, key='scatter3d_3')
fig = px.scatter_3d(df,x=x, y=y, z=z,)
c2.plotly_chart(fig,use_container_width=True)