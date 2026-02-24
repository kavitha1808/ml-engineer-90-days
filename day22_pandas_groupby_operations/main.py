from src.employee_analysis import run_employee_analysis
from src.loan_analysis import run_loan_analysis
from src.sales_analysis import run_sales_analysis


def main():
    print("Running Day 22 – GroupBy Projects 🚀")

    run_employee_analysis()
    run_loan_analysis()
    run_sales_analysis()

    print("\nAll Day 22 Projects Completed Successfully!")


if __name__ == "__main__":
    main()
