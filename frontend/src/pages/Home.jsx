import React, { useState } from "react";
import { api } from "../services/api";

// components
import Nav from "../components/Nav";

const Home = () => {
  const [suspicious, setSuspicious] = useState();
  const HandleSubmit = () => {
    // api
    //   .post("most_similar/", { query: {content : suspicious} })
    //   .then((res) => console.log(res.data));
    api
      .post("/most_similar/", { content: suspicious })
      .then((res) => console.log(res.data));
  };
  return (
    <div>
      <Nav />
      <textarea
        name=""
        id=""
        cols="30"
        rows="10"
        placeholder="enter suspicious text"
        onChange={(e) => setSuspicious(e.target.value)}
      ></textarea>
      <button onClick={() => HandleSubmit()}>sumbit</button>
      <div className="results"></div>
    </div>
  );
};

export default Home;
