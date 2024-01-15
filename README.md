# Projet IA Ambiance

Ce projet utilise Python pour récupérer les titres et extraits des nouvelles des sites de grands médias français,
analyse le sentiment de chaque titre et donne une note par média.

## Configuration

1. Assurez-vous d'avoir Python 3.6 ou plus récent ainsi que `pip` installé.
   ```bash
    python --version
    pip --version
   ```
   ⚠️ Suivant votre ordinateur, la commande peut être `python3` au lieu de `python` et `pip3` au lieu de `pip`.

   Si ce n'est pas le cas, installez-les :

   ```bash
    sudo apt install python3 python3-pip
    ```

2. Assurez-vous aussi d'avoir le modèle `llama2` installé ([Ollama](https://ollama.ai/))
   ```bash
   ollama pull llama2
   ```

3. Installez les dépendances nécessaires en vous assurant d'être dans le dossier du projet :

   ```bash
   pip install -r requirements.txt
    ```
   ⚠️ Suivant votre ordinateur, la commande peut être `pip3` au lieu de `pip`.


4. Lancez le script `main.py` en vous assurant d'être dans le dossier du projet :

   ```bash
   python main.py
   ```
   ⚠️ Suivant votre ordinateur, la commande peut être `python3` au lieu de `python`.

♥️ Enjoy!