# TP complémentaire Orange / KNIME

Le dataset conforme au sujet est généré par `donnees.py` : 5 000 transactions et 568 fraudes.

## Préparation

```powershell
python donnees.py
```

Le workflow Orange est fourni dans `workflows\fraude-orange.ows`. Après installation
d’Orange, ouvrir ce fichier, vérifier le chemin du CSV, exécuter Test and Score puis
exporter le Gradient Boosting avec Save Model vers `models\fraude-gb.pkcls`.

Le workflow KNIME est fourni dans `workflows\tp-fraude.knwf`. La version persistée
contient le lecteur CSV et le learner de régression logistique ; les autres branches
doivent être ajoutées et exécutées dans KNIME 5.12 avant remise finale.

## Vérification locale

```powershell
python run_models.py
```

Cette commande reproduit le protocole 75/25 stratifié et vérifie les modèles de référence.
