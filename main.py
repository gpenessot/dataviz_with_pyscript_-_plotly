# Importer les bibliothèques
import pandas as pd
import plotly.express as px
import js

# Titres et descriptions
header = """Changement de température mondiale et émissions de CO2"""
subheader = "Évolution de la température mondiale et des émissions de CO2 au cours des derniers siècles"
description = """Le graphique montre l'augmentation de la température année après année.
Les données couvrent les années de 1880 à 2023 et incluent les anomalies de température pour chaque mois de chaque année ainsi que les températures moyennes pour des groupes de mois tels que de juin à août.
Les données sur les émissions de CO2 couvrent une période similaire, et vous pouvez voir une corrélation entre les deux ensembles de données."""
footer = """Dashboard créé avec ❤️, PyScript & Plotly - © Gaël Penessot 2024"""


# Afficher les titres et la description
def display_texts():
    display(header, target="header")
    display(subheader, target="subheader")
    display(description, target="description")
    display(footer, target="footer")


# Créer le graphique des anomalies de température
def create_temperature_chart(df, period):
    fig = px.bar(
        df,
        x="Year",
        y=period,
        color=period,
        title="Évolution des anomalies de température (Juin-Août)",
        color_continuous_scale="inferno",
        template="plotly_white",
        width=600,
        height=400,
    )
    return fig


# Créer le graphique des émissions de CO2
def create_co2_chart(df):
    fig = px.line(
        df,
        x="Year",
        y="Annual CO₂ emissions",
        title="Évolution des émissions annuelles de CO₂",
        line_shape="linear",
        line_dash_sequence=["solid"],  # style de ligne
        color_discrete_sequence=["#8A2BE2"],  # couleur violette
        width=600,
        height=400,
        template="plotly_white",
    )
    return fig


# Exécuter les fonctions
display_texts()

# Charger les données pour le graphique de température
df_temp = pd.read_csv("./globaltemp.csv", skiprows=1)
temperature_chart = create_temperature_chart(df_temp, "JJA")
js.plot(temperature_chart.to_json(), "chart1")

# Charger les données pour le graphique de CO2
df_co2 = pd.read_csv("./hadcrutworld.csv")
co2_chart = create_co2_chart(df_co2)
js.plot(co2_chart.to_json(), "chart2")
