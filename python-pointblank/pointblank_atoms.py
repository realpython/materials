# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "pointblank[pl]",
# ]
# ///

import polars as pl
import pointblank as pb

VALID_ELEMENTS = {"Cu", "Pt"}


def main() -> None:
    atoms = pl.read_csv("pointblank_atoms.csv")

    validation = (
        pb.Validate(
            data=atoms,
            tbl_name="atoms_from_parser",
            label="Round-trip validation before re-export",
            thresholds=pb.Thresholds(warning=0.05, error=0.10, critical=0.25),
        )
        .col_vals_in_set(columns="symbol", set=list(VALID_ELEMENTS))
        .col_vals_not_null(columns=["x", "y", "z"])
        .col_vals_between(columns=["x", "y", "z"], left=0, right=20)
        .col_vals_between(columns="fx", left=-1000, right=1000)
        .interrogate()
    )

    clean = validation.get_sundered_data(type="pass")
    dirty = validation.get_sundered_data(type="fail")

    print(f"Safe to re-export: {len(clean)} rows")
    print(f"Needs review:      {len(dirty)} rows\n")
    print(dirty.select(["atom_id", "symbol", "x", "fx"]))


if __name__ == "__main__":
    main()
