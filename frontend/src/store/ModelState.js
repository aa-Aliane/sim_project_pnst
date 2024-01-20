import { create } from "zustand";

export const useModel = create((set) => ({
  multiLang: true,
  suspicious: "",
  set_suspicious: (text) => set(() => ({ suspicious: text })),
  results: [],
  set_results: (results) => set(() => ({ results: results })),
  switchMultiLang: () => set((state) => ({ multiLang: !state.multiLang })),
}));
