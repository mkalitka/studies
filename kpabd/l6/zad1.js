print("Listing all available databases:");
db.adminCommand({ listDatabases: 1 }).databases.forEach(function(database) {
    print("- " + database.name);
});
