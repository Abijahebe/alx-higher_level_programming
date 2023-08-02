
$.get('https://swapi.co/api/films?format=json', function (body) {
	for (let movie of body['results']) {
		$('UL#list_movies').append('<li>' + movie['title'] + '</li>');
	}
});
