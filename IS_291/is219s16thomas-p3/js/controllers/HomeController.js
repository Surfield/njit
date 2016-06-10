app.controller('HomeController', ['$scope', function($scope) {


	/* THESE ARE YOUR LIST OF MOVIES AND ACCOMPANYING METADATA
	//
	// 	They are in the following format:
	// 	title (String): the name of the movie
	// 	iscore (Number): the IMDB score
	// 	rating (String): the movie's MPAA rating
	// 	released (Date): the release date
	// 	country (String): the country of production
	// 	posters (Array): an array of String values with the URL to movie posters
	// 	imdb (String): the URL to the corresponding IMDB website
	// 	website (String): the URL to the corresponding official website
	// 	likes (Number): a fictitious number of user likes
	// 	dislikes (Number): a fictitious number of user dislikes
	// 	posterindex (Number): a counter to use with the "posters" array to keep track of the current displayed poster index
	//
	// FOR STEP 16, ADD THREE OF YOUR OWN FAVORITE MOVIES WITH METADATA TO THE END OF THIS LIST
	*/
	$scope.movies = [
    {
      title:	'The Shawshank Redemption',
      iscore:	9.3,
      rating:	'R',
      runtime:	142,
      released:	new Date('1994', '10', '14'),
      country:	'USA',
      posters:	['img/shawshank.jpg','img/shawshank2.jpg','img/shawshank3.jpg'],
      imdb:		'http://www.imdb.com/title/tt0111161',
      website:	'https://www.facebook.com/ShawshankRedemptionFilm',
      likes:	1021,
      dislikes:	122,
      posterindex: 0
	},
    {
      title:	'The Godfather',
      iscore:	9.2,
      rating:	'R',
      runtime:	175,
      released:	new Date('1972', '03', '24'),
      country:	'USA',
      posters:	['img/godfather.jpg','img/godfather_2.jpg','img/godfather_3.jpg'],
      imdb:		'http://www.imdb.com/title/tt0068646',
      website:	'https://www.facebook.com/thegodfather',
      likes:	928,
      dislikes:	109,
      posterindex: 0
	},
    {
      title:	'The Godfather: Part II',
      iscore:	9.0,
      rating:	'R',
      runtime:	202,
      released:	new Date('1974', '12', '20'),
      country:	'USA',
      posters:	['img/godfather2.jpg','img/godfather2_2.jpg'],
      imdb:		'http://www.imdb.com/title/tt0071562',
      website:	'https://www.facebook.com/thegodfather',
      likes:	855,
      dislikes:	99,
      posterindex: 0
	},
    {
      title:	'The Dark Knight',
      iscore:	8.9,
      rating:	'PG-13',
      runtime:	152,
      released:	new Date('2008', '07', '18'),
      country:	'USA',
      posters:	['img/darkknight.jpg','img/darkknight2.jpg'],
      imdb:		'http://www.imdb.com/title/tt0468569',
      website:	'http://www.42entertainment.com/work/whysoserious',
      likes:	828,
      dislikes:	127,
      posterindex: 0
	},
    {
      title:	'Schindler\'s List',
      iscore:	8.9,
      rating:	'R',
      runtime:	195,
      released:	new Date('1993', '11', '30'),
      country:	'USA',
      posters:	['img/schindlerslist.jpg'],
      imdb:		'http://www.imdb.com/title/tt0108052',
      website:	'https://www.uphe.com/schindlers-list',
      likes:	812,
      dislikes:	101,
      posterindex: 0
	},
    {
      title:	'Troy',
      iscore:	7.2,
      rating:	'R',
      runtime:	163,
      released:	new Date('2004', '04', '14'),
      country:	'USA',
			posters:	['img/troy1.jpg','img/troy2.jpg'],
      imdb:		'http://www.imdb.com/title/tt0332452',
      website:	'https://www.facebook.com/Troy.Film',
      likes:	485,
      dislikes:	21,
      posterindex: 0
	},
    {
      title:	'300',
      iscore:	7.7,
      rating:	'R',
      runtime:	117,
      released:	new Date('2007', '02', '09'),
      country:	'USA',
      posters:	['img/300_1.jpg','img/300_2.jpg','img/300_3.jpg','img/300_4.jpg'],
      imdb:		'http://www.imdb.com/title/tt0416449',
      website:	'https://www.facebook.com/300Movie',
      likes:	900,
      dislikes:	52,
      posterindex: 0
	},
    {
      title:	'Avengers: Age of Ultron',
      iscore:	7.5,
      rating:	'PG-13',
      runtime:	141,
      released:	new Date('2015', '04', '01'),
      country:	'USA',
      posters:	['img/ultron1.jpg','img/ultron2.jpg','img/ultron3.jpg','img/ultron4.jpg','img/ultron5.jpg','img/ultron6.jpg'],
      imdb:		'http://www.imdb.com/title/tt2395427',
      website:	'https://www.facebook.com/avengers',
      likes:	750,
      dislikes:	500,
      posterindex: 0
	}


  ];




	/* ADD VARIABLES FOR STEP 3 HERE */
	$scope.title = "IMDB Surfield's Top 8 Movies";
	$scope.owner = "Surfield";
	$scope.github = "https://github.com/Surfield/is219s16thomas-p3";





	/* ADD FUNCTIONS FOR STEP 7 HERE */

	$scope.like = function(index){
		$scope.movies[index].likes++;
	};
	$scope.dislike = function(index){
		$scope.movies[index].dislikes++;
	};
	$scope.posterClick = function(index){
		$scope.movies[index].posterindex++;
		if($scope.movies[index].posterindex > $scope.movies[index].posters.length-1){
			$scope.movies[index].posterindex=0;
		}
	};
	$scope.timeText = function(minutes){
		return Math.floor(minutes/60)+"h "+minutes%60+"m";
	};








}]);
