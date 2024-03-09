-- Отримати всі завдання певного користувача
select *
from tasks
where user_id = 5;

-- Вибрати завдання за певним статусом
select *
from tasks
where status_id = (select id from status where name = 'IN_PROGRESS')
limit 50;

-- Оновити статус конкретного завдання
update tasks
set status_id = (select id from status where name = 'NEW')
where id = 7;

-- Отримати список користувачів, які не мають жодного завдання
select *
from users
where id not in (select user_id
                 from tasks
                 where user_id is not null);

-- Додати нове завдання для конкретного користувача
insert into tasks (title, description, status_id, user_id)
values ('Test task', 'Test description', 1, 5);

-- Отримати всі завдання, які ще не завершено
select *
from tasks
where status_id in (select id from status where name in ('NEW', 'IN_PROGRESS'));

-- Видалити конкретне завдання
delete
from tasks
where id = 7;

-- Знайти користувачів з певною електронною поштою
select *
from users
where email like '%example.net%';

-- Оновити ім'я користувача
update users
set fullname = 'John Doe'
where id = 5;

-- Отримати кількість завдань для кожного статусу
select status.name, count(tasks.id)
from tasks
         join status on tasks.status_id = status.id
group by status.name;

-- Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти
select tasks.title, users.fullname
from tasks
         join users on tasks.user_id = users.id
where users.email like '%example.com';

-- Отримати список завдань, що не мають опису.
select *
from tasks
where description is null;

-- Вибрати користувачів та їхні завдання, які є у статусі
select users.fullname, tasks.title
from users
         join tasks on users.id = tasks.user_id
where tasks.status_id = (select id from status where name = 'IN_PROGRESS');

-- Отримати користувачів та кількість їхніх завдань
select users.fullname, count(tasks.id)
from users
         left join tasks on users.id = tasks.user_id
group by users.fullname
