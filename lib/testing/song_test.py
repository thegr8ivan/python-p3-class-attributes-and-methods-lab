import unittest
from lib.song import Song

class TestSong(unittest.TestCase):
    

    @classmethod
    def setUpClass(cls):
        # Set up any class variables, like the Song count
        Song.count = 0
        Song.genre_count = {}
        Song.artist_count = {}

        # Create Song instances to test
        cls.song1 = Song("99 Problems", "Jay-Z", "Rap")
        cls.song2 = Song("Halo", "Beyonce", "Pop")
        cls.song3 = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
        cls.song4 = Song("Out of touch", "Hall and Oates", "Pop")
        cls.song5 = Song("Song 2", "Jay-Z", "Rap")

    def test_saves_name_artist_genre(self):
        '''instantiates with a name, artist, and genre.'''
        out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
        self.assertEqual(out_of_touch.name, "Out of Touch")
        self.assertEqual(out_of_touch.artist, "Hall and Oates")
        self.assertEqual(out_of_touch.genre, "Pop")

    def test_has_song_count(self):
        '''counts the total number of Song objects.'''
        self.assertEqual(Song.count, 5)  
        Song("Sara Smile", "Hall and Oates", "Pop")
        self.assertEqual(Song.count, 6)

    def test_has_genres(self):
        '''keeps track of all Song genres.'''
        self.assertIn("Rap", Song.genre_count)
        self.assertIn("Pop", Song.genre_count)
        self.assertIn("Rock", Song.genre_count)

    def test_has_artists(self):
        '''keeps track of all Song artists.'''
        self.assertIn("Jay-Z", Song.artist_count)
        self.assertIn("Beyonce", Song.artist_count)
        self.assertIn("Nirvana", Song.artist_count)
        self.assertIn("Hall and Oates", Song.artist_count)

    def test_has_genre_count(self):
        '''keeps count of Songs for each genre.'''
        self.assertEqual(Song.genre_count["Rap"], 2)
        self.assertEqual(Song.genre_count["Pop"], 2)  
        self.assertEqual(Song.genre_count["Rock"], 1)

    def test_has_artist_count(self):
        '''keeps count of Songs for each artist.'''
        self.assertEqual(Song.artist_count["Jay-Z"], 2)
        self.assertEqual(Song.artist_count["Beyonce"], 1)
        self.assertEqual(Song.artist_count["Nirvana"], 1)
        self.assertEqual(Song.artist_count["Hall and Oates"], 1) 

if __name__ == "__main__":
    unittest.main()
