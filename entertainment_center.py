import movies
import fresh_tomatoes

moving_castle = movies.Movie("Howl's Moving Castle", "2004", "Hayao Miyazaki", 
	"When a young woman is cursed with an old body by a spiteful witch, her only chance of breaking the spell lies with a self-indulgent yet insecure young wizard and his companions in his legged, walking castle.", 
	"https://upload.wikimedia.org/wikipedia/en/a/a0/Howls-moving-castleposter.jpg", 
	"https://www.youtube.com/watch?v=iwROgK94zcM")

princess_mononoke = movies.Movie("Princess Mononoke", "1997", "Hayao Miyazaki", 
	"On a journey to find the cure for a Tatarigami's curse, Ashitaka finds himself in the middle of a war between the forest gods and Tatara, a mining colony. In this quest he also meets San, the Mononoke Hime.", 
	"https://upload.wikimedia.org/wikipedia/en/2/24/Princess_Mononoke_Japanese_Poster_%28Movie%29.jpg", 
	"https://www.youtube.com/watch?v=pkWWWKKA8jY")

spirited_away = movies.Movie("Spirited Away", "2001", "Hayao Miyazaki", 
	"During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts.", 
	"https://upload.wikimedia.org/wikipedia/en/3/30/Spirited_Away_poster.JPG", 
	"https://www.youtube.com/watch?v=ByXuk9QqQkk")

your_name = movies.Movie("Your Name", "2016", "Makoto Shinkai", 
	"Two strangers find themselves linked in a bizarre way. When a connection forms, will distance be the only thing to keep them apart?", 
	"https://upload.wikimedia.org/wikipedia/en/0/0b/Your_Name_poster.png", 
	"https://www.youtube.com/watch?v=hRfHcp2GjVI")

ghost_in_shell = movies.Movie("Ghost in the Shell", "1995", "Kazunori Itō", 
	"A cyborg policewoman and her partner hunt a mysterious and powerful hacker called the Puppet Master.", 
	"https://upload.wikimedia.org/wikipedia/en/c/ca/Ghostintheshellposter.jpg", 
	"https://www.youtube.com/watch?v=oP2Pt6m3yKU")

wolf_children = movies.Movie("Wolf Children", "2012", "Mamoru Hosoda", 
	"After her werewolf lover unexpectedly dies in an accident, a woman must find a way to raise the werewolf son and daughter that she had with him. But their inheritance of their father's traits proved to be a challenge for her.", 
	"https://upload.wikimedia.org/wikipedia/en/9/9c/%C5%8Ckami_Kodomo_no_Ame_to_Yuki_poster.jpg", 
	"https://www.youtube.com/watch?v=ed1xwAtF728")

five_cm_second = movies.Movie("5 Centimeters per Second", "2007", "Makoto Shinkai",  
	"Told in three interconnected segments, we follow a young man named Takaki through his life as cruel winters, cold technology, and finally, adult obligations and responsibility converge to test the delicate petals of love.", 
	"https://upload.wikimedia.org/wikipedia/en/7/79/5_Centimeters_Per_Second_poster.jpg", 
	"https://www.youtube.com/watch?v=wdM7athAem0")

girl_through_time = movies.Movie("The Girl Who Leapt Through Time", "2006", "Mamoru Hosoda", 
	"A high-school girl named Makoto acquires the power to travel back in time, and decides to use it for her own personal benefits. Little does she know that she is affecting the lives of others just as much as she is her own.", 
	"https://upload.wikimedia.org/wikipedia/en/4/4e/The_Girl_Who_Leapt_Through_Time_poster.jpg", 
	"https://www.youtube.com/watch?v=U_ULXRMvU7k")

anime = [moving_castle, princess_mononoke, spirited_away, your_name, ghost_in_shell, wolf_children, five_cm_second, girl_through_time]


fresh_tomatoes.open_movies_page(anime)

