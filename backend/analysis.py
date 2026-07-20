import os
import shutil
import uuid
import pandas as pd

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

CURRENT_FILE = None


def save_uploaded_file(file):
    global CURRENT_FILE

    filename = str(uuid.uuid4()) + ".csv"
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    CURRENT_FILE = file_path

    return file_path


def load_data():
    global CURRENT_FILE

    if CURRENT_FILE is None:
        raise Exception("No CSV file uploaded yet.")

    return pd.read_csv(CURRENT_FILE)


def import_csv(file_path):
    df = pd.read_csv(file_path)

    return {
        "success": True,
        "rows": len(df),
        "columns": list(df.columns),
        "preview": df.head(10).to_dict(orient="records")
    }


def get_columns():
    df = load_data()
    return list(df.columns)


def get_preview():
    df = load_data()
    return df.head(10).to_dict(orient="records")


def get_summary():
    df = load_data()
    return df.describe(include="all").fillna("").to_dict()


def get_missing_values():
    df = load_data()
    return df.isnull().sum().to_dict()


def get_numeric_columns():
    df = load_data()
    return list(df.select_dtypes(include="number").columns)


def get_value_counts(column):
    df = load_data()

    if column not in df.columns:
        return {"error": "Column not found"}

    return df[column].value_counts().to_dict()