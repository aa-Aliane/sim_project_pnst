import React, { useState } from "react";
import { api } from "../services/api";

// components
import Nav from "../components/Nav";
import Filters from "../Layouts/Filters";
import Interface from "../Layouts/Interface";
import Results from "../Layouts/Results";

const Home = () => {
  return (
    <div>
      <Nav />
      <main>
        <Filters />
        {/* <Interface /> */}
        <Results />
      </main>
    </div>
  );
};

export default Home;
