# 직원 리스트 데이터
employees = [
    {"name": "Alice", "department": "Engineering", "age": 30, "salary": 85000},
    {"name": "Bob", "department": "Marketing", "age": 25, "salary": 60000},
    {"name": "Charlie", "department": "Engineering", "age": 35, "salary": 95000},
    {"name": "David", "department": "HR", "age": 45, "salary": 70000},
    {"name": "Eve", "department": "Engineering", "age": 28, "salary": 78000}
]

# 문제 1: 부서가 "Engineering"이고 salary >= 80000인 직원들의 이름만 리스트로 출력
eng_high_salary = [emp["name"] for emp in employees if emp["department"] == "Engineering" and emp["salary"] >= 80000]
print("문제 1:", eng_high_salary)

# 문제 2: 30세 이상 직원의 이름과 부서를 튜플(name, department) 형태로 리스트 출력
over_30 = [(emp["name"], emp["department"]) for emp in employees if emp["age"] >= 30]
print("문제 2:", over_30)

# 문제 3: 급여 기준으로 직원 리스트를 salary 내림차순 정렬 후, 상위 3명의 이름과 급여 출력
sorted_by_salary = sorted(employees, key=lambda x: x["salary"], reverse=True)
top3 = [(emp["name"], emp["salary"]) for emp in sorted_by_salary[:3]]
print("문제 3:", top3)

# 문제 4: 모든 부서별 평균 급여 출력
from collections import defaultdict

dept_salaries = defaultdict(list)
for emp in employees:
    dept_salaries[emp["department"]].append(emp["salary"])

dept_avg_salary = {dept: sum(salaries) / len(salaries) for dept, salaries in dept_salaries.items()}
print("문제 4:", dept_avg_salary)