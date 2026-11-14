# Comparatif Orange, KNIME et FLAML

| Approche | Meilleur modele | F1 classe 1 | Jeu de test | Temps humain | Graine fixee ? | Export du modele |
|---|---|---:|---|---|---|---|
| FLAML 60 s (TP04) | XGBoost | 0.7608 | 1 250 lignes, 134 fraudes | faible | seed=42 | MLflow |
| Orange, avant amelioration | Random Forest | 0.813 attendu | 1 250 lignes, 142 fraudes | moyen | oui | `.pkcls` |
| Orange, apres amelioration | Gradient Boosting | 0.837 attendu | 1 250 lignes, 142 fraudes | moyen | oui | `fraude-gb.pkcls` |
| KNIME | Gradient Boosted Trees | a mesurer dans Scorer | 1 250 lignes, 142 fraudes | moyen | seed=42 | `.knwf` |

FLAML est adapté à l’exploration rapide et reproductible sur un poste local. Orange est recommandé
pour l’apprentissage visuel et l’inspection interactive des erreurs. KNIME est plus adapté à une équipe
qui veut assembler des flux séparant clairement apprentissage, prédiction et évaluation. Les résultats
ne doivent pas être comparés au centième près car les protocoles et les tirages peuvent différer.
