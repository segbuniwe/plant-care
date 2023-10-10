import { configureStore } from "@reduxjs/toolkit";
import { setupListeners } from "@reduxjs/toolkit/query";
import { plantCareApi } from "./apiSlice";

export const store = configureStore({
    reducer: {
        [plantCareApi.reducerPath]: plantCareApi.reducer,
    },
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware().concat(plantCareApi.middleware),
});

setupListeners(store.dispatch);
