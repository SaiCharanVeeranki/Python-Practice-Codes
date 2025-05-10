class Movie:
    def __init__(self,title,director):
        self.title = title
        self.director = director
        self.is_watched = False

    def display_info(self):
        if self.is_watched:
            Status = "Watched"
        else:
            Status = "Not Watched"
        print(f"Title: {self.title}, Director: {self.director}, Status: {Status}")
    
    def mark_watched(self):
        self.is_watched = True
        print(f"{self.title} has been marked as watched.")

my_movie = Movie("Inception", "Christopher Nolan")
my_movie.display_info()
my_movie.mark_watched()
my_movie.display_info()