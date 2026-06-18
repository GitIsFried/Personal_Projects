#Rooms and their times in military formal 0000 
class BackRooms:
    def __init__(self, name, session_times):
        self.name = name
        self.session_times = session_times
        self.votes = 0
#1845
Mad_Scientist = BackRooms("Mad_Scientist", [1845, 2030, 2215])
Black_Queen = BackRooms("Black_Queen", [1015, 1200, 2230])
Gaol_Break = BackRooms("Gaol_Break", [1030, 2100, 2245])
Speak_Easy = BackRooms("Speak_Easy", [1000, 1145, 1330, 2215])
Abandoned_Cabin = BackRooms("Abandoned_Cabin", [1015, 1345, 1900, 2045, 2230])
Mafia = BackRooms("Mafia", [1030, 1215, 1915, 2100, 2245])
escape_Rooms = [Mad_Scientist, Black_Queen, Gaol_Break, Speak_Easy, Abandoned_Cabin, Mafia]

# They'll store Time[Start, End] in military format and Rooms[] match with Room Types
class Attendees:
    def __init__(self, name, RSVP, s_time, e_time, votes):
        self.name = name
        self.RSVP = RSVP
        self.s_time = s_time
        self.e_time = e_time
        self.votes = votes

Ocean = Attendees("Ocean", True, 900, 2300, ["Black_Queen", "Speak_Easy", "Mafia"])
Leuwin = Attendees("Leuwin", True, 100, 2359, ["Yellow Submarine"]) #Test outlandish values
Didier = Attendees("Didier", True, 1400, 2100, ["Black_Queen"])
Nour = Attendees("Nour", True, 1200, 1900, ["Black_Queen", "Abandoned_Cabin"])
Kosta = Attendees("Kosta", True, None, None, [None])
Falah = Attendees("Falah", True, None, None, [None])
Punya = Attendees("Punya", True, 900, 2359, ["Any"])
Nick = Attendees("Nick", True, 1200, 2359, ["Gaol_Break", "Abandoned_Cabin"])
Shane = Attendees("Shane", False, None, None, [None]) # Not coming
Zak = Attendees("Zak", True, 900, 2300, ["Mafia"])
Kyle = Attendees("Kyle", True, None, None, [None])
Andrew = Attendees("Andrew", True, 900, 2359, "Any")
Corbin = Attendees("Corbin", False, None, None, [None])
Aidan = Attendees("Aidan", False, None, None, [None])
Fletcher = Attendees("Fletcher", False, None, None, [None])
Mads = Attendees("Mads", True, None, None, "Any")
Harry = Attendees("Harry", True, None, None, [None])
attending = [Ocean, Leuwin, Didier, Nour, Kosta, Falah, Punya, Nick, Shane, Zak, Kyle, Andrew, Corbin, Aidan, Fletcher, Mads, Harry]

#Remove attendees if time and/or rooms are empty[note not null as the empty [] are still there, just not null]
attending = [everyone for everyone in attending if everyone.RSVP == True and everyone.s_time != None and everyone.e_time != None and everyone.votes != None]
print("Total Attendees: ", len(attending))
for everyone in attending:
    print("Attendees: ", everyone.name)

#Filter time zone outliars
#Filter those whose end times doesn't overlap with other's start times
#Filter those whose start time doesn't overlap with other's end times
attending_filter = []
for compare in attending:
    for contrast in attending:
        if compare != contrast:
            if compare.s_time < contrast.e_time and compare.e_time > contrast.s_time and compare not in attending_filter:
                attending_filter.append(compare)
for everyone in attending_filter:
    print("Attendees: ", everyone.name)

#Calculate best times with current times
#Calculate everyone's best availability overlap
start_Time = 0000
for everyone in attending_filter: #Finds 
    if start_Time < everyone.s_time:
        start_Time = everyone.s_time
print("start_Time: ", start_Time)

end_Time = 2400
for everyone in attending_filter: #Finds 
    if end_Time > everyone.e_time:
        end_Time = everyone.e_time
print("end_Time: ", end_Time)

#Filter rooms with availabile time that is within that time range
escape_Rooms_filter = []
for rooms in escape_Rooms:
    for time_available in rooms.session_times: 
        if  time_available > start_Time and time_available < end_Time:
            escape_Rooms_filter.append(rooms)

if len(escape_Rooms_filter) <= 0:
    consider_Rooms = escape_Rooms
else:
    consider_Rooms = escape_Rooms_filter


#Calculate Room popularity
for everyone in attending_filter: #Finds 
    for picks in everyone.votes:
        for rooms in consider_Rooms:
            if picks == rooms.name:
                rooms.votes += 1 
    if everyone.votes == "Any":
        for rooms in consider_Rooms:
            rooms.votes += 1

for rooms in consider_Rooms:
    print(f"Votes for {rooms.name}: ", rooms.votes)
    print(f"Votes for {rooms.name}: ", rooms.session_times)

#If no escape room can fit everyone's availiability, find one that is closest to everyone's availability
popular_Rooms_filter = []
for rooms in consider_Rooms:
    for time_available in rooms.session_times: 
        if  time_available > start_Time - 1 and time_available < end_Time + 1:
            popular_Rooms_filter.append(rooms)

scope = 1
chosen_Room_times = 6767
chosen_Room_votes = 0 
chosen_Room = []
for rooms in consider_Rooms:
    if rooms.votes >= chosen_Room_votes and rooms.name:
        chosen_Room.append(rooms)
        for time_available in rooms.session_times: 
            while True:
                found_time = False

                for available in rooms.session_times:
                    if start_Time - scope * 100 <= available <= end_Time + scope * 100:
                        chosen_Room_times = available
                        found_time = True
                        break

                if found_time:
                    break

                scope += 1
                
# chosen_Room
# chosen_Room_votes
#Print best room with best time for yall
print("")
print("-----------------------------------------------")
print(f"The chosen room with the best times for everyone and with the highest votes is")
for rooms in chosen_Room:
    print(f"{rooms.name}, with {rooms.votes}")
print(f"The best time chosen is {chosen_Room_times}")
escape_Attendees = []
for everyone in attending_filter:
    if everyone.s_time < chosen_Room_times and everyone.e_time > chosen_Room_times:
        escape_Attendees.append(everyone.name)
print(f"The number of attendees to the escape room is {len(escape_Attendees)} people")
print(f"Possible attendees are:")
for everyone in escape_Attendees:
    print(everyone)
print("-----------------------------------------------")