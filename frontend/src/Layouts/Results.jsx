import React from "react";

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
];

const Results = () => {
  return (
    <div className="results__container">
      <Pagination pages={pages} />
      <ul className="results">
        {results.map((r) => (
          <li className="results__item">{r.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default Results;
