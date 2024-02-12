# TODO : - Explore how students perform in different terms.
#        - Visualize the average scores per term. #DONE

import seaborn as sns
import matplotlib.pyplot as plt


def term_performance(df):
    """
        Explore how students perform in different terms and visualize the average scores per term.

        Parameters:
        - df (pd.DataFrame): Input DataFrame.

        Returns:
        - None (Prints term-wise performance visualizations).
    """
    # Visualizations
    plt.figure(figsize=(10, 5))

    # Box plot for term-wise performance
    sns.boxplot(x='TERM', y='SCORE', data=df)
    plt.title('Term-wise Performance')
    plt.xlabel('Term')
    plt.ylabel('Score')

    plt.show()
