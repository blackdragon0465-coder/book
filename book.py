def book_details(id,tittle,name,year):
    result = (
        f"Book ID: {id}\n"
        f" Book Title: {tittle}\n"
        f" Author Name: {name}\n"
        f" Publication Year: {year}\n"
    )
    return result
if __name__ == "__main__":
    id = 101
    tittle = "Ramayana"
    name = "Bhimanagouda"
    year = 2006

    print(book_details(1001,"Atomic habit","Bob",2016))
    
