import psycopg2
import logging

logging.basicConfig(filename="snippets.log", level= logging.DEBUG)
logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect(database="snippets")
logging.debug("Database connection established.")
def put(name, snippet):
    logging.info("Storing snippet {!r}: {!r}".format(name, snippet))
    cursor = connection.cursor()
    command = "insert into snippets values (%s, %s)"
    cursor.execute(command, (name, snippet))
    connection.commit()
    logging.debug("Snippet stored successfully.")
    return name, snippet


    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
    return name, snippet

def get(name):
    """
    Retrieve the snippet with a given name.

    If there is no such snippet, return '404: Snippet Not Found'.

    Returns the snippet.
    """

    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return ""

