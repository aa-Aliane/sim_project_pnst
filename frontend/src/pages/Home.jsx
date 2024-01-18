import React, { useState } from "react";
// import { api } from "../services/api";
// import { useLayout } from "../store/LayoutState";

// // components
// import Nav from "../components/Nav";
// import Filters from "../components/Filters";
// import Interface from "./Interface";
// import Results from "../Layouts/Results";
// import About from "./About";
// import Details from "../Layouts/Details";

const Home = () => {
  const current_layout = useLayout((state) => state.current_layout);
  return (
    <div>
      {/* <Nav />
      <main>
        {(current_layout === "interface" ||
          current_layout === "results" ||
          current_layout === "details") && <Filters />}
        {current_layout === "interface" && <Interface />}
        {current_layout === "results" && <Results />}
        {current_layout === "about" && <About />}
        {current_layout === "details" && <Details />}
      </main> */}
    </div>
  );
};

export default Home;
