from book import book_details
def test_book_details():
    expected_output = (
        "Book ID: 101\n"
        " Book Title: Ramayana\n"
        " Author Name: Bhimanagouda\n"
        " Publication Year: 2006\n"
    )
    assert book_details(1001, "Atomic habit", "Bob", 2016) == expected_output
