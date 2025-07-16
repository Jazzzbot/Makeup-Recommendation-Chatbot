Elabada Ararchchige, Sonali, 22301094

Hosseini, Yasaman, 22300310


# Cosmetics Recommender

https://mygit.th-deg.de/se20094/assistance-systems-project

https://mygit.th-deg.de/se20094/assistance-systems-project/-/wikis/home

## Project description

This project is a data-driven web application built with Streamlit and Rasa, aimed at recommending cosmetic products based on user preferences and skin characteristics. It features interactive visualizations, predictive modeling using Scikit-learn, and a chatbot that assists users in finding products suitable to their needs. The application is built according to principles learned in the Assistance Systems course, including GUI design, data handling, and user interaction.

## Installation

To run the project, follow these steps:

1. Clone the repository from MyGit.
2. Ensure you have Python 3.10 installed.
3. Create and activate a virtual environment:

python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
4. Install dependencies:

pip install -r requirements.txt
### Versions used:
- Python 3.10
- Streamlit 1.33
- Rasa 3.6
- scikit-learn 1.4
- pandas 2.2
- matplotlib 3.8

## Data

The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets) and contains product information, prices, skin types, and customer reviews.  
We handled outliers by applying the IQR method to numerical fields like Price and Rating, and smoothed extreme values.  
Fake data (about 35%) was generated using Faker and numpy to simulate realistic user reviews and purchase behavior.  
This was done to increase data variability and robustness of model training.

## Basic Usage

To run the app:

streamlit run app.py
Key features:
- Navigate through the sidebar: Overview, Chatbot, Visualizations, and Recommendations.
- Use filters like skin type, brand, and price to explore data.
- Interact with the chatbot for product suggestions.
- Admin login available for testing purposes:
  - Username: admin
  - Password: admin123

## Implementation of the Requests

1. Multi-page web app using Streamlit tabs and routing.
2. Git repository and wiki created on MyGit.
3. Personas (e.g., College Student, Makeup Enthusiast, Sensitive Skin User) documented in Wiki.
4. 5 use cases defined and documented.
5. requirements.txt used for all dependencies.
6. This README follows the specified structure.
7. venv is used and documented.
8. Dataset from Kaggle, not built-in.
9. CSV import implemented (data/clean.csv).
10. Data analyzed in Streamlit (min, max, median, correlation, distribution).
11. Feature descriptions added to Wiki with statistics.
12. Outliers handled with IQR and visual validation.
13. Feature transformation includes one-hot encoding, scaling, and binning.
14. Fake data added (~35%), with analysis of its influence on model generalization.
15. Widgets: Slider (price), SelectBox (skin type), TextInput (brand).
16. Models used: K-Nearest Neighbors (base), Random Forest, ElasticNet.
17. Chatbot integrated for use cases like product recommendation and skin tips.
18. System persona created ("CosmoBot"), documented in Wiki.
19. Sample dialogs added to Wiki (3 per use case).
20. High-level dialog flow diagrams added to Wiki.
21. Rasa bot included in the repository.
22. Screencast showing app usage and chatbot uploaded to repository.

## Work done

Sonali Elabada Arachchige
- GUI development with Streamlit
- Data visualizations and summary stats
- Personas and chatbot dialogs

Yasaman Hosseini
- Data preprocessing, outlier detection, and fake data generation
- Model training with KNN, Random Forest, ElasticNet
- Dialog flow and Rasa integration

Both
- Wiki documentation
- Project structure, version control, and README
- Testing and video demonstration
