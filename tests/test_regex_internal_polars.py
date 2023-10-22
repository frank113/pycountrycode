import pytest
from countrycode import countrycode
from custom_strategies import codelist

try:
    import polars as pl
    _has_polars = True
except ImportError:
    _has_polars = False

_regex_internal_skip_reason = "Test requires polars installation"


# Test all country names with iso3c codes are matched exactly once
@pytest.mark.skipif(not _has_polars,
                    reason=_regex_internal_skip_reason)
def test_iso3c_match():
    """
    Skip test for now.
    Returns:

    """
    name = codelist.filter(pl.col("iso3c").is_not_null())
    iso3c_from_name = countrycode(name["country.name.en"], origin='country.name', destination="iso3c")
    assert len(iso3c_from_name) == len(set(iso3c_from_name))


# Test iso3c-to-country.name-to-iso3c is internally consistent
@pytest.mark.skipif(not _has_polars,
                    reason=_regex_internal_skip_reason)
def test_iso3c_consistency():
    tmp = codelist.filter(pl.col("iso3c").is_not_null())
    a = countrycode(tmp["iso3c"], origin='iso3c', destination="country.name")
    b = countrycode(a, origin='country.name', destination="iso3c")
    assert (b == tmp["iso3c"]).all()


# Test English regex vs. cldr.short.
@pytest.mark.skipif(not _has_polars,
                    reason=_regex_internal_skip_reason)
def test_english_regex():
    tmp = codelist.filter(pl.col("country.name.en").is_not_null())
    tmp = tmp.with_columns(
        test=countrycode(tmp["country.name.en"], origin="country.name.en", destination="cldr.short.en")
    )
    assert (tmp["test"] != tmp["cldr.short.en"]).any() == False


# Test Italian regex vs. cldr.short.it
@pytest.mark.skipif(not _has_polars,
                    reason=_regex_internal_skip_reason)
def test_italian_regex():
    tmp = codelist.filter(pl.col("country.name.it").is_not_null())
    tmp = tmp.with_columns(
        test=countrycode(tmp["country.name.it"], origin="country.name.it", destination="cldr.short.it")
    )
    assert (tmp["test"] != tmp["cldr.short.it"]).any() == False


# Test German regex vs. cldr.short.de
@pytest.mark.skipif(not _has_polars,
                    reason=_regex_internal_skip_reason)
def test_german_regex():
    tmp = codelist.filter(pl.col("country.name.de").is_not_null())
    tmp = tmp.with_columns(
        test=countrycode(tmp["country.name.de"], origin="country.name.de", destination="cldr.short.de")
    )
    assert (tmp["test"] != tmp["cldr.short.de"]).any() == False


# Test French regex vs. cldr.short.fr
@pytest.mark.skipif(not _has_polars,
                    reason=_regex_internal_skip_reason)
def test_french_regex():
    tmp = codelist.filter(pl.col("country.name.fr").is_not_null())
    tmp = tmp.with_columns(
        test=countrycode(tmp["country.name.fr"], origin="country.name.fr", destination="cldr.short.fr")
    )
    assert (tmp["test"] != tmp["cldr.short.fr"]).any() == False