import React, { useState, useEffect } from "react";
import { Pagination, PaginationInfo } from "../components/Pagination";
import { usePagination } from "../store/PaginationState";

const results = [
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-ggg-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-bbb-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-hhhh-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-zzzz-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-tttt-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-tttt-ccc", author: "Amine Aliane", date: "2020" },
  { title: "aaa-tttt-ccc", author: "Amine Aliane", date: "2020" },
];

const Results = () => {
  const current_page = usePagination((state) => state.current_page);
  const results_per_page = usePagination((state) => state.results_per_page);
  const [start, setStart] = useState(0);
  const [end, setEnd] = useState(Math.min(results.length, 10));

  useEffect(() => {
    setStart(current_page * results_per_page - results_per_page);
    setEnd(Math.min(current_page * results_per_page, results.length));
  }, [, current_page, results_per_page]);
  return (
    <div className="results__container">
      <PaginationInfo nb_results={results.length} />
      <ul className="results">
        {results.slice(start, end).map((r) => (
          <li className="results__item">{r.title}</li>
        ))}
      </ul>
      <Pagination />
    </div>
  );
};

export default Results;
