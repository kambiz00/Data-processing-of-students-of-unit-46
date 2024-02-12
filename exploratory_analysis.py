# TODO : - Calculate and visualize basic statistics for the
#         'AGE,' 'SCORE,' and 'TERM' columns. This can include
#          mean, median, mode, and standard deviation. #DONE

# TODO :   - Explore the distribution of genders in the dataset.
#          - Compare the average scores of male and female students using visualizations (e.g., bar chart). #DONE

# TODO :    - Analyze the distribution of students across academic years.
#           - Visualize the average scores of students in each academic year. #DONE

# TODO :    - Use correlation coefficients to examine relationships between variables (e.g., age and score).
#           - Create a heatmap to visualize correlations. #DONE

# TODO :    - Visualize the distribution of scores using a histogram or kernel density plot. #DONE


import matplotlib.pyplot as plt
import seaborn as sns


def descriptive_statistics(df):
    """
        Calculate and visualize basic statistics for the 'AGE,' 'SCORE,' and 'TERM' columns.

        Parameters:
        - df (pd.DataFrame): Input DataFrame.

        Returns:
        - None (Prints descriptive statistics and visualizations).
    """

    print("\nDescriptive Statistics for 'AGE':")
    print(df["AGE"].describe())

    print("\nDescriptive Statistics for 'SCORE':")
    print(df['SCORE'].describe())

    print("\nDescriptive Statistics for 'TERM':")
    print(df['TERM'].describe())

    # Visualize distributions
    plt.figure(figsize=(12, 5))

    # Histogram for 'AGE'
    plt.subplot(1, 3, 1)
    sns.histplot(df['AGE'], kde=True)
    plt.title("Distribution of Age")
    # Histogram for 'SCORE'
    plt.subplot(1, 3, 2)
    sns.histplot(df['SCORE'], kde=True)
    plt.title('Distribution of Score')

    # Histogram for 'TERM'
    plt.subplot(1, 3, 3)
    sns.countplot(x='TERM', data=df)
    plt.title('Term-wise Distribution')

    plt.tight_layout()
    plt.show()


def gender_analysis(df):
    """
        Explore the distribution of genders and compare the average scores of male and female students.

        Parameters:
        - df (pd.DataFrame): Input DataFrame.

        Returns:
        - None (Prints gender distribution and visualizations).
    """
    gender_counts = df['GENDER'].value_counts()
    print("\nGender Distribution:")
    print(gender_counts)

    average_scores = df.groupby('GENDER')['SCORE'].mean()
    print("\nAverage Scores by Gender:")
    print(average_scores)

    # Visualizations
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    sns.countplot(x='GENDER', data=df)
    plt.title('Gender Distribution')

    plt.subplot(1, 2, 2)
    sns.barplot(x='GENDER', y='SCORE', data=df)
    plt.title('Average Scores by Gender')

    plt.tight_layout()
    plt.show()


def academic_year_analysis(df):
    """
        Analyze the distribution of students across academic years and visualize the average scores.

        Parameters:
        - df (pd.DataFrame): Input DataFrame.

        Returns:
        - None (Prints academic year distribution and visualizations).
    """
    academic_year_counts = df['ACADEMIC YEAR'].value_counts()
    print("\nAcademic Year Distribution:")
    print(academic_year_counts)

    average_scores = df.groupby('ACADEMIC YEAR')['SCORE'].mean()
    print("\nAverage Scores by Academic Year:")
    print(average_scores)

    # Visualizations
    plt.figure(figsize=(12, 5))

    # Bar chart for academic year distribution
    plt.subplot(1, 2, 1)
    sns.countplot(x='ACADEMIC YEAR', data=df)
    plt.title('Academic Year Distribution')

    # Bar chart for average scores by academic year
    plt.subplot(1, 2, 2)
    sns.barplot(x='ACADEMIC YEAR', y='SCORE', data=df)
    plt.title('Average Scores by Academic Year')

    plt.tight_layout()
    plt.show()


def correlation_analysis(df):
    """
    Use correlation coefficients to examine relationships between numeric variables and create a heatmap.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.

    Returns:
    - None (Prints correlation matrix and heatmap).
    """
    # Select numeric columns for correlation analysis
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

    # Calculate correlation matrix
    correlation_matrix = df[numeric_columns].corr()

    # Print correlation matrix
    print("\nCorrelation Matrix:")
    print(correlation_matrix)

    # Visualize correlation matrix using a heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.show()


def score_distribution(df):
    """
        Visualize the distribution of scores using a histogram or kernel density plot.

        Parameters:
        - df (pd.DataFrame): Input DataFrame.

        Returns:
        - None (Prints score distribution visualizations).
    """

    # Visualizations
    plt.figure(figsize=(12, 5))

    # Histogram for score distribution
    plt.subplot(1, 3, 2)
    sns.histplot(df['SCORE'], kde=True)
    plt.title('Score Distribution (Histogram)')
    plt.xlabel('Score')
    plt.ylabel('Frequency')

    # Kernel density plot for score distribution
    plt.subplot(1, 3, 3)
    sns.kdeplot(df['SCORE'], fill=True)
    plt.title('Score Distribution (Kernel Density Plot)')
    plt.xlabel('Score')
    plt.ylabel('Density')

    plt.tight_layout()
    plt.show()
