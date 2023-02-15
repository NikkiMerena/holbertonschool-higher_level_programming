-- Script that lists all shows and genres linked to that show from database hbtn_0d_tvshows
SELECT tv_shows.title, tv_genres.name
    FROM tv_shows
    LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
    LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
    ORDER BY title, name;
