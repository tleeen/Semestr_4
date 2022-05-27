select kof.title, count(ks.id)
from Kind_of_sport kof inner join Kinds_sportsman ks
on kof.id = ks.Kind_of_sport_id
group by kof.title;