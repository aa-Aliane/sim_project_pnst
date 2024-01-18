import { create } from "zustand";

export const useResultStore = create((set) => ({
  source: {},
  target: "",
  result: [],
  setSource: (source) => set({ source: source }),
  setTarget: (target) => set({ target: target }),
  setResult: (result) => set({ result: result }),
}));
