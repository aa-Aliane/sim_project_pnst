import React, { useState } from "react";
import { api } from "../services/api";
import { useLayout } from "../store/LayoutState";

// components
import Nav from "../components/Nav";
import Filters from "../Layouts/Filters";
import Interface from "../Layouts/Interface";
import Results from "../Layouts/Results";

const Home = () => {
  const current_layout = useLayout((state) => state.current_layout);
  return (
    <div>
      <Nav />
      <main>
        <Filters />
        {current_layout === "interface" && <Interface />}
        {current_layout === "results" && <Results />}
      </main>
    </div>
  );
};

export default Home;
