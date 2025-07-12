from faker import Faker
import pandas as pd
import numpy as np
import streamlit as st




def generate_fake_data(clean_df, fraction=0.3):
    faker = Faker()
    num_fake = int(len(clean_df) * fraction)

    fake_data = []

    for _ in range(num_fake):
        fake_data.append({
            'brand': faker.company(),
            'name': faker.word(),
            'label': np.random.choice(clean_df.get('label', ['Unknown'])),
            'price': round(np.random.uniform(5, 100), 2),
            'rank': round(np.random.uniform(2, 5), 1),
            'ingredients': faker.words(nb=5)
        })

    df_fake = pd.DataFrame(fake_data)
    return df_fake
