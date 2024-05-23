from neo4j import GraphDatabase
from secret import URI, USERNAME, PASSWORD

class Person:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Person: {self.name}"


class Movie:
    def __init__(self, title) -> None:
        self.title = title

    def __repr__(self) -> str:
        return f"Movie: {self.title}"


class ActedIn:
    def __init__(self, person, movie, role) -> None:
        self.person = person
        self.movie = movie
        self.role = role

    def __repr__(self) -> str:
        return f"{self.person.name} acted in {self.movie.title} as {self.role}"


class Neo4jConnection:
    def __init__(self, uri, username, password) -> None:
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        self.driver.close()

    def get_person(self, name):
        query = "MATCH (p:Person {name: $name}) RETURN p"
        with self.driver.session() as session:
            result = session.run(query, name=name)
            try:
                return Person(result.single()["p"]["name"])
            except (TypeError, KeyError):
                return None

    def get_people(self):
        query = "MATCH (p:Person) RETURN p"
        with self.driver.session() as session:
            result = session.run(query)
            return [Person(record["p"]["name"]) for record in result]

    def get_movie(self, title):
        query = "MATCH (m:Movie {title: $title}) RETURN m"
        with self.driver.session() as session:
            result = session.run(query, title=title)
            try:
                return Movie(result.single()["m"]["title"])
            except (TypeError, KeyError):
                return None

    def get_movies(self):
        query = "MATCH (m:Movie) RETURN m"
        with self.driver.session() as session:
            result = session.run(query)
            return [Movie(record["m"]["title"]) for record in result]

    def get_acted_in(self, person_name, movie_title):
        query = """
            MATCH (p:Person {name: $person_name})-[r:ACTED_IN]->(m:Movie {title: $movie_title})
            RETURN p, r, m
        """
        with self.driver.session() as session:
            result = session.run(query, person_name=person_name, movie_title=movie_title)
            try:
                record = result.single()
                person = Person(record["p"]["name"])
                movie = Movie(record["m"]["title"])
                return ActedIn(person, movie, record["r"]["role"])
            except (TypeError, KeyError):
                return None

    def get_acted_ins(self):
        query = "MATCH (p:Person)-[r:ACTED_IN]->(m:Movie) RETURN p, r, m"
        with self.driver.session() as session:
            result = session.run(query)
            return [ActedIn(Person(record["p"]["name"]), Movie(record["m"]["title"]), record["r"]["role"]) for record in result]

    def add_person(self, name):
        query = "CREATE (p:Person {name: $name})"
        with self.driver.session() as session:
            session.run(query, name=name)

    def add_movie(self, title):
        query = "CREATE (m:Movie {title: $title})"
        with self.driver.session() as session:
            session.run(query, title=title)

    def add_acted_in(self, person_name, movie_title, role):
        query = """
            MATCH (p:Person {name: $person_name}), (m:Movie {title: $movie_title})
            CREATE (p)-[r:ACTED_IN {role: $role}]->(m)
        """
        with self.driver.session() as session:
            session.run(query, person_name=person_name, movie_title=movie_title, role=role)

    def update_person(self, name, new_name):
        query = "MATCH (p:Person {name: $name}) SET p.name = $new_name"
        with self.driver.session() as session:
            session.run(query, name=name, new_name=new_name)

    def update_movie(self, title, new_title):
        query = "MATCH (m:Movie {title: $title}) SET m.title = $new_title"
        with self.driver.session() as session:
            session.run(query, title=title, new_title=new_title)

    def update_acted_in(self, person_name, movie_title, new_role):
        query = """
            MATCH (p:Person {name: $person_name})-[r:ACTED_IN]->(m:Movie {title: $movie_title})
            SET r.role = $new_role
        """
        with self.driver.session() as session:
            session.run(query, person_name=person_name, movie_title=movie_title, new_role=new_role)

    def delete_person(self, name):
        query = "MATCH (p:Person {name: $name}) DETACH DELETE p"
        with self.driver.session() as session:
            session.run(query, name=name)

    def delete_movie(self, title):
        query = "MATCH (m:Movie {title: $title}) DETACH DELETE m"
        with self.driver.session() as session:
            session.run(query, title=title)

    def delete_acted_in(self, person_name, movie_title):
        query = "MATCH (p:Person {name: $person_name})-[r:ACTED_IN]->(m:Movie {title: $movie_title}) DELETE r"
        with self.driver.session() as session:
            session.run(query, person_name=person_name, movie_title=movie_title)


if __name__ == "__main__":
    connection = Neo4jConnection(URI, USERNAME, PASSWORD)
    # Add person
    connection.add_person("Tom Hanks")
    # Add movie
    connection.add_movie("Forrest Gump")
    # Add acted in
    connection.add_acted_in("Tom Hanks", "Forrest Gump", "Forrest Gump")
    # Get person
    print(connection.get_person("Tom Hanks"))
    # Get people
    print("People:")
    for person in connection.get_people():
        print(f"  {person}")
    # Get movie
    print(connection.get_movie("Forrest Gump"))
    # Get movies
    print("Movies:")
    for movie in connection.get_movies():
        print(f"  {movie}")
    # Get acted in
    print(connection.get_acted_in("Tom Hanks", "Forrest Gump"))
    # Get acted ins
    print("Acted ins:")
    for acted_in in connection.get_acted_ins():
        print(f"  {acted_in}")
    # Update person
    connection.update_person("Tom Hanks", "Tom Cruise")
    # Update movie
    connection.update_movie("Forrest Gump", "The Green Mile")
    # Update acted in
    connection.update_acted_in("Tom Cruise", "The Green Mile", "Paul Edgecomb")
    # Get person
    print(connection.get_person("Tom Cruise"))
    # Get movie
    print(connection.get_movie("The Green Mile"))
    # Get acted in
    print(connection.get_acted_in("Tom Cruise", "The Green Mile"))
    # Delete acted in
    connection.delete_acted_in("Tom Cruise", "The Green Mile")
    # Delete movie
    connection.delete_movie("The Green Mile")
    # Delete person
    connection.delete_person("Tom Cruise")
    connection.close()
