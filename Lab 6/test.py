i = "north"
o = {'south': 'Admins', 'east': 'Tutor', 'west': 'Parking'}
#print(o[i])
#print(len(o))
#a = []
#match_counter = 0
#not_match_counter = 0
#for key, value in o.items():
#    if i == key:
#        match_counter = match_counter + 1
        #print(match_counter)
#        j = i
#    else:
#        not_match_counter = not_match_counter + 1
        #print()
#if match_counter > 0:
#    return True
#else:
#    return False
#i = "##Hello##Hello##"
#l = len(i)
#for x in range(0,l):
#  if input[x] == " ":
#     if input[x+1] and input[x-1]
#r = rooms["reception"]["exit"]
#room = [{'id': 'biscuits', 'name': 'a pack of biscuits', 'description': 'A pack of biscuits.'}, {'id': 'handbook', 'name': 'a student handbook', 'description': 'This student handbook explains everything. Seriously.'}]
#ab =[]
#roomlen = len(room)
#print(roomlen)
#for x in range(0, len(room)):
#    g = room[x]
#    ans = g['name']
#    ab.append(ans)
#print(ab)
item_id = "handbook"
current_room_items =[]
current_room = [{'id': 'biscuits', 'name': 'a pack of biscuits', 'description': 'A pack of biscuits.'}, {'id': 'handbook', 'name': 'a student handbook', 'description': 'This student handbook explains everything. Seriously.'}]
inventory = [{'id': 'id', 'name': 'id card', 'description': 'You new shiny student ID card. Expires 1 June 2017.\nYou wonder why they have printed a suicide hotline number on it?...'}, {'id': 'laptop', 'name': 'laptop', 'description': 'It has seen better days. At least it has a WiFi card!'}, {'id': 'money', 'name': 'money', 'description': 'This wad of cash is barely enough to pay your tuition fees.'}]
print(inventory)
print(current_room)
#Remove handbook from current_room
#current_room[item_id]
l = len(current_room)
for x in range(0, l):
 current_room_list = current_room[x]
 if current_room_list["id"] == item_id:
    inventory.append(current_room_list)
    current_room.remove(current_room_list)
    print('match')
    print(inventory)
    print(current_room)

#Add handbook to inventory



