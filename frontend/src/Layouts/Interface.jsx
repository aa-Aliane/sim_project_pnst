import React, { useState } from "react";
import { useLanguage } from "../store/LanguageState";
import { api } from "../services/api";
import { useLayout } from "../store/LayoutState";
import { useModel } from "../store/ModelState";

const Interface = () => {
  const suspicious = useModel((state) => state.suspicious);
  const set_suspicious = useModel((state) => state.set_suspicious);
  const set_results = useModel((state) => state.set_results);
  const text = useLanguage((state) => state.text.interface);
  const set_current_layout = useLayout((state) => state.set_current_layout);

  // Handle plagiarism detection
  const HandlePlagiarismDetection = (text) => {
    console.log(
      "🚀 ~ file: Interface.jsx:16 ~ HandlePlagiarismDetection ~ text:",
      text
    );
    api
      .post("most_similar/", {
        content: text,
        k: 100,
      })
      .then((res) => {
        console.log("🚀 ~ file: Interface.jsx:22 ~ .then ~ res:", res);
        set_suspicious(text);
        set_results(res.data.response);
        set_current_layout("results");
      });
  };
  return (
    <div className="interface">
      <textarea
        className="textarea"
        placeholder={text.suspicious}
        onChange={(e) => set_suspicious(e.target.value)}
      ></textarea>
      <button className="btn btn--check interface__upload">
        <p>{text.upload}</p>
        <span class="material-symbols-outlined">picture_as_pdf</span>
      </button>
      <button
        className="btn btn--check interface__check"
        onClick={() => HandlePlagiarismDetection(suspicious)}
      >
        <p>{text.detect}</p>
        <span class="material-symbols-outlined">plagiarism</span>
      </button>
    </div>
  );
};

export default Interface;
