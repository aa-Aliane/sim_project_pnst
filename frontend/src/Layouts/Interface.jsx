import React from "react";
import { useLanguage } from "../store/LanguageState";

const Interface = () => {
  const text = useLanguage((state) => state.text.interface);
  return (
    <div className="interface">
      {/* <textarea
        className="textarea"
        placeholder={text.suspicious}
      ></textarea> */}

      <button className="btn btn--check interface__upload">
        <p>{text.upload}</p>
        <span class="material-symbols-outlined">picture_as_pdf</span>
      </button>
      <button className="btn btn--check interface__check">
        <p>{text.detect}</p>
        <span class="material-symbols-outlined">plagiarism</span>
      </button>
    </div>
  );
};

export default Interface;
