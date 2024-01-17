import { create } from "zustand";

export const useResultStore = create((set) => ({
  source: {},
  target: "",
  setSource: (source) => set({ source: source }),
  setTarget: (target) => set({ target: target }),
}));
