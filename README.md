# Projet IA Ambiance

Ce projet utilise Python pour récupérer les titres et extraits des nouvelles des sites de grands médias français,
analyse le sentiment de chaque titre et donne une note par média.

## Configuration

1. Assurez-vous d'avoir Python 3.6 ou plus récent ainsi que `pip` installé.
   ```bash
    python --version
    pip --version
   ```
   sinon, installez-le :
   ```bash
    sudo apt install python3 python3-pip
    ```

2. Assurez-vous aussi d'avoir le modèle `llama2` installé.
   ```bash
   ollama pull llama2
   ```

3. Installez les dépendances nécessaires :

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