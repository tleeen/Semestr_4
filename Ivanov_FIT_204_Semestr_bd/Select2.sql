select kos.title
from Kind_of_sport kos inner join Kinds_sportsman ks
on kos.id = ks.Kind_of_sport_id
group by kos.title
having count(ks.id) =
(select max(count(ks.id))
from Kind_of_sport kos inner join Kinds_sportsman ks
on kos.id = ks.Kind_of_sport_id 
group by kos.id);