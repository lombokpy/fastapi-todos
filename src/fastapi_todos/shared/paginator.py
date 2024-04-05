from typing import Any, List, Tuple
from shared import entity

def paginate_data(total, skip, limit):
    # Calculate page number
    page_number = (skip // limit) + 1
    
    # Calculate total pages
    total_pages = total // limit
    if total % limit != 0:
        total_pages += 1

    return entity.Pagination(
        total_item=total,
        total_page=total_pages,
        page_size=limit,
        curr_page=page_number,
        prev_page=page_number - 1 if page_number > 1 else 0,
        next_page=page_number + 1 if page_number < total_pages else 0,
        has_prev=page_number > 1,
        has_next=page_number < total_pages
    )
    
    

# def paginate_data(
#     data: List[Any], page_size: int, curr_page: int
# ) -> Tuple[List[Any], Pagination]:
#     total_item = len(data)
#     total_page = (
#         total_item + page_size - 1
#     ) // page_size  # Ceiling division to handle partial pages

#     # Calculate start and end indices for slicing the data list
#     start = (curr_page - 1) * page_size
#     end = start + page_size
#     paginated_data = data[start:end]

#     # Set up the Pagination instance
#     pagination_info = Pagination()
#     pagination_info.total_item=total_item,
#     pagination_info.total_page=total_page,
#     pagination_info.page_size=page_size,
#     pagination_info.curr_page=curr_page,
#     pagination_info.prev_page=max(curr_page - 1, 0),
#     pagination_info.next_page=curr_page + 1 if curr_page < total_page else 0,
#     pagination_info.has_prev=curr_page > 1,
#     pagination_info.has_next=curr_page < total_page,

#     return paginated_data, pagination_info
