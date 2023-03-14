import { create } from "zustand";
import { range } from "../utils";

export const usePagination = create((set) => ({
  results_per_page: 5,
  nb_pages : 0,
  pages: range(0, 5, 1),
  set_results_per_pages: (nb) => set(() => ({ results_per__pages: nb, pages: range(0, nb, 1) })),
}));
