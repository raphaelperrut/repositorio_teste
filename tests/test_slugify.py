"""Tests for the slugify helper."""

from geospatial_etl.normalization import slugify


def test_slugify_removes_accents_and_diacritics() -> None:
    assert slugify("áçãé") == "acae"
    assert slugify("São Paulo") == "sao-paulo"


def test_slugify_replaces_spaces_with_hyphens() -> None:
    assert slugify("hello world") == "hello-world"
    assert slugify("hello    world") == "hello-world"


def test_slugify_normalizes_mixed_case() -> None:
    assert slugify("GeoData ETL Pipeline") == "geodata-etl-pipeline"


def test_slugify_handles_special_characters() -> None:
    assert slugify("Olá, Mundo! (2024)") == "ola-mundo-2024"
    assert slugify("  --Já_Valeu--  ") == "ja-valeu"
