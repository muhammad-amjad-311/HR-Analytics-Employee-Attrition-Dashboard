# HR Analytics — Employee Attrition Dashboard (Power BI)

An interactive Power BI dashboard built on the IBM HR Analytics Employee Attrition dataset, designed to help HR teams understand **where**, **why**, and **among whom** employee attrition is happening — and where retention efforts should be focused.

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat&logo=powerbi&logoColor=black)
![Status](https://img.shields.io/badge/status-completed-brightgreen)

---

## 📌 Project Overview

Employee attrition (staff turnover) is costly and disruptive for any organization. This dashboard analyzes 1,470 employee records across demographic, job, satisfaction, and compensation factors to surface actionable patterns behind why employees leave.

The project answers three core questions:
1. **Where** is attrition happening? (Department, Job Role, etc.)
2. **Why** is it happening? (Overtime, satisfaction, income, distance from home, etc.)
3. **Who** is most at risk? (Age, tenure, marital status, etc.)

---

## 🗂️ Dataset

- **Source:** IBM HR Analytics Employee Attrition & Performance dataset
- **Rows:** 1,470 employees
- **Columns:** 35 attributes (demographic, job-related, satisfaction, and compensation data)
- No missing values in the raw dataset.

**Data cleaning steps applied:**
- Removed constant/non-informative columns: `EmployeeCount`, `StandardHours`, `Over18`
- Checked for and removed duplicate records
- Retained `EmployeeNumber` as a unique identifier only (excluded from visuals)
- Created binned versions of continuous fields (`Age`, `DistanceFromHome`, `MonthlyIncome`, `YearsAtCompany`) for clearer categorical comparisons
- Applied a filter on `YearsAtCompany` (≤ 20 years) in trend visuals to avoid misleading spikes caused by very small sample sizes at high tenure values

---

## 📊 Dashboard Structure

The report is organized across **2 pages**, each focused on a specific theme:

### Page 1 — Overview
- KPI cards: Total Employees, Attrition Rate, Attrition Count, Total Monthly Income, Average Monthly Income
- Attrition Rate by OverTime
- Attrition Rate by Job Role
- Attrition split (donut) by Attrition status
- Attrition Rate by Monthly Income (bins)
- Attrition Rate by Years at Company (bins)
- Attrition Rate by Department (pie)

### Page 2 — Demographics & Work Factors
- Attrition Rate by Job Satisfaction
- Attrition Rate by Age (bins)
- Attrition Rate by Gender (donut)
- Attrition Rate by Distance From Home (bins)
- Attrition Rate by Business Travel

---

## 🧮 Key DAX Measures

```DAX
Total Employees = COUNTROWS('HR_Analytics')

Attrition Count = 
CALCULATE(COUNTROWS('HR_Analytics'), 'HR_Analytics'[Attrition] = "Yes")

Attrition Rate = 
DIVIDE(
    CALCULATE(COUNTROWS('HR_Analytics'), 'HR_Analytics'[Attrition] = "Yes"),
    COUNTROWS('HR_Analytics'),
    0
)
```

---

## 🔍 Key Insights

**Overall numbers:**
- Total Employees: **1,470**
- Attrition Rate: **16%** (≈ 237 employees)
- Average Monthly Income: **6.50K**

| Factor | Finding |
|---|---|
| **OverTime** | Employees who work overtime have a much higher attrition rate (~30%) compared to those who don't (~10%) — the strongest driver in the dataset |
| **Job Role** | Sales Representatives have the highest attrition rate, followed by Laboratory Technicians |
| **Department** | Sales carries the largest share of attrition among the three departments |
| **Monthly Income** | Lower-income employees (0K–5K bracket) attrite the most; attrition steadily declines as income rises |
| **Years at Company** | Newer employees (0 years tenure) show the highest attrition; the rate drops as tenure increases |
| **Job Satisfaction** | Employees with the lowest satisfaction rating (1) show the highest attrition; attrition drops sharply as satisfaction improves |
| **Age** | Younger employees show the highest attrition rate, declining steadily with age |
| **Distance From Home** | Employees living farther from work (20+ km) attrite at a noticeably higher rate |
| **Business Travel** | Frequent travelers have the highest attrition; non-travelers have the lowest |
| **Gender** | Female (~17%) vs Male (~15%) — a small difference, not a strong driver |

**Executive takeaway:**
> Attrition is highest among employees who work overtime, earn lower salaries, live farther from the office, travel frequently for work, are newer to the company, or report low job satisfaction.

---

## 🛠️ Tools Used

- **Power BI Desktop** — data modeling, DAX measures, and dashboard visuals
- **Power Query** — data cleaning and transformation

---

## 🚀 How to Use

1. Clone or download this repository
2. Open the `.pbix` file in Power BI Desktop
3. Explore each page using the tabs at the bottom of the report
4. Use the filter/slicer panes to drill into specific departments, roles, or demographics

---

## 📁 Repository Contents

```
├── HR_Attrition_Dashboard.pbix    # Power BI dashboard file
├── HR_Analytics_Data.csv          # Source dataset
└── README.md                      # Project documentation
```

---

## 📌 Notes

This project is for educational/portfolio purposes using a publicly available HR dataset. It is not intended as production HR decision-making software.
