import argparse
from .connection import manager
from .models import part, tire, new_tire, used_tire, refurbished_tire


def handle_part(filter_query=None, sort_column=None, sort_order=None):
    if filter_query:
        print(filter_query)
        parts = part.find_filter(filter_query)
    elif sort_column:
        parts = part.find_all_sorted(sort_column, sort_order)
    else:
        parts = part.find_all()
    table = [
        ["ID", "OEM", "Manufacturer", "Number", "Description"]
    ]
    for p in parts:
        table.append([p.id, p.oem, p.manufacturer, p.number, p.description])
    for row in table:
        print("{: >5} {: >20} {: >20} {: >20} {: >20}".format(*row))


def handle_tire(filter_query=None, sort_column=None, sort_order=None):
    if filter_query:
        tires = tire.find_filter(filter_query)
    elif sort_column:
        tires = tire.find_all_sorted(sort_column, sort_order)
    else:
        tires = tire.find_all()
    table = [
        ["ID", "OEM", "Manufacturer", "Number", "Description", "Speed", "Rating"]
    ]
    for t in tires:
        table.append([t.id, t.oem, t.manufacturer, t.number, t.description, t.speed, t.rating])
    for row in table:
        print("{: >5} {: >20} {: >20} {: >20} {: >20} {: >20} {: >20}".format(*row))


def handle_new_tire(filter_query=None, sort_column=None, sort_order=None):
    if filter_query:
        new_tires = new_tire.find_filter(filter_query)
    elif sort_column:
        new_tires = new_tire.find_all_sorted(sort_column, sort_order)
    else:
        new_tires = new_tire.find_all()
    table = [
        ["ID", "OEM", "Manufacturer", "Number", "Description", "Speed", "Rating", "On Stock"]
    ]
    for t in new_tires:
        table.append([t.id, t.oem, t.manufacturer, t.number, t.description, t.speed, t.rating, t.onstock])
    for row in table:
        print("{: >5} {: >20} {: >20} {: >20} {: >20} {: >20} {: >20} {: >20}".format(*row))

def handle_used_tire(filter_query=None, sort_column=None, sort_order=None):
    if filter_query:
        used_tires = used_tire.find_filter(filter_query)
    elif sort_column:
        used_tires = used_tire.find_all_sorted(sort_column, sort_order)
    else:
        used_tires = used_tire.find_all()
    table = [
        ["ID", "OEM", "Manufacturer", "Number", "Description", "Speed", "Rating", "Prod Year", "Consump lvl"]
    ]
    for t in used_tires:
        table.append([t.id, t.oem, t.manufacturer, t.number, t.description, t.speed, t.rating, t.production_year, t.consumption_level])
    for row in table:
        print("{: >5} {: >20} {: >20} {: >20} {: >20} {: >20} {: >20} {: >20} {: >20}".format(*row))


def handle_refurbished_tire(filter_query=None, sort_column=None, sort_order=None):
    if filter_query:
        refurbished_tires = refurbished_tire.find_filter(filter_query)
    elif sort_column:
        refurbished_tires = refurbished_tire.find_all_sorted(sort_column, sort_order)
    else:
        refurbished_tires = refurbished_tire.find_all()
    table = [
        ["ID", "OEM", "Manufacturer", "Number", "Description", "Speed", "Rating", "Prod Year", "Consump lvl", "Consump lvl after fixing"]
    ]
    for t in refurbished_tires:
        table.append([t.id, t.oem, t.manufacturer, t.number, t.description, t.speed, t.rating, t.production_year, t.consumption_level, t.consumption_level_after_fixing])
    for row in table:
        print("{: >5} {: >20} {: >20} {: >20} {: >20} {: >20} {: >20} {: >20} {: >20} {: >20}".format(*row))


def main():
    parser = argparse.ArgumentParser(description="KPABD project")
    subparsers = parser.add_subparsers(dest="command", help="model to use")

    parser_part = subparsers.add_parser("part", help="show all parts")
    parser_part.add_argument("--filter", help="filter query", required=False, type=str)
    parser_part.add_argument("--sort-column", help="column to be sorted", required=False, type=str)
    parser_part.add_argument("--sort-order", help="sort order", choices=["ASC", "DESC"], default="ASC", type=str)

    parser_tire = subparsers.add_parser("tire", help="show all tires")
    parser_tire.add_argument("--filter", help="filter query", required=False, type=str)
    parser_tire.add_argument("--sort-column", help="column to be sorted", default=None, type=str)
    parser_tire.add_argument("--sort-order", help="sort order", choices=["ASC", "DESC"], default="ASC", type=str)

    parser_new_tire = subparsers.add_parser("new_tire", help="show all new tires")
    parser_new_tire.add_argument("--filter", help="filter query", required=False, type=str)
    parser_new_tire.add_argument("--sort-column", help="column to be sorted", default=None, type=str)
    parser_new_tire.add_argument("--sort-order", help="sort order", choices=["ASC", "DESC"], default="ASC", type=str)

    parser_used_tire = subparsers.add_parser("used_tire", help="show all used tires")
    parser_used_tire.add_argument("--filter", help="filter query", required=False, type=str)
    parser_used_tire.add_argument("--sort-column", help="column to be sorted", default=None, type=str)
    parser_used_tire.add_argument("--sort-order", help="sort order", choices=["ASC", "DESC"], default="ASC", type=str)

    parser_refurbished_tire = subparsers.add_parser("refurbished_tire", help="show all refurbished tires")
    parser_refurbished_tire.add_argument("--filter", help="filter query", required=False, type=str)
    parser_refurbished_tire.add_argument("--sort-column", help="column to be sorted", default=None, type=str)
    parser_refurbished_tire.add_argument("--sort-order", help="sort order", choices=["ASC", "DESC"], default="ASC", type=str)

    args = parser.parse_args()
    if args.command == "part":
        handle_part(filter_query=args.filter, sort_column=args.sort_column, sort_order=args.sort_order)
    elif args.command == "tire":
        handle_tire(filter_query=args.filter, sort_column=args.sort_column, sort_order=args.sort_order)
    elif args.command == "new_tire":
        handle_new_tire(filter_query=args.filter, sort_column=args.sort_column, sort_order=args.sort_order)
    elif args.command == "used_tire":
        handle_used_tire(filter_query=args.filter, sort_column=args.sort_column, sort_order=args.sort_order)
    elif args.command == "refurbished_tire":
        handle_refurbished_tire(filter_query=args.filter, sort_column=args.sort_column, sort_order=args.sort_order)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
