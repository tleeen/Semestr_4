CREATE VIEW EMP_VU
AS SELECT	l.id, l.last_name "EMPLOYEE", c.name
FROM	chair c, lecturer l
where c.id = l.char_id;