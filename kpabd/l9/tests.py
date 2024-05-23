from kpabd.models import part, tire, new_tire, used_tire, refurbished_tire
from kpabd.connection import manager


# Parts
p1 = part.Part(id=2, oem="1234", manufacturer="Michelin", number=100, description="Part")
p2 = part.Part(id=3, oem="5678", manufacturer="Michelin", number=200, description="Part")
part.insert(p1)
part.insert(p2)

found_part = part.find(2)
print(f"Part id 2: {found_part}")

part.update(2, "0000", "Michelin", 200, "Part")
updated_part = part.find(2)
print(f"Updated Part id 2: {updated_part}")

parts = part.find_all()
print(f"Parts before deleting: {parts}")

part.delete(2)
parts_after_deleting = part.find_all()
print(f"Parts after deleting: {parts_after_deleting} \n")


# Tires
t1 = tire.Tire(id=2, oem="1234", manufacturer="Michelin", number=100, description="Tire", speed=100, rating="A")
t2 = tire.Tire(id=3, oem="5678", manufacturer="Michelin", number=200, description="Tire", speed=150, rating="B")
tire.insert(t1)
tire.insert(t2)

found_tire = tire.find(2)
print(f"Tire id 2: {found_tire}")

tire.update(2, "0000", "Michelin", 200, "Tire", 150, "B")
updated_tire = tire.find(2)
print(f"Updated Tire id 2: {updated_tire}")

tires = tire.find_all()
print(f"Tires before deleting: {tires}")

tire.delete(2)
tires_after_deleting = tire.find_all()
print(f"Tires after deleting: {tires_after_deleting} \n")


# New tires
nt1 = new_tire.NewTire(id=2, oem="5678", manufacturer="Michelin", number=200, description="New Tire", speed=150, rating="B", onstock=50)
nt2 = new_tire.NewTire(id=3, oem="9101", manufacturer="Michelin", number=300, description="New Tire", speed=120, rating="C", onstock=100)
new_tire.insert(nt1)
new_tire.insert(nt2)

found_new_tire = new_tire.find(2)
print(f"New Tire id 2: {found_new_tire}")

new_tire.update(2, "0000", "Michelin", 200, "New Tire", 150, "B", 100)
updated_new_tire = new_tire.find(2)
print(f"Updated New Tire id 2: {updated_new_tire}")

new_tires = new_tire.find_all()
print(f"New Tires before deleting: {new_tires}")

new_tire.delete(2)
new_tires_after_deleting = new_tire.find_all()
print(f"New Tires after deleting: {new_tires_after_deleting} \n")


# Used tires
ut1 = used_tire.UsedTire(id=2, oem="9101", manufacturer="Michelin", number=300, description="Used Tire", speed=120, rating="C", production_year=2018, consumption_level="Medium")
ut2 = used_tire.UsedTire(id=3, oem="1121", manufacturer="Michelin", number=400, description="Used Tire", speed=130, rating="B", production_year=2014, consumption_level="Medium")
used_tire.insert(ut1)
used_tire.insert(ut2)

found_used_tire = used_tire.find(2)
print(f"Used Tire id 2: {found_used_tire}")

used_tire.update(2, "0000", "Michelin", 200, "Used Tire", 150, "B", 2014, "Low")
updated_used_tire = used_tire.find(2)
print(f"Updated Used Tire id 2: {updated_used_tire}")

used_tires = used_tire.find_all()
print(f"Used Tires before deleting: {used_tires}")

used_tire.delete(2)
used_tires_after_deleting = used_tire.find_all()
print(f"Used Tires after deleting: {used_tires_after_deleting} \n")


# Refurbished tires
rt1 = refurbished_tire.RefurbishedTire(id=2, oem="1121", manufacturer="Michelin", number=400, description="Refurbished Tire", speed=130, rating="B", production_year=2014, consumption_level="Medium", consumption_level_after_fixing="Low")
rt2 = refurbished_tire.RefurbishedTire(id=3, oem="1314", manufacturer="Michelin", number=500, description="Refurbished Tire", speed=140, rating="A", production_year=2016, consumption_level="High", consumption_level_after_fixing="Medium")
refurbished_tire.insert(rt1)
refurbished_tire.insert(rt2)

found_refurbished_tire = refurbished_tire.find(2)
print(f"Refurbished Tire id 2: {found_refurbished_tire}")

refurbished_tire.update(2, "0000", "Michelin", 200, "Refurbished Tire", 150, "B", 2014, "Low", "Medium")
updated_refurbished_tire = refurbished_tire.find(2)
print(f"Updated Refurbished Tire id 2: {updated_refurbished_tire}")

refurbished_tires = refurbished_tire.find_all()
print(f"Refurbished Tires before deleting: {refurbished_tires}")

refurbished_tire.delete(2)
refurbished_tires_after_deleting = refurbished_tire.find_all()
print(f"Refurbished Tires after deleting: {refurbished_tires_after_deleting} \n")


manager.close()
