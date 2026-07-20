from fastapi import APIRouter, UploadFile, File
from analysis import (
    save_uploaded_file,
    import_csv,
    get_columns,
    get_preview,
    get_summary,
    get_missing_values,
    get_numeric_columns,
    get_value_counts
)

router = APIRouter()


@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    path = save_uploaded_file(file)
    return import_csv(path)


@router.get("/columns")
def columns():
    return get_columns()


@router.get("/preview")
def preview():
    return get_preview()


@router.get("/summary")
def summary():
    return get_summary()


@router.get("/missing-values")
def missing_values():
    return get_missing_values()


@router.get("/numeric-columns")
def numeric_columns():
    return get_numeric_columns()


@router.get("/value-count/{column}")
def value_count(column: str):
    return get_value_counts(column)