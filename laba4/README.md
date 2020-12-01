### Full data.tsv u can download at  https://datasets.imdbws.com/title.basics.tsv.gz

# Build and run:

* docker build -t films .
* docker run -d -p 5000:5000 films

# Examples of usage (on test data.tsv at this repo):

## GET by id:
* curl -X GET 127.0.0.1:5000/movie_id/tt0000022

<img src="images/1.jpg" height=262 width=709>



## GET by title:
* curl -X GET 127.0.0.1:5000/movie/Carmencita

<img src="images/2.jpg" height=296 width=812>



## GET by year:
* curl -X GET 127.0.0.1:5000/year/1894

<img src="images/3.jpg" height=985 width=624>



## POST with likes (return suggest of topk films):
* curl -d '{
"likes": {
"tt0000001": 1,
"tt0000002": 0,
"tt00000010": 0
}}' -H "Content-Type: application/json" -X POST 127.0.0.1:5000/suggest/5

<img src="images/4.jpg" height=343 width=753>


---


