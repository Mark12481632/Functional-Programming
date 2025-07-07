# #########################################################
# The program that implements the solution to the problem.
#
# Using typing and FP principles.
# #########################################################

import pandas as pd
from collections import defaultdict
from typing import DefaultDict
from typing import NamedTuple
from typing import Iterator
from functools import reduce
from types import MappingProxyType

# Use "NamedTuple" to create imutable structures:
class Employee(NamedTuple):
    id: str
    name: str
    dept: str
    status: str
    salary: int

def read_employee_data(emp_location: str) -> Iterator[Employee]:
    """
    This function creates an iterator that lazily loads the
    data from the given input file.
    Each entry in the iterator is an Employee object.
    """
    def create_employee(id: str, name: str, dept: str, status: str, salary: int) -> Employee:
        return Employee(id, name, dept, status, salary)

    df = pd.read_csv(emp_location)
    return (create_employee(int(df.iloc[inx]["employee_id"]),
                            df.iloc[inx]["name"],
                            df.iloc[inx]["department"],
                            df.iloc[inx]["status"],
                            int(df.iloc[inx]["salary"])) for inx in range(len(df)))


def is_active_employee(emp: Employee) -> bool:
    """
    Returns if employee is cuurently being payed (=> not retired)
    """
    return emp.status != "Retired"


def accumulate_salary_by_dept(acc: DefaultDict[str, int], emp: Employee) -> DefaultDict[str, int]:
    """
    Accummulates the salaries by dept.
    """
    acc[emp.dept] += emp.salary
    acc['Total'] += emp.salary
    return acc


def calculate_department_salaries(active_emp_itr: Iterator[Employee]) -> MappingProxyType:
    """
    Takes the active employees and accummulates salary by department (and Total).
    """
    dept_salary = MappingProxyType(reduce(accumulate_salary_by_dept, active_emp_itr, defaultdict(int)))
    return dept_salary


def display_results(dept_salary: DefaultDict[str, int]) -> None:
    """
    Display results of salary aggregation.
    """
    print("=====================================")
    print("Current Salary Bill by Department:")
    for dept in dept_salary.keys():
        if dept != 'Total':
            print(f"Dept:{dept:<20}  Salaries: ${dept_salary[dept]:<12}")
    print(f"Total Salary Bill: ${dept_salary['Total']}")
    print("=====================================")


def main():
    display_results(
        calculate_department_salaries(
            filter(is_active_employee,
                   read_employee_data("Sample_Employee_Data.csv")
                   )
        )
    )


if __name__ == "__main__":
    main()
