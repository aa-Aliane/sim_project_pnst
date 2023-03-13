import React from "react";
import { useLanguage } from "../store/LanguageState";

const Nav = () => {
  //   useLanguage methods and variables
  const lang = useLanguage((state) => state.current_language);
  const languages = useLanguage((state) => state.languages);
  const text = useLanguage((state) => state.text.nav);
  const change_language = useLanguage((state) => state.change_language);

  const HandleLanguageChange = (l) => {
    console.log("🚀 ~ file: Nav.jsx:12 ~ HandleLanguageChange ~ l:", l);

    change_language(l);
  };
  return (
    <nav className="nav">
      <ul className="nav__items">
        <li>{text.home}</li>
        <li>{text.about}</li>
        <li>{text.api}</li>
      </ul>
      <h3 className="nav__title">{text.title}</h3>
      {/* language settings */}
      <div>
        <select name="" id="">
          {Object.keys(languages).map((l) => {
            console.log(l);
            if (lang == l) {
              return (
                <option
                  value="{l}"
                  selected
                  onClick={() => HandleLanguageChange(l)}
                >
                  {l}
                </option>
              );
            }
            return (
              <option value="{l}" onClick={() => HandleLanguageChange(l)}>
                {l}
              </option>
            );
          })}
        </select>
      </div>
    </nav>
  );
};

export default Nav;
