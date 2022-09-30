# 1回目コミットのテスト
import pandas as pd
import streamlit as st

df = pd.DataFrame({'Japanese': [55, 96, 76, 82,67],'Mathmatics': [44, 77, 54, 67, 88],'English': [67, 54, 76, 91, 68]})
st.subheader('テスト結果')
st.dataframe(df)
