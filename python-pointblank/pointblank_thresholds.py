# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "pointblank[pl]",
# ]
# ///

import pointblank as pb


def main() -> None:
    validation = (
        pb.Validate(
            data=pb.load_dataset("small_table", tbl_type="polars"),
            tbl_name="small_table",
            label="Threshold-driven validation",
            thresholds=pb.Thresholds(warning=0.05, error=0.10, critical=0.15),
            actions=pb.Actions(
                warning=(
                    "Warning: step {step} reached {level} severity during "
                    "{type}."
                ),
                critical=(
                    "Critical: step {step} reached {level} severity during "
                    "{type}."
                ),
            ),
        )
        .col_vals_between(columns="d", left=0, right=5000)
        .col_vals_not_null(columns="c")
        .rows_distinct()
        .interrogate()
    )

    print("All checks passed perfectly:", validation.all_passed())
    print(
        "Anything above the error threshold:",
        validation.above_threshold(level="error"),
    )

    try:
        validation.assert_below_threshold(level="critical")
    except AssertionError as exc:
        print("CI gate tripped:", exc)


if __name__ == "__main__":
    main()
