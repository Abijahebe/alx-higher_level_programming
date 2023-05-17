-- creates the table id_not_null on the server

CREATE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256)
);
