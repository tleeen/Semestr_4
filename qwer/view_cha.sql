CREATE VIEW CHA_VU
AS SELECT c.name , count(l.last_name) "COUNT"
FROM	chair c, lecturer l
where c.id = l.char_id
group by c.name;