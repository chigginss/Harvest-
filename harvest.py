############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = [
        MelonType("musk", 1998, "green", True, True, "Muskmelon"),
        MelonType("cas", 2003, "orange", False, False, "Casaba"),
        MelonType("cren", 1996, "green", False, False, "Crenshaw"),
        MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
        ]
    all_melon_types[0].add_pairing("mint")
    all_melon_types[1].add_pairing("strawberries")
    all_melon_types[1].add_pairing("mint")
    all_melon_types[2].add_pairing("proscuitto")
    all_melon_types[3].add_pairing("ice cream")

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print "{name} pairs with".format(name=melon.name)
        for pairing in melon.pairings:
            print "- {pairing}".format(pairing=pairing)
        print ""


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melons = {}
    for melon in melon_types:
        melons[melon.code] = melon
    return melons


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, harvested_from,
                 harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by

    def is_sellable(self):
        if (self.shape_rating > 5 and self.color_rating > 5
                and self.harvested_from != 3):
            return True
        return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_by_id = make_melon_type_lookup(make_melon_types())
    melons = [
        Melon(melons_by_id["yw"], 8, 7, 2, "Sheila"),
        Melon(melons_by_id["yw"], 3, 4, 2, "Sheila"),
        Melon(melons_by_id["yw"], 9, 8, 3, "Sheila"),
        Melon(melons_by_id["cas"], 10, 6, 35, "Sheila"),
        Melon(melons_by_id["cren"], 8, 9, 35, "Michael"),
        Melon(melons_by_id["cren"], 8, 2, 35, "Michael"),
        Melon(melons_by_id["cren"], 2, 3, 4, "Michael"),
        Melon(melons_by_id["musk"], 6, 7, 4, "Michael"),
        Melon(melons_by_id["yw"], 7, 10, 3, "Sheila")
        ]

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        message = "Harvested by {name} from Field # {field}".format(
            name=melon.harvested_by, field=melon.harvested_from)
        if melon.is_sellable():
            print "{} CAN BE SOLD".format(message)
        else:
            print "{} NOT SELLABLE".format(message)


#################
# Further Study #
#################


def parse_harvest_file(filename):
    """Open and read harvest file, returns melon_list"""

    melon_types = make_melon_type_lookup(make_melon_types())
    # melon_list = []
    melons = {}

    data = open(filename)
    for line in data:
        line = line.strip()

        _, shape, _, color, _, melon_type, _, _, harvested_by, _, _, harvested_from = line.split()

        # end_index = 0

        # start_index = end_index + 6
        # end_index = line.index(' ', start_index)
        # shape = int(line[start_index:end_index])

        # start_index = end_index + 7
        # end_index = line.index(' ', start_index)
        # color = int(line[start_index:end_index])

        # start_index = end_index + 6
        # end_index = line.index(' ', start_index)
        # melon_type = line[start_index:end_index]

        # start_index = end_index + 14
        # end_index = line.index(' ', start_index)
        # harvested_by = line[start_index:end_index]

        # start_index = end_index + 9
        # harvested_from = int(line[start_index:])

        melon = Melon(melon_types[melon_type], int(shape), int(color),
                      int(harvested_from), harvested_by)

        if melon.harvested_by in melons:
            melons[melon.harvested_by].append(melon)
        else:
            melons[melon.harvested_by] = [melon]

        # melon_list.append(melon)

    # return melon_list
    return melons

if __name__ == '__main__':

    # melon_types = make_melon_types()

    # print_pairing_info(melon_types)

    # melons = make_melons(melon_types)

    # get_sellability_report(melons)

    melons = parse_harvest_file("harvest_log.txt")

    # melon_list = sorted(melon_list, key=lambda x: x.harvested_by)

    for harvested_by in melons:
        get_sellability_report(melons[harvested_by])

    # get_sellability_report()
