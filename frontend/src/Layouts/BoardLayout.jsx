import React from "react";
import Filters from "../components/Filters"
const BoardLayout = ({ children }) => {
  return (
    <>
      <Filters />
      {children}
    </>
  );
};

export default BoardLayout;
