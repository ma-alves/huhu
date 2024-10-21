__app_name__ = "huhu"
__author__ = "ma-alves"
__version__ = "0.1.0"


HUMOR = {
    1: 'worst',
    2: 'bad',
    3: 'okay',
    4: 'good',
    5: 'great'
}

DATABASE = 'database.json'
TEST_DATABASE = 'test_database.json'

# Sem uso por enquanto
(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(7)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    DB_READ_ERROR: "database read error",
    DB_WRITE_ERROR: "database write error",
    ID_ERROR: "to-do id error",
}