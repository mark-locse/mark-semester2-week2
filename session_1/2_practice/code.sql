-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 library.db
-- 2. Load this script: .read code.sql
-- 3. Exit SQLite: .exit


-- write your sql code here

-- 1 --
select b.title, m.name, l.loan_date from books b, members m, loans l
where b.id=l.book_id and l.member_id=m.id;

-- 2 --
select b.title, l.loan_date 
from books b left join loans l on l.book_id = b.id;

-- 3 --
select lb.name, b.title
from librarybranch lb left join books b on lb.id = b.branch_id;

-- 4 --
select lb.name, count(b.id)
from librarybranch lb left join books b on lb.id = b.branch_id
group by lb.name;

-- 5 --
select lb.name, count(b.id)
from librarybranch lb left join books b on lb.id = b.branch_id
group by lb.name having count(b.id)>7;

-- 6 --
select m.name, count(l.id)
from members m left join loans l on m.id=l.member_id
group by m.name;

-- 7 --
select m.name, count(l.id)
from members m left join loans l on m.id=l.member_id
group by m.name having count(l.id)=0;

-- 8 --
select lb.name, count(l.id)
from librarybranch lb, books b left join loans l on lb.id=b.branch_id and b.id=l.book_id
group by lb.name;

-- 9 --
select m.name, count(l.id)
from members m inner join loans l on m.id=l.member_id
group by m.name having count(l.id)>=1;

-- 10 --
select b.title, l.loan_date,
case when l.id is null then 'Unloaned book' else 'Loaned Book' end as Status
from books b left join loans l on b.id=l.book_id;
