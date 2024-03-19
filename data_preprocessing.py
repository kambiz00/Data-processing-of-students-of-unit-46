import pandas as pd


def load_dataset(file_path, file_type='csv'):
    """
        Load the dataset into a Pandas DataFrame.

        Parameters:
        - file_path (str): Path to the dataset file.
        - file_type (str): Type of the dataset file.

        Returns:
        - df (pd.DataFrame): Loaded DataFrame.
    """
    print("Loading dataset...")
    try:
        if file_type == 'csv':
            df = pd.read_csv(file_path)
            return df
        elif file_type == 'xlsx':
            df = pd.read_excel(file_path)
            print("dataset loaded successfully\n")
            return df
    except FileNotFoundError:
        raise "File type not supported or path does not exist"


def explore_data(df):
    """
        Explore the dataset for missing values, outliers, and general statistics.

        Parameters:
        - df (pd.DataFrame): Input DataFrame.

        Returns:
        - None (Prints exploration results).
    """
    print("Exploring Data...")
    print("Dataset Information:")
    print(df.info(), '\n')

    print("\nMissing Values:")
    print(df.isnull().sum(), '\n')

    print("\nSummary Statistics:")
    print(df.describe(), '\n')
    print("Exploration completed successfully")
