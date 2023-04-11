import { Fragment, useEffect, useState } from "react";
import collect from "collect.js";
import Header from "components/Header";
import TheAsyncSelect from "components/TheAsyncSelect";
import getPaginate from "utils/get-paginate";
import { http } from "utils/http";

export default function Index() {
  const [theData, setTheData] = useState([] as any);
  const [selectedOption, setSelectedOption] = useState(null as any);
  const [pagination, setPagination] = useState({} as any);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    if (selectedOption !== null) {
      fetchDataById();
    } else {
      fetchData();
    }
  }, [selectedOption]);

  /**
   * Fetch typeahead data
   * @param {number} page - page number.
   * @returns {void}
   */
  function fetchData(page: number = 1): void {
    setIsLoading(true);
    http
      .get(`/typeahead?page=${page}&query`)
      .then((response: any) => {
        setTheData(response.data.items);
        let { data } = response;
        let paginationData = getPaginate(data);
        setPagination(paginationData);
        setIsLoading(false);
      })
      .catch((error: any) => {
        setIsLoading(false);
      });
  }

  /**
   * Fetch specific physician data.
   */
  function fetchDataById() {
    setIsLoading(true);
    http
      .get(`/search/${selectedOption?.recipient_id}`)
      .then((response: any) => {
        setTheData(response.data?.items ?? []);
        let { data } = response;
        let paginationData = getPaginate(data);
        setPagination(paginationData);
        setPagination(paginationData);
        setIsLoading(false);
      })
      .catch((error: any) => {
        setIsLoading(false);
      });
  }

  /**
   * Change the page.
   *
   * @param {string} type
   * @returns {void}
   */
  function changePage(type: string): void {
    if (type === "prev" && pagination?.previous_page) {
      fetchData(pagination.previous_page);
    } else if (type === "next" && pagination.next_page) {
      fetchData(pagination.next_page);
    }
  }

  /**
   * Asycn load typeahead.
   *
   * @param search
   * @param prevOptions
   * @param {any} param2
   * @returns
   */
  const loadOptions = async (search: any, prevOptions: any, { page }: any) => {
    if (search.length < 1) {
      return { options: [], hasMore: false };
    }
    try {
      let response: any = await http.get("/typeahead", {
        params: {
          query: search,
          page: page,
        },
      });

      const collection = collect(response.data?.items);
      let uniqueData = collection.unique("recipient_id");
      console.log(uniqueData.all());

      let data = {
        options: uniqueData.all(),
        hasMore: response.data.has_next,
        additional: {
          page: page + 1,
        },
      };
      return data;
    } catch (error) {
      return { options: [], hasMore: false };
    }
  };

  function theOnChange(data: any) {
    setSelectedOption(data);
    console.log(data)
  }

  function exportData() {
    if (selectedOption) {
      http
      .get(`/export/${selectedOption.recipient_id}`, { responseType: "blob" })
      .then((response: any) => {
        const url = window.URL.createObjectURL(new Blob([response.data]));

        // Create a link and click it to download the file
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", "data.xlsx");
        document.body.appendChild(link);
        link.click();
      }).catch((error: any) => {
        console.log(error)
      });
    } else {
      alert("Filter some data then try to export")
    }
  }

  function importData() {
    alert("import data");
  }

  return (
    <>
      <div className="min-h-full">
        <Header />
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 mt-4">
          <div className="px-4 sm:px-6 lg:px-8">
            <div className="sm:flex sm:items-center">
              <div className="sm:flex-auto">
                <div className=" w-1/2 ">
                  <TheAsyncSelect
                    placeholder="Type Here to Search..."
                    getOptionLabel={(item: any) =>
                      `${item.physcian_first_name}  ${item.physcian_last_name}  (${item.recipient_id})`
                    }
                    getOptionValue={(item: any) => item.recipient_id}
                    onChange={(option: any) => theOnChange(option)}
                    defaultOptions
                    loadOptions={loadOptions}
                    isClearable={true}
                    additional={{
                      page: 1,
                    }}
                  />
                </div>
              </div>
              <div className="mt-4 sm:ml-16 sm:mt-0 sm:flex-none flex ">
                {/* <button
                  type="button"
                  className=" mr-2 block rounded-md bg-green-600 px-3 py-2 text-center text-sm font-semibold text-white shadow-sm hover:bg-green-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-green-600"
                  onClick={() => importData()}
                >
                  Import
                </button> */}

                <button
                  type="button"
                  className="block rounded-md bg-indigo-600 px-3 py-2 text-center text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                  onClick={() => exportData()}
                >
                  Export
                </button>
              </div>
            </div>
            {isLoading ? (
              <div className="flex items-center justify-center h-96">
                <svg
                  className="animate-spin h-16 w-16 text-gray-400"
                  viewBox="0 0 24 24"
                >
                  <circle
                    className="opacity-25"
                    cx="12"
                    cy="12"
                    r="10"
                    stroke="currentColor"
                    strokeWidth="4"
                  />
                  <path
                    className="opacity-75"
                    fill="currentColor"
                    d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm8 8a8 8 0 008-8h4a12 12 0 01-12 12v-4zm0-16a8 8 0 018 8H8a12 12 0 01-12-12v4z"
                  />
                </svg>
              </div>
            ) : (
              <div className="mt-8 flow-root">
                <div className="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
                  <div className="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
                    <div className="overflow-hidden shadow ring-1 ring-black ring-opacity-5 sm:rounded-lg">
                      <table className="min-w-full divide-y divide-gray-300">
                        <thead className="bg-gray-50">
                          <tr>
                            <th
                              scope="col"
                              className="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6"
                            >
                              Physican Name
                            </th>
                            {/* <th
                              scope="col"
                              className="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6"
                            >
                              Physican Speciality
                            </th> */}
                            <th
                              scope="col"
                              className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                            >
                              Record ID
                            </th>
                            <th
                              scope="col"
                              className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                            >
                              Payment Amount
                            </th>
                            <th
                              scope="col"
                              className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                            >
                              Payment Info
                            </th>
                          </tr>
                        </thead>
                        <tbody className="divide-y divide-gray-200 bg-white">
                          {theData.map((item: any) => (
                            <tr key={item.id}>
                              <td className="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6">
                                {item.physcian_first_name}{" "}
                                {item?.physcian_last_name ?? ""} - (
                                {item.recipient_id})
                              </td>
                              {/* <td className=" px-3 py-4 text-sm text-gray-500 break-words">
                                {item.physcian_specialty}
                              </td> */}
                              <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                                {item.record_id}
                              </td>
                              <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                                {parseFloat(
                                  item.total_amount_of_Payment
                                ).toFixed(2)}
                              </td>
                              <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                                <p>id: {item.payment_id}</p>
                                <p>name: {item.payment_name}</p>
                                <p>date: {item.date_of_payment}</p>
                                <p>{item.form_of_payment}</p>
                                <p>
                                  {item?.payment_state} {item.payment_country}
                                </p>
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
            )}
            <div>
              <nav
                className="flex items-center justify-between border-t border-gray-200 bg-white px-4 py-3 sm:px-6"
                aria-label="Pagination"
              >
                <div className="hidden sm:block">
                  <p className="text-sm text-gray-700">
                    Showing{" "}
                    <span className="font-medium">{pagination.from}</span> to{" "}
                    <span className="font-medium">{pagination?.to}</span> of{" "}
                    <span className="font-medium">{pagination?.total}</span>{" "}
                    results
                  </p>
                </div>
                <div className="flex flex-1 justify-between sm:justify-end">
                  <button
                    className="relative inline-flex items-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus-visible:outline-offset-0"
                    onClick={() => changePage("prev")}
                  >
                    Previous
                  </button>
                  <button
                    className="relative ml-3 inline-flex items-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus-visible:outline-offset-0"
                    onClick={() => changePage("next")}
                  >
                    Next
                  </button>
                </div>
              </nav>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
