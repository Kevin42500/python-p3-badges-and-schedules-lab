def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(speakers):
    room_assignments = []
    for index, speaker in enumerate(speakers, start=1):
        room_assignments.append(f"Hello, {speaker}! You'll be assigned to room {index}!")
    return room_assignments

def printer(speakers):
    badges = batch_badge_creator(speakers)
    room_assignments = assign_rooms(speakers)
    
    for badge in badges:
        print(badge)
    
    for assignment in room_assignments:
        print(assignment)

speaker_list = ["Arel", "Carol", "John"]
printer(speaker_list)
