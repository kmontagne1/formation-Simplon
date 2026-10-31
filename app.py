import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')
figureByProduct =px.pie(données, values='qte', names='produit', title='quantité vendue par produit')

données["chiffre d'affaires"] = données['prix']*données['qte']
figureCAbyProduct = px.pie(données, values="chiffre d'affaires", names='produit', title='chiffre d affaire par produit')

figure.write_html('ventes-par-region.html')
figureByProduct.write_html('quantite-vendue-par-produit.html')
figureCAbyProduct.write_html('CA-par-produit.html')

print('ventes-par-région.html généré avec succès !')
