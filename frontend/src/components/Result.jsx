import React from "react";

const Result = ({ result }) => {
  return (
    <div className="result">
      <div className="result__title">{result.title}</div>
      <div className="result__rate">{result.rate}%</div>
      <button className="btn btn--deep">deep search</button>
    </div>
  );
};

export default Result;
