select t.last_name, count(r.place_in_the_competition)
from Trainer t inner join Trainer_staff ts
on t.id = ts.Trainer_id
inner join Sportsman sp
on ts.id = sp.Trainer_staff_id
inner join Rewarding r
on sp.id = r.Sportsman_id
where r.place_in_the_competition in (1, 2, 3)
group by t.last_name
ORDER BY count(r.place_in_the_competition) desc;