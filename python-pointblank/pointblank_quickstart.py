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
            label="Quickstart validation",
        )
        .col_vals_between(columns="d", left=0, right=5000)
        .col_vals_in_set(columns="f", set=["low", "mid", "high"])
        .col_vals_not_null(columns="c")
        .interrogate()
    )

    print("Validation summary:\n")
    for step in validation.validation_info:
        print(
            f"{step.assertion_type:>20}  "
            f"passed={step.n_passed:>2}  "
            f"failed={step.n_failed:>2}"
        )

    print(
        "\nRun this same object in a notebook to see the interactive report."
    )


if __name__ == "__main__":
    main()
