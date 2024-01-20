import React from "react";
import { useLanguage } from "../store/LanguageState";
import { useResultStore } from "../store/ResultState";
import { useLayout } from "../store/LayoutState";
import { useNavigate } from "react-router-dom";
import { useModel } from "../store/ModelState";
import { api } from "../services/api";



const Result = ({ result }) => {
  const current_lang = useLanguage((state) => state.current_language);
  const text = useLanguage((state) => state.text.result);

  const { setResult } = useResultStore();
  const { set_current_layout } = useLayout();
  const { suspicious } = useModel();

  const navigate = useNavigate();

  const handleResultDisplay = (doc_id) => {
    console.log(doc_id)
    set_current_layout("details");
    api
      .post("compare", { source: doc_id, target: suspicious })
      .then((response) => {
        console.log(response);
        setResult(response.data.similarity_rates);
      });

    navigate("/details");
  };

  return (
    <div className="result">
      <div data-rlang={result.lang} className="result__title">
        <a href={result.url} target="_blank">
          {result.title}
        </a>
      </div>
      <div data-dir={current_lang === "ar"} className="result__rate">
        {result.rate}%
      </div>
      <ul data-rlang={result.lang} className="result__authors">
        <li className="result__authors__author">{result.author}</li>
      </ul>
      <div data-dir={current_lang === "ar"} className="result__deep">
        <button className="btn btn--deep" onClick={() => handleResultDisplay(result.doc_id)}>
          {text.deep}
        </button>
      </div>
    </div>
  );
};

export default Result;
