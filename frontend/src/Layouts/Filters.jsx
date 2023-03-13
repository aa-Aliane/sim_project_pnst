import React from "react";
import { useLanguage } from "../store/LanguageState";
import { useDropDowns } from "../store/clickState";
import Filter from "../components/filter";

const Filters = () => {
  const domains = useLanguage((state) => state.text.filters.domains);
  const show_domains = useDropDowns((state) => state.domains);
  const switch_domains = useDropDowns((state) => state.switch_domains);
  const depots = useLanguage((state) => state.text.filters.depots);
  const show_depots = useDropDowns((state) => state.depots);
  const switch_depots = useDropDowns((state) => state.switch_depots);

  console.log(depots);
  return (
    <ul className="filters">
      <li>
        <Filter
          filter={domains}
          display={show_domains}
          change={switch_domains}
        />
      </li>
      <li>
        <Filter filter={depots} display={show_depots} change={switch_depots} />
      </li>
    </ul>
  );
};

export default Filters;
