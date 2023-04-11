/**
 * Generate pagination data.
 * 
 * @param {object} data 
 * @returns {object}
 */
function getPaginate(data: any): {} {
  let paginationData = {
    has_next: data.has_next,
    has_previous: data.has_previous,
    page: data.page,
    total_page: data.pages,
    previous_page: data?.prev_num ?? null,
    next_page: data?.next_num ?? null,
    per_page: data.per_page,
    total: data.total,
    to: parseInt(data.page) * parseInt(data.per_page),
    from:
      parseInt(data.page) * parseInt(data.per_page) -
      parseInt(data.per_page),
  };

  return paginationData
}

export default getPaginate