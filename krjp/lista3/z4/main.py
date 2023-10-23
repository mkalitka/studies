NUM_DICT = {
    "jeden": 1,
    "dwa": 2,
    "trzy": 3,
    "cztery": 4,
    "pięć": 5,
    "sześć": 6,
    "siedem": 7,
    "osiem": 8,
    "dziewięć": 9,
    "dziesięć": 10,
    "jedenaście": 11,
    "dwanaście": 12,
    "trzynaście": 13,
    "czternaście": 14,
    "piętnaście": 15,
    "szesnaście": 16,
    "siedemnaście": 17,
    "osiemnaście": 18,
    "dziewiętnaście": 19,
    "dwadzieścia": 20,
    "trzydzieści": 30,
    "czterdzieści": 40,
    "pięćdziesiąt": 50,
    "sześćdziesiąt": 60,
    "siedemdziesiąt": 70,
    "osiemdziesiąt": 80,
    "dziewięćdziesiąt": 90,
    "sto": 100,
    "dwieście": 200,
    "trzysta": 300,
    "czterysta": 400,
    "pięćset": 500,
    "sześćset": 600,
    "siedemset": 700,
    "osiemset": 800,
    "dziewięćset": 900,
    "tysiąc": 1000,
}


def convert_string_into_int(str_num: str) -> int:
    if "tysiące" in str_num or "tysięcy" in str_num:
        if "tysiące" in str_num:
            thousands_parts = str_num.split("tysiące", 1)
        else:
            thousands_parts = str_num.split("tysięcy", 1)
        thousands = thousands_parts[0].strip()
        hundreds = thousands_parts[1].strip()
        return convert_string_into_int(thousands) * 1000 + convert_string_into_int(hundreds)

    parts = str_num.split(" ", 1)

    if parts[0] in NUM_DICT and len(parts) == 2:
        return NUM_DICT[parts[0]] + convert_string_into_int(parts[1])
    elif parts[0] in NUM_DICT:
        return NUM_DICT[parts[0]]
    else:
        return 0


def sort_list(list_to_sort: list) -> list:
    return sorted(list_to_sort, key=convert_string_into_int)


if __name__ == "__main__":
    print(
        sort_list(
            [
                "pięćset dwadzieścia tysięcy osiem",
                "dwa tysiące trzysta osiemnaście",
                "sto tysięcy",
                "tysiąc dwanaście",
            ]
        )
    )
