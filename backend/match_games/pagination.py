from math import ceil


def count_items(items):
    return {'count': len(items)}


def count_pages(limit):
    def inner(pagination):
        new_pagination = pagination.copy()
        count = new_pagination['count']
        new_pagination['pages'] = ceil(count / limit)
        return new_pagination
    return inner


def verify_has_previous(current_page):
    def inner(pagination):
        new_pagination = pagination.copy()
        pages = new_pagination['pages']
        new_pagination['has_previous'] = current_page - 1 != 0
        return new_pagination
    return inner


def verify_has_next(current_page):
    def inner(pagination):
        new_pagination = pagination.copy()
        pages = new_pagination['pages']
        new_pagination['has_next'] = current_page + 1 <= pages
        return new_pagination
    return inner


def create_pagination(current_page, items):
    return (
        verify_has_next(current_page)(
            verify_has_previous(current_page)(
                count_pages(8)(
                    count_items(items)
                )
            )
        )
    )
