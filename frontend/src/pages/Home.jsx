import React, { useState } from "react";
import { api } from "../services/api";

// components
import Nav from "../components/Nav";
import Filters from "../Layouts/Filters";
import Interface from "../Layouts/Interface";

const Home = () => {
  return (
    <div>
      <Nav />
      <main>
        <Filters />
        <Interface />
      </main>
    </div>
  );
};

export default Home;
