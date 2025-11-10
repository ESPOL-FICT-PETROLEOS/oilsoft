import xlwings as xw
from poes.model.poes import poes
import numpy as np
import pandas as pd

# Define Sheet names
SUMMARY = "Summary"
RESULTS = "Results"

# Define Column Names
VARIABLES = "Variables"
VALUES = "Values"
DISTRIBUTION = "Distribution"
LOC = "Loc"
SCALE = "Scale"
C = "c"
LIM_MIN = "Lim min"
LIM_MAX = "Lim max"

# Call cells from Ms Excell
DF_POES = "df_poes"
DET_POES = "det_values"
REALIZATIONS = "realizations"
SEED = "seed"

# Write values in Excel from Python
POES_DET = "det_poes"
POES_PROB = "prob_poes"
POES_ARRAY = "poes_array"

# Index of POES Parameters
AREA_IDX, H_IDX, PORO_IDX, SWI_IDX, BOI_IDX = 0, 1, 2, 3, 4


def main():
    wb = xw.Book.caller()

    # Define sheet
    sheet = wb.sheets[SUMMARY]

    # Call values from Excel
    params = sheet[DET_POES].options(np.array).value

    # Calculate poes from Python to Excel
    sheet[POES_DET].value = poes(*params)


if __name__ == "__main__":
    xw.Book("stoiip.xlsm").set_mock_caller()
    main()
