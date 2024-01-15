# Projet IA Ambiance

Ce projet utilise Python pour récupérer les titres et extraits des nouvelles des sites de grands médias français,
analyse le sentiment de chaque titre et donne une note par média.

## Configuration

1. Assurez-vous d'avoir Python 3.6 ou plus récent ainsi que `pip` installé.
   ```bash
    python --version
   ```
   ```bash
    pip --version
   ```
   **⚠️ Suivant votre ordinateur, la commande peut être `python3` au lieu de `python` et `pip3` au lieu de `pip`.**

   Si ce n'est pas le cas,
   installez-les ([Python](https://www.python.org/downloads/), [pip](https://pip.pypa.io/en/stable/installation/)).


2. Créez un environnement virtuel et activez-le en vous assurant d'être dans le dossier du projet :
   ```bash
   python -m venv venv
   ```
   ```bash
   source venv/bin/activate
   ```
   **⚠️ Suivant votre ordinateur, la commande peut être `python3` au lieu de `python`.<br />
   ⚠️ Suivant votre ordinateur, la commande peut être `source venv/Scripts/activate` (Windows)
   ou `source venv/bin/activate` (Linux/MacOS).**


3. Assurez-vous aussi d'avoir le modèle `llama2` installé ([Ollama](https://ollama.ai/)) et éxécuté puis tapez la
   commande suivante :
   ```bash
   ollama pull llama2
   ```


4. Installez les dépendances nécessaires en vous assurant d'être dans le dossier du projet :

   ```bash
   pip install -r requirements.txt
    ```
   **⚠️ Suivant votre ordinateur, la commande peut être `pip3` au lieu de `pip`.**


5. Lancez le script `main.py` en vous assurant d'être dans le dossier du projet :

   ```bash
   python main.py
   ```
   **⚠️ Suivant votre ordinateur, la commande peut être `python3` au lieu de `python`.**
