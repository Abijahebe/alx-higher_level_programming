-- lists all genres of a show in the db

SELECT tg.name
FROM tv_shows AS ts
	INNER JOIN tv_shows_genres AS tsg
		ON ts.id = tsg.show_id
	INNER JOIN tv_genres AS tg
		ON tg.id = tsg.genre_id
where ts.title = "Dexter"
ORDER BY tg.name;
