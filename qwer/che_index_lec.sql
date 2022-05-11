SELECT	ic.index_name, ic.column_name,
ic.column_position col_pos,ix.uniqueness
FROM	user_indexes ix, user_ind_columns ic
WHERE	ic.index_name = ix.index_name
AND	ic.table_name = 'lecturer';
