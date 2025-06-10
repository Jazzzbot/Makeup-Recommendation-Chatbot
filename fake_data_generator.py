from faker import Faker
import pandas as pd
import numpy as np

def generate_fake_data(clean_df, fraction=0.3):
    faker = Faker()
    num_fake = int(len(clean_df) * fraction)

    fake_data = []

    for _ in range(num_fake):
        fake_data.append({
            'Brand': faker.company(),
            'Name': faker.word(),
            'Label': np.random.choice(clean_df['Label'].dropna().unique()),
            'Price': round(np.random.uniform(5, 100), 2),
            'Rank': round(np.random.uniform(2, 5), 1),
            'Ingredients': faker.words(nb=5)
        })

    df_fake = pd.DataFrame(fake_data)
    return df_fake
