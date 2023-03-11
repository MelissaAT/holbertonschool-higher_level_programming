-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT genres.name
FROM genres
INNER JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY genres.name ASC;