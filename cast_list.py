def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    with open(filename) as f:
    #use the for loop syntax to process each line
        for line in f:
            name = line.split(',')[0]
            cast_list.append(name)
    #and add the actor name to cast_list

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
