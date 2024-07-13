import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # return employees.mul({"name": 1, "salary": 2})

    employees["salary"] *= 2
    return employees
