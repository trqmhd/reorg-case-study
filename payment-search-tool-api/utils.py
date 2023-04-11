# Define a function to serialize query results
def serialize_results(results):
    return {
        'items': [result.serialize() for result in results.items],
        'total': results.total,
        'page': results.page,
        'per_page': results.per_page,
        'pages': results.pages,
        'has_prev': results.has_prev,
        'has_next': results.has_next,
        'prev_num': results.prev_num,
        'next_num': results.next_num,
    }