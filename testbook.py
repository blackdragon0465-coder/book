from book import book_details
def test_book_details():
    expected_output = (
        "Book ID: 1001\n"
        " Book Title: Atomic habit\n"
        " Author Name: Bob\n"
        " Publication Year: 2016\n"
    )
    assert book_details(1001, "Atomic habit", "Bob", 2016) == expected_output
