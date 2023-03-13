import { create } from "zustand";

export const useDropDowns = create((set) => ({
  domains: true,
  switch_domains: () => set((state) => ({ domains: !state.domains })),
  depots: true,
  switch_depots: () => set((state) => ({ depots: !state.depots })),
}));
