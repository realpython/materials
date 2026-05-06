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

    report = validation.get_dataframe_report()
    summary = report.select(
        ["step_description", "pass_n", "failed_n"]
    ).iter_rows(named=True)

    print("Validation summary:\n")
    for step in summary:
        print(
            f"{step['step_description']:20}"
            f"passed={step['pass_n']:<4}"
            f"failed={step['failed_n']}"
        )


if __name__ == "__main__":
    main()
