# ScoLaM : Grands modèles de langage pour la synthèse de propositions législatives

<p align="center">
    <img src="assets/logo.png" width="30%">
</p>
ScoLaM (Scalable Contrastive Learning of Representations for Unsupervised Language and Behavior Modeling) est un modèle d'apprentissage profond innovant conçu pour détecter des signaux faibles sur internet et l'intranet. Ce modèle utilise une approche d'apprentissage contrastif pour apprendre des représentations robustes et informatives à partir de données textuelles et comportementales non étiquetées.

Le projet ScoLaM vise à répondre à la problématique de la gestion des risques et des menaces numériques au sein des organisations. Il représente une avancée technologique significative en proposant une solution permettant de renforcer l'efficacité et la capacité d'adaptation des collaborateurs et des agents de sécurité numérique face à l'augmentation des fraudes numériques et de la désinformation liée à l'accélération et au développement de l'intelligence artificielle.

## Détails du Modèle

- **Développé par:** [TheSchooly](https://www.theschooly.tech) : 
- **Type de modèle:** Un modèle de langue auto-régressif basé sur l'architecture transformers
- **Licence:** Llama 2 Community License Agreement
- **Basé sur le modèle:** [Llama 2](https://arxiv.org/abs/2307.09288)
- **Papier:** [Rapport technique](https://arxiv.org/xxxxxx)

## Installation

### Méthode 1 : Avec pip

```bash
cd FastChat
pip3 install "fschat[model_worker,webui,train]"
```
Cette commande vous permet d'installer FastChat, indispensable pour charger et effectuer une inférence avec notre modèle.

### Méthode 2 : Docker

```bash
docker build -t fastchat:training-latest .
# puis
docker run -it --gpus '"device=0,1"' -v /path/to/model:/path/to/model fastchat:training-latest # with gpu
docker run -it -v /path/to/model:/path/to/model fastchat:training-latest # no gpu
```
Ici, nous construisons une image Docker et exécutons un conteneur. Ce processus nécessite Docker d'installé dans votre système et il est recommandé si vous prévoyez d'utiliser le modèle à grande échelle ou dans un environnement de production. 

Pour installer Docker, vous pouvez consulter la documentation officielle de Docker à l'adresse suivante : [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)


## Commencer avec ScoLaM

Les poids pré-entraînés du modèle LLamadement sont disponibles sur Hugging Face à l'adresse suivante : [ScoLaM-7b](https://huggingface.co/schoolyAI/ScoLaM-7b) et [ScoLaM-13b](https://huggingface.co/schoolyAI/ScoLaM/ScoLaM-13b).   

### Inférence avec l'interface de ligne de commande

```bash
python3.9 -m fastchat.serve.cli --model-path /paht/to/scolam --conv-template alpaca ##--device cpu if no gpu available
```

<p align="left">
    <img src="assets/cli_scolam.png" width="50%">
</p>
Cette commande vous permet de démarrer le modèle et de commencer à l'interroger.

## Re-Entraîner ScoLaM

Les données d'entraînement qui ont servi à apprendre à ScoLaM se trouvent dans ./data/fine_tuning_data_dila_v4.json.
Pour plus d'informations sur la composition du dataset, voir la section 3.3 du [rapport technique](https://arxiv.org/abs/xxxxxxxxx)

Si vous souhaitez ré-entraîner LLaMAndement, voici les étapes à suivre : 

1. Téléchargez llama v2 13b : https://huggingface.co/meta-llama/Llama-2-13b-chat-hf

2. Configurez train_llamandement_13b.sh

3. Lancez un fine tuning

Il est recommandé de lancer le script d'entraînement dans une image Docker pour assurer un environnement de développement cohérent et éviter les problèmes de dépendances. En utilisant une image Docker, vous pouvez encapsuler toutes les dépendances nécessaires, y compris les versions spécifiques des bibliothèques et des frameworks, ce qui facilite la reproductibilité de l'entraînement du modèle.

```bash
sh train_llamandement_13b.sh
```

## Citation
```
@article{bacelyy2024scolam,,
  title={ScoLAM: Large Language Models for  Learning of Representations for Unsupervised Language and Behavior Modeling},
  author={Florent Pasquier,Pascal Jollivet, Bacely Yorobi and others},
  journal={arXiv preprint arXiv:},
  year={2024}
}
```