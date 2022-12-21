"""Print out all the melons in our inventory."""


from melons import melons_data 


def print_melon(melons_data):
    """Print each melon with corresponding attribute information."""

    for each_melon in melons_data.items():
        #print(each_melon)
        print(f"{each_melon[0]} \nprice: {each_melon[1]['price']} \nseedless: {each_melon[1]['seedlessness']} \nflesh color: {each_melon[1]['flesh_color']} \nrind color: {each_melon[1]['rind_color']} \naverage weight: {each_melon[1]['average_weight']}\n")


        #print(f"{each_melon[0]} \nprice: {each_melon[1][0]} \nseedless: {each_melon[1][1]} \nflesh color: {each_melon[1][2]} \nrind color: {each_melon[1][3]} \naverage weight: {each_melon[1][4]}\n")
        

print_melon(melons_data)