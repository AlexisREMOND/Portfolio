from pathlib import Path
import streamlit as st
from PIL import Image
import os

# streamlit run app.py

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_Alexis_REMOND.pdf"
profile_pic = current_dir / "assets" / "Alexis.png"
video_path_1 = r"C:\Users\alexl\PycharmProjects\pythonProject\test\Data_Science\Portfolio\assets\Projet_Perso\Droide.mp4"
video_path_2 = r"C:\Users\alexl\PycharmProjects\pythonProject\test\Data_Science\Portfolio\assets\Projet_Perso\projet_perso_3.mp4"


PAGE_TITLE = "Portfolio | Alexis REMOND"
PAGE_ICON = ":film_projector:"
NAME = "Alexis REMOND"
DESCRIPTION ="""
Bienvenue sur mon Portfolio."""

EMAIL = "remond.alexis@yahoo.com"
SOCIAL_MEDIA = {
    "Linkedin" : "https://www.linkedin.com/in/alexis-remond-021818206/",
    "Github" : "https://github.com/AlexisREMOND"
}

CERTIFICATS = {
    "MACHINE LEARNING IN PYTHON WITH SCIKIT-LEARN" : "https://openbadgepassport.com/app/badge/info/520881"
}

projet_ecole_1 = current_dir / "assets" / "Projet_Ecole" / "projet_coureur.png"
projet_ecole_2 = current_dir / "assets" / "Projet_Ecole" / "projet_ecole_2.png"
projet_ecole_3 = current_dir / "assets" / "Projet_Ecole" / "projet_ecole_3.png"
projet_ecole_4 = current_dir / "assets" / "Projet_Ecole" / "projet_4.png"
projet_ecole_5 = current_dir / "assets" / "Projet_Ecole" / "projet_5.png"
projet_ecole_6 = current_dir / "assets" / "Projet_Ecole" / "projet_6.png"
projet_ecole_7 = current_dir / "assets" / "Projet_Ecole" / "projet_7.png"
projet_reseau = r"C:\Users\alexl\PycharmProjects\pythonProject\test\Data_Science\Portfolio\assets\Projet_Ecole\Featuring_musique.html"
projet_ecole_8 = current_dir / "assets" / "Projet_Ecole" / "projet_8.png"

projet_perso_1 = current_dir / "assets" / "Projet_Perso" / "Perso_2.png"
projet_perso_2 = current_dir / "assets" / "Projet_Perso" / "projet_perso_4.png"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}<style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file :
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Télécharger CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📩", EMAIL)

    st.write("#")
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")

st.write("#")
st.sidebar.header("Menu")
selected_option = st.sidebar.selectbox("Choisir une section", ["Formations", "Expériences", "Projets", "Certificats"])

if selected_option == "Formations":
    st.header("🎓 Formations")
    st.write("---")
    st.subheader("🚧 Master DATA & INTELLIGENCE ARTIFICIELLE | Alternance")
    st.write("2023-2025")
    st.write("Université catholique de Lille | Lille, FR")
    st.write("---")
    st.subheader("✅ Bachelor Développement et Data | Alternance")
    st.write("2022-2023")
    st.write("EFREI | Villejuif, FR")
    st.write("---")
    st.subheader("✅ DUT Statistique et informatique Décisionnelle")
    st.write("2020-2022")
    st.write("IUT Paris Rives-De-SEINE | Paris, FR ")

elif selected_option == "Expériences":
    st.header("💻 Expériences")
    st.write("---")
    st.subheader("📊 Data Engineer | Yper | Contrat en alternance")
    st.write(" sept 2023 - Actuellement")
    st.write(
        """
    - • Analyse et présentation des données d'entreprise pour une communication en interne et avec les clients
    - • Détection d'objet 
    - • Classification de texte
    - • Modèle de Prédiction
        """
    )

    st.write("---")
    st.subheader("🚗 Data Analyst | Renault Group (via Expleo) | Contrat en alternance")
    st.write("mai 2023 - septembre 2023")
    st.write(
        """
    - • Création de diagramme UML 
    - • Mise à jour de la documentation 
    - • Création de listes pour améliorer les requêtes
    - • Création de requêtes
        """
    )

    st.write("---")
    st.subheader("🛜 Developpeur Data | Expleo | Contrat en alternance")
    st.write("janvier 2023 - mai 2023")
    st.write(
        """
    - • Création d'une application web pour le suivi des projets R&D en interne
        """
    )

    st.write("---")
    st.subheader("🔎 Ingénieur Data | Expleo | Contrat en alternance")
    st.write("septembre 2022 - janvier 2023")
    st.write(
        """
    - • Durant un projet R&D sur The Future of Hospitals, je travaillais sur la traduction de questions complexes en langage naturel vers un langage SPARQL
        """
    )

    st.write("---")
    st.subheader("📋 Ingénieur Data Scientist | Expleo | Stage")
    st.write("mars 2022 - juin 2022")
    st.write(
        """
    - • Évaluation des data drift en appliquant des méthodes de monitoring sur les données d’un modèle NLP 
        """
    )
    st.write("---")

elif selected_option == "Projets":
    st.header("💼 Projets")
    st.write("---")

    projet_type = st.sidebar.selectbox("Type de projet", ["Perso", "Ecole"])

    if projet_type == "Perso":
        st.subheader("🖱️ Souris d'ordinateur controlée par les yeux | mars 2024 ")
        st.video(video_path_2)
        st.write("Durant ce projet, nous pouvons contrôler la souris en fonction de notre regard, et cliquer grâce à un clin d'oeil")
        st.write("---")

        st.subheader("🤖 Chatbot | janvier 2024 ")
        st.image(str(projet_perso_1), width=700)
        st.write("Ce projet consiste à créer un chatbot avec lequel on peut interagir. Pour l'instant, il ne connait que les informations générales sur les célébrités")
        st.write("---")

        st.subheader("📈 Différents Notebooks | janvier 2023 - Actuellement ")
        st.image(str(projet_perso_2), width=700)
        st.write("Suivi de Notebook, trouvé sur Linkedin, Kaggle, dans différents domaines")
        st.write("---")

        st.subheader("🦾 Droïde | octobre 2023 ")
        st.video(video_path_1)
        st.write("---")

    elif projet_type == "Ecole":
        st.subheader("🎸 Social Network Analysis - Featuring dans la musique | mars 2024 - avril 2024")
        st.image(str(projet_ecole_8), width=700)
        def download_html():
            with open(projet_reseau, "r", encoding="utf-8") as file:
                html_content = file.read()
            return html_content

        html_content = download_html()
        st.download_button(label="Télécharger le projet en HTML", data=html_content, file_name="Featuring_musique.html", mime="text/html", key="download_button")

        st.write("Ce projet a été réalisé sur Rstudio, le but était de trouver les artistes influençant le plus les autres artistes en raison de leur forte de présence dans les featurings. Nous avons donc fait une analyse de données ainsi qu'une analyse de réseau. Je vous laisse télécharger le fichier html pour plus de détails :)")
        st.write("---")

        st.subheader("🥐 Projet Jaamsim | novembre 2023 - janvier 2024")
        st.image(str(projet_ecole_4), width=700)
        st.image(str(projet_ecole_5), width=700)
        st.image(str(projet_ecole_6), width=700)
        st.image(str(projet_ecole_7), width=700)
        st.write("Durant ce projet, réalisé sur Jaamsim, logiciel de simulation, nous avons réalisé le schéma de la préparation d'un gâteau, de l'oeuf à la farine, du mélange des ingrédients, de la cuisson ainsi que le sucrage et l'envoi vers la boutique. Un EDA de nos données a été effectué par la suite.")
        st.write("---")

        st.subheader("👟 Developpement d'une application mobile | octobre 2022 - fevrier 2023")
        st.image(str(projet_ecole_3), width=300, use_column_width=True)
        st.write("Cette application développée sur Android Studio est inspirée de Stockx, célèbre site internet permettant d’acheter mais aussi vendre des vêtements, chaussures, accessoires de collection. Celle-ci se concentre plus particulièrement au monde de la chaussure. Nous pouvons nous inscrire avec nos informations avant de pouvoir accéder à la page de recherche.")
        st.write("---")

        st.subheader("📻 Projet sur les résultats d'un sondage Médiamétrie | octobre 2021 - mars 2022")
        st.write("Récupération des résultats des auditeurs d'un sondage de Médiamétrie sur Excel. Création de variables et analyse des résultats sur SAS. Conception de graphique sur Rstudio. Première visualisation des résultats sur un Powerpoint, et seconde visualisation des résultats sur RShinny.")
        st.write("---")

        st.subheader("🏃 Projet sur les performances des coureurs du marathon de Berlin de 2001 à 2010 | février 2021 - juin 2021")
        st.image(str(projet_ecole_1), width=700)
        st.write("---")

        st.subheader("🎓 Enquête sur la vie sociale et affective des étudiants pendant la crise du coronavirus | octobre 2020 - janvier 2021")
        st.image(str(projet_ecole_2), width=700)
        st.write("---")


elif selected_option == "Certificats":
    st.header("📜 Certificats")
    st.write("---")
    for certificat, link in CERTIFICATS.items():
        st.write(f'[{certificat}]({link})')
