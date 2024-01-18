import React from "react";
import Nav from "../components/Nav";

const MainLayout = ({ children }) => {
  return (
    <div>
      <Nav />
      <main>{children}</main>
    </div>
  );
};

export default MainLayout;
