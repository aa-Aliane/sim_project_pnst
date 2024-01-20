import React, { useState } from "react";
import { useLanguage } from "../store/LanguageState";
import { api, api_form } from "../services/api";
import { useLayout } from "../store/LayoutState";
import { useModel } from "../store/ModelState";
import { useToggleMenu } from "../store/General";
import { useResultStore } from "../store/ResultState";
import { useNavigate } from "react-router-dom";

const Interface = () => {
  const suspicious = useModel((state) => state.suspicious);
  const multiLang = useModel((state) => state.multiLang);
  const set_suspicious = useModel((state) => state.set_suspicious);
  const set_results = useModel((state) => state.set_results);
  const text = useLanguage((state) => state.text.interface);
  const set_current_layout = useLayout((state) => state.set_current_layout);
  const current_lang = useLanguage((state) => state.current_language);
  const { setTarget } = useResultStore();
  const [fromFile, setFromFile] = useState(false);

  const menu_toggled = useToggleMenu((state) => state.toggle);

  const navigate = useNavigate();

  const handleFileUpload = (event) => {
    const uploadedFile = event.target.files[0];
    set_suspicious(uploadedFile);
    setFromFile(true);

    if (uploadedFile) {
      // Create a new FileReader
      var reader = new FileReader();

      // Define the onload event callback
      reader.onload = function (e) {
        // e.target.result contains the file content
        var fileContent = e.target.result;
        console.log("File Content:", fileContent);
        setTarget(fileContent);
        // You can now do something with the file content
      };

      // Read the file as text (you can use other methods like readAsArrayBuffer for binary files)
      reader.readAsText(uploadedFile);
    } else {
      console.error("No file selected.");
    }
  };

  const HandleSubmit = (event) => {
    event.preventDefault();
    HandlePlagiarismDetection(suspicious);
    k;
  };

  // Handle plagiarism detection
  const HandlePlagiarismDetection = (text) => {
    console.log(text);
    if (typeof text === "string") {
      let data = {
        content: text,
        k: 100,
      };
      api
        .post(`most_similar${!multiLang ? "_standard" : ""}/`, data)
        .then((res) => {
          console.log("🚀 ~ file: Interface.jsx:22 ~ .then ~ res:", res);
          set_suspicious(text);
          set_results(res.data.response);
          set_current_layout("results");
          navigate("results");
        });
    } else {
      let data = new FormData();
      data.append("file", text);
      data.append("k", 100);
      api_form.post("most_similar_file/", data).then((res) => {
        console.log("🚀 ~ file: Interface.jsx:22 ~ .then ~ res:", res);
        set_suspicious(text);
        set_results(res.data.response);
        set_current_layout("results");
        navigate("results");
      });
    }
  };
  return (
    <form
      className="interface"
      onSubmit={HandleSubmit}
      data-opened={menu_toggled}
    >
      <button
        data-display={fromFile}
        data-dir={current_lang === "ar"}
        className="interface__cancel btn btn--cancel"
        onClick={() => {
          set_suspicious("");
          setFromFile(false);
        }}
      >
        <span class="material-symbols-outlined">backspace</span>
      </button>

      {!fromFile && (
        <textarea
          className="interface__text textarea"
          placeholder={text.suspicious}
          onChange={(e) => set_suspicious(e.target.value)}
        ></textarea>
      )}

      {/* <button className="btn btn--check interface__upload">
        
        </button> */}
      {fromFile && <p className="interface__text">{suspicious.name}</p>}
      <div className="flex-container">
        <label
          className="btn btn--check interface__upload"
          htmlFor="file-input"
        >
          <p>
            {text.upload}
            {/* {String(multiLang)} */}
          </p>
          <span class="material-symbols-outlined">picture_as_pdf</span>
        </label>
        <input
          className="interface__upload"
          id="file-input"
          type="file"
          onChange={handleFileUpload}
        />
        <button
          data-enabled={suspicious !== ""}
          className="btn btn--check interface__check"
          type="submit"
        >
          <p>{text.detect}</p>
          <span class="material-symbols-outlined">plagiarism</span>
        </button>
      </div>
    </form>
  );
};

export default Interface;
