import React from "react";

const Result = ({ result }) => {
  return (
    <div className="result">
      <div className="result__title">
        <a href={result.url} target="_blank">
          {result.title}
        </a>
      </div>
      <div className="result__rate">{result.rate}%</div>
      <div className="result__deep">
        <button className="btn btn--deep">deep search</button>
      </div>
    </div>
  );
};

export default Result;
