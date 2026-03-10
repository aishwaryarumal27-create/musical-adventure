contacts = {
    "Gagan": "9876543210",
    "Aishu": "9123456780",
    "Sharan": "9988776655"
}
contacts["Priya"] = "9012345678"
contacts["Amit"] = "9000000000"
print("Lookup Existing:", contacts.get("Aishu"))
print("Lookup Missing:", contacts.get("Ravi", "Contact not found"))
print("All Contacts:")
for name, number in contacts.items():
    print(f"Contact: {name} | Phone: {number}")