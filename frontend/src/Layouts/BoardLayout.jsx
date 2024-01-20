import React from "react";
import Filters from "../components/Filters"
const BoardLayout = ({ children }) => {
  return (
    <div className="board">
      {/* <Filters /> */}
      <div className="board__main">{children}</div>
    </div>
  );
};

export default BoardLayout;
