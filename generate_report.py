from pathlib import Path

from docx import Document
from docx.shared import Inches, Pt


ROOT = Path(__file__).parent
REPORT = ROOT / "rapport_tp_complementaire.docx"

document = Document()
document.add_heading("TP complémentaire : Orange puis KNIME", 0)
document.add_paragraph("Détection de fraude bancaire - compte rendu")
document.add_paragraph("Nom : Othmane Boushabi\nFilière : À compléter\nGroupe : À compléter\nDate : 14/11/2026")

document.add_heading("1. Données et protocole", 1)
document.add_paragraph(
    "Le jeu de données est généré avec la graine 7 et contient 5 000 transactions, "
    "dont 568 fraudes. La cible fraude est binaire et déséquilibrée. Orange et KNIME "
    "utilisent un partage stratifié 75 % / 25 %, avec une graine fixe 42."
)

document.add_heading("2. Workflow Orange", 1)
document.add_paragraph(
    "File -> Data Sampler -> Test and Score. La cible fraude est réglée en categorical "
    "target. Cinq learners sont comparés : Logistic Regression, kNN, Tree, Random Forest "
    "et Gradient Boosting. Le kNN reçoit ensuite Preprocess -> Normalize Features. "
    "La forêt utilise 100 arbres et l'entraînement reproductible."
)
table = document.add_table(rows=1, cols=3)
table.style = "Table Grid"
for cell, text in zip(table.rows[0].cells, ["Modèle", "F1 avant", "F1 après"]):
    cell.text = text
for row in [
    ("Logistic Regression", "0.781", "0.781"),
    ("kNN", "0.478 attendu", "0.780 attendu"),
    ("Tree", "0.756", "0.756"),
    ("Random Forest", "0.813 attendu", "0.833 attendu"),
    ("Gradient Boosting", "0.837", "0.837"),
]:
    cells = table.add_row().cells
    for cell, text in zip(cells, row):
        cell.text = text
document.add_paragraph(
    "La matrice attendue du Gradient Boosting est : vrais négatifs 1093, fausses alertes 15, "
    "fraudes manquées 29, fraudes détectées 113. Le modèle est enregistré sous "
    "models/fraude-gb.pkcls et le workflow sous workflows/fraude-orange.ows."
)
document.add_paragraph(
    "État de vérification : les scores Python et la matrice Python sont exécutés et vérifiés. "
    "Les scores Orange indiqués ci-dessus sont ceux du sujet et doivent être confirmés après "
    "ouverture du workflow dans Orange. Le fichier pkcls doit être exporté par Orange."
)

document.add_heading("3. Workflow KNIME", 1)
document.add_paragraph(
    "CSV Reader -> Number to String (fraude) -> Table Partitioner. La sortie apprentissage "
    "alimente Logistic Regression Learner, Random Forest Learner et Gradient Boosted Trees "
    "Learner. Chaque modèle est relié à son Predictor, puis à un Scorer. Le Scorer compare "
    "fraude et Prediction (fraude), et la ligne de classe 1 fournit le F-measure."
)
document.add_paragraph(
    "Contrôles attendus : 3 750 lignes d'apprentissage, 1 250 lignes de test, 426 fraudes "
    "dans l'apprentissage et 142 dans le test. Le workflow est exporté sous workflows/tp-fraude.knwf."
)

document.add_heading("4. Réponses aux questions", 1)
answers = [
    ("Question 1 - Exactitude ou F1 ?", "L'exactitude est trompeuse avec une classe minoritaire : prédire presque toujours 0 donne déjà un score élevé. Le F1 combine précision et rappel de la classe fraude. Le kNN dépend des distances ; la normalisation empêche montant de dominer les autres variables."),
    ("Question 2 - Reproductibilité", "Sans graine fixe, la forêt peut changer entre deux exécutions, ce qui empêche de reproduire un résultat ou d'expliquer une régression. Orange propose Replicable training, KNIME Use static random seed et scikit-learn/FLAML utilisent random_state ou seed=42."),
    ("Question 3 - Coût des erreurs", "Une fraude manquée coûte généralement plus cher qu'une fausse alerte, mais le choix dépend du métier. Le seuil de décision permet de déplacer l'équilibre entre rappel et précision."),
    ("Question 4 - La cible", "KNIME traite une colonne entière comme numérique ; Number to String la transforme en catégorie. Dans Orange, on règle fraude sur categorical et target dans File. Sans cette étape, on obtient une régression ou aucun F1."),
    ("Question 5 - Deux environnements", "Orange recalcule automatiquement le graphe, tandis que KNIME exige l'exécution des nœuds et indique leur état par des feux. Orange est immédiat pour débuter ; KNIME sépare mieux les étapes Learner/Predictor et convient davantage aux flux d'équipe."),
    ("Question 6 - FLAML", "FLAML reste utile pour explorer automatiquement plusieurs familles et hyperparamètres. Les outils visuels sont utiles pour comprendre et communiquer un pipeline. Pour la production, fraude-gb.pkcls devrait être complété par un contrat de données, un seuil documenté, des tests, une API, la traçabilité, le monitoring, la gestion des biais et un plan de réentraînement."),
]
for title, answer in answers:
    document.add_heading(title, 2)
    document.add_paragraph(answer)

document.add_heading("5. Captures et livrables", 1)
document.add_paragraph(
    "Captures à joindre : Test and Score après amélioration, matrice de confusion Gradient Boosting, "
    "workflow Orange, workflow KNIME exécuté, vue Confusion Matrix et Accuracy statistics. "
    "Les fichiers .ows, .knwf et .pkcls doivent être exportés depuis les applications correspondantes."
)

document.save(REPORT)
print(REPORT)
