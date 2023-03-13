import React from "react";

const Filter = ({ filter, display, change }) => {
  let title = filter.title;
  let items = filter.items;
  let items_keys = Object.keys(filter.items);

  return (
    <ul className="filter">
      <h4 className="filter__title">
        {display===true && <span className="material-symbols-outlined" onClick={() => change()}>
          arrow_drop_up
        </span>}
        {display===false && <span className="material-symbols-outlined" onClick={() => change()}>
          arrow_drop_down
        </span>}
        {title}
      </h4>
      {items_keys.map((item) => (
        <li className="filter__item" data-display={display}>
          <p>{items[item]}</p>
          <span></span>
        </li>
      ))}
    </ul>
  );
};

export default Filter;
