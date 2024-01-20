import React from "react";
import Nav from "../components/Nav";

const MainLayout = ({ children }) => {
  return (
    <>
      <Nav />
      <main className="main-layout">{children}</main>
    </>
  );
};

export default MainLayout;
