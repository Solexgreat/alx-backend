def index_range(page, page_size):
    i = page_size
    i = page_size * page
    page = i - page_size
    page_size = i
    result = (page, page)
    return(result)