class Media:
    """A class representing a media"""
    title: str
    artist: str
    releaseDate: str
    url: str
    
    def __init__(self, title = "No Title", artist = "No Artist", releaseDate = "No Release Date", url = "No URL"):
        """
        Constructs all the necessary attributes for the Media object.
        You need to init the instance with the following attribute with default value
        by passing the following parameter to the constructor.

        Parameters
        ----------
        title : str
            The title of the media, default value: "No Title"
        artist : str
            The artist of the media, default value: "No Artist"
        releaseDate : str
            The relase date of the media, default value: "No Release Date"
        url : str
            The URL of the media, default value: "No URL"

        Attributes
        -----------
        self.title 
        self.artist 
        etc.
        """
        self.title = title
        self.artist = artist
        self.releaseDate = releaseDate
        self.url = url
        

    def info(self):
        """
        Return a formatted string including the information of the media

        Format:
        <media title> by <artist> (<release date>)

        For example, “Bridget Jones's Diar (Unabridged) by Helen Fielding (2012)”
        """
        return f"{self.title} by {self.artist} ({self.releaseDate})"
        

    def length(self):
        """
        Return 0 as the length of the media

        You don't need to modify this class method
        """
        return 0

    def play(self):
        """
        Print the content of the media in the standard output.
        
        You should include the media information.

        Format:
        <media title> by <artist> (<release date>)
        """
        print(self.info())


class Track(Media):
    """ A class representing a music track."""
    title: str
    artist: str
    releaseDate: str
    url: str
    album: str
    genre: str
    duration: int
    
    def __init__(self, title, artist, releaseDate, url, album="No Album", genre="No Genre", duration=0):
        """
        Constructs all the necessary attributes for the Track object.
        remeber to use super().__init__(some parameters).
        Additional instance variables: 
        album (default value: "No Album"), 
        genre (default value: "No Genre"), 
        duration (default value: 0)

        Parameters
        ----------
        title : str
            The title of the track.
        artist : str
            The artist or group who performed the track.
        releaseDate : str
            The release date of the track.
        url : str
            The URL for the track.
        album : str
            The album on which the track appears.
        genre : str
            The genre of the track.
        duration : int 
            The duration of the track in seconds(rounded to nearest second).

        Attributes
        -----------
        self.title 
        self.artist 
        etc.        
        """
        super().__init__(title, artist, releaseDate, url)
        self.album = album
        self.genre = genre
        self.duration = duration / 1000
        

    def info(self):
        """
        Return a formatted string including the information of the music track
        It should add “[<genre>]” to the end of the output from Media.info(). 

        Format:
        <music title> by <artist> - <music album> (<release date>) [<genre>]
        For example “Hey Jude by The Beatles (1968) [Rock]”

        """
        return f"{self.title} by {self.artist} - {self.album} ({self.releaseDate}) [{self.genre}]"
        

    def length(self):
        """
        Return the length of the music in seconds(rounded to nearest second)

        Notice the length in the provide json might not in seconds
        """
        return round(self.duration)
        

    def play(self):
        """
        Print the content of the music track in the standard output.
        
        You should include the music information along with the music length.

        Format:
        <music title> by <artist> - <music album> (<release date>) length: <length> sec
        """
        print(f"{self.info()} length: {self.length()} sec")


class Movie(Media):
    """ A class representing a movie."""
    title: str
    artist: str
    releaseDate: str
    url: str
    rating: str
    movieLength: int
    
    def __init__(self, title, artist, releaseDate, url, rating="No Rating", movieLength=0):
        """
        Constructs all the necessary attributes for the Movie object.
        remeber to use super().__init__(some parameters).
        Additional instance variables: 
        rating (default value: "No Rating"),
        movieLength (default value: 0) 

        Parameters
        ----------
        title : str
            The title of the movie.
        artist : str
            The artist or group who contributes to the movie.
        releaseDate : str
            The release date of the movie.
        url : str
            The URL for the movie.
        rating : str
            The rating of the movie.
        movieLength : int
            The movie length in minutes(rounded to nearest minute)

        Attributes
        -----------
        self.title 
        self.artist 
        etc.
        """
        super().__init__(title, artist, releaseDate, url)
        self.rating = rating
        self.movieLength = movieLength / 60000

        

    def info(self):
        """
        Return a formatted string including the information of the movie
        add “[<rating>]” to the end of the output from Media.info( ). 

        Format:
        <movie title> by <artist> (<release date>) [<movie rating>]

        For example “Jaws by Steven Speilberg (1975) [PG]”
        """
        return f"{self.title} by {self.artist} ({self.releaseDate}) [{self.rating}]"
        

    def length(self):
        """
        Return the length of the movie in minutes(rounded to nearest minute)

        Notice the length in the provide json might not in minutes
        """
        return round(self.movieLength)
        

    def play(self):
        """
        Print the content of the movie in the standard output.
        
        You should include the movie information along with the movie length.

        Format:
        <movie title> by <artist> (<release date>) [<movie rating>] length: <length> mins
        """
        print(f"{self.info()} length: {self.length()} mins")