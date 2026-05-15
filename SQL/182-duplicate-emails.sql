-- LeetCode 182: Duplicate Emails
-- Topics: SQL, GROUP BY, HAVING

-- Problem Description:
-- Find all duplicate emails from the Person table.
--
-- The email field is guaranteed to be NOT NULL.
--
-- Return all emails that appear more than once.

-- Approach:
-- - Group rows by email
-- - Count occurrences of each email
-- - Use HAVING to filter groups with count > 1

-- Time Complexity:
-- O(n)

-- Space Complexity:
-- O(n) in worst case for grouping

SELECT email FROM Person GROUP BY email HAVING COUNT(email) > 1;
