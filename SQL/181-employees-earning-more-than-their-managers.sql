-- LeetCode 181: Employees Earning More Than Their Managers
-- Topics: SQL, Self Join

-- Problem Description:
-- Find the employees whose salary is greater than their manager's salary.
--
-- Return the employee names.

-- Approach:
-- - Use a self join on the Employee table.
-- - Treat:
--     e1 → manager
--     e2 → employee
--
-- - Match:
--     manager.id = employee.managerId
--
-- - Compare salaries:
--     employee.salary > manager.salary

-- Time Complexity:
-- O(n)

-- Space Complexity:
-- O(1) extra space (excluding query processing)

SELECT e2.name AS Employee
FROM Employee e1
JOIN Employee e2
ON e1.id = e2.managerId
WHERE e2.salary > e1.salary;
