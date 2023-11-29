import pandas as pd
import plotly_express as px
import streamlit as st

# Lendo a base de dados
df = pd.read_csv("acidentes2022.csv", on_bad_lines="skip", sep=';')

df["vitimasfatais"] = df["vitimasfatais"].str.replace(",", ".").astype(float)
df["vitimas"] = df["vitimas"].str.replace(",", ".").astype(float)

clima = df["tempo_clima"].value_counts().sort_values(ascending=False)

bairro = df["bairro"].value_counts().head(10).sort_values(ascending=True)

# alterando coluna de data para datetime
df["data"] = pd.to_datetime(df["data"])

# criando coluna de mês
df["Mês_Acidente"] = df["data"].dt.month

#total_mes = df["Mês_Acidente"].value_counts().reset_index()
#total_mes = total_mes.sort_values(by='index')

def main():
    st.header("Relatório Acidentes de Trânsito em Recife - 2022")

    total_acidentes = df.shape[0]
    total_com_vitimas = df['vitimas'].sum()
    total_vitimas_fatais = df["vitimasfatais"].sum()    

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Acidentes 🚦", int(total_acidentes))
    col2.metric("Total Vítimas 🚨", int(total_com_vitimas))
    col3.metric("Total Vítimas Fatais 🪦", int(total_vitimas_fatais))

    fig = px.bar(clima, text=clima.values, color_discrete_sequence=["#FF4500"])
    fig.update_layout(title="Total de acidentes por Clima", title_x=0.1,showlegend=False)
    st.plotly_chart(fig)
    
    fig1 = px.bar(bairro, text=bairro.values,
             color_discrete_sequence=["#FF4500"], orientation="h")
    fig1.update_layout(title="Top 10 acidentes por Bairro", title_x=0.1,showlegend=False)
    st.plotly_chart(fig1)

    #fig2 = px.line(total_mes, x="index", y="Mês_Acidente",
    #          color_discrete_sequence=["#FF4500"], markers=True,
    #          labels={"index":"Mês Acidente", "Mês_Acidente":"Total Acidentes"})
    #fig2.update_layout(title='Total de acidentes por mês', title_x=0.5)
    #fig2.update_traces(textposition='top center')
    #st.plotly_chart(fig2)



if __name__ == "__main__":
    main()
    