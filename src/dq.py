
def get_validator(df):
    # import here to prevent the dag import to time out
    import great_expectations as ge

    context = ge.get_context()

    suite_name = "rinde_suite"

    if suite_name not in context.list_expectation_suite_names():
        context.add_expectation_suite(expectation_suite_name=suite_name)

    datasource = context.sources.add_pandas(name="pandas_ds")
    asset = datasource.add_dataframe_asset(name="rinde_asset")

    batch_request = asset.build_batch_request(dataframe=df)

    validator = context.get_validator(
        batch_request=batch_request,
        expectation_suite_name=suite_name
    )

    return validator

def validate_rinde(df):
    validator = get_validator(df)

    validator.expect_column_values_to_be_between(
        "rinde_kg_ha", 0, 15000
    )

    validator.expect_column_values_to_not_be_null("lote_id")

    results = validator.validate()

    if not results.success:
        raise Exception("DQ failed")

    return True