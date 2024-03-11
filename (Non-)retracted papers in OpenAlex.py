#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def categorize_titles(input_file):
    df = pd.read_csv(input_file)

    categories = {
        "Notice of Retraction": [],
        "Retracted": [],
        "Withdrawn": [],
        "Removed": [],
        "Temporary Removal": [],
        "Others": []  
    }

    for title in df['display_name']:
        if isinstance(title, float):  
            continue
        found_category = False
        for category in categories.keys():
            if category.lower() in str(title).lower():
                categories[category].append(title)
                found_category = True
                break
        if not found_category:
            categories["Others"].append(title)

    return categories

def plot_bar_graph(categories):
    custom_order = ["Retracted", "Notice of Retraction", "Withdrawn", "Removed", "Temporary Removal", "Others"]
    sorted_categories = [(key, categories[key]) for key in custom_order]

    labels = [x[0] for x in sorted_categories]
    counts = [len(x[1]) for x in sorted_categories]

    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.bar(labels, counts, color='skyblue')

    for rect in bars:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  
                    textcoords="offset points",
                    ha='center', va='bottom')

    ax.set_xlabel('Categories')
    ax.set_ylabel('Number of Publications')
    ax.set_title('Publications by Category')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    
    ax.grid(axis='y', linestyle='--')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    input_file = "Downloads/works-2024-03-11T16-37-37.csv"
    categories = categorize_titles(input_file)
    plot_bar_graph(categories)


# In[ ]:




