import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/dist/query";

export const plantCareApi = createApi({
    reducerPath: "plantCareApi",
    baseQuery: fetchBaseQuery({
        baseUrl: process.env.REACT_APP_API_HOST,
    }),
    endpoints: (builder) => ({
        getAccount: builder.query({
            query: () => ({
                url: '/token',
                credentials: "include",
            }),
            transformResponse: (response) => (response ? response.account : null),
            providesTags: ['Account'],
        }),
        login: builder.mutation({
            query: ({ username, password }) => {
                const body = new FormData();
                body.append('username', username);
                body.append('password', password);
                return {
                    url: '/token',
                    method: 'POST',
                    body,
                    credentials: 'include',
                };
            },
            invalidatesTags: ['Account', 'Favorites'],
        }),
        signup: builder.mutation({
            query: (body) => ({
                url: '/api/accounts',
                method: 'POST',
                body,
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                },
            }),
            invalidatesTags: ['Account', 'Favorites'],
        }),
        logout: builder.mutation({
            query: () => ({
                url: '/token',
                method: 'DELETE',
                credentials: 'include',
            }),
            invalidatesTags: ['Account', 'Favorites'],
        }),
        getFavorites: builder.query({
            query: () => ({
                url: '/api/favorites/mine',
                credentials: 'include',
            }),
            transformResponse: (response) => response.favorites,
            providesTags: ['Favorites'],
        }),
        createFavorite: builder.mutation({
            query: (body) => ({
                url: '/api/favorites',
                method: 'POST',
                body,
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                },
            }),
            invalidatesTags: ['Favorites', 'Account'],
        }),
        deleteFavorite: builder.mutation({
            query: (favorite_id) => ({
                url: `api/favorites/${favorite_id}`,
                method: 'DELETE',
                credentials: 'include',
            }),
            invalidatesTags: ['Favorites', 'Account'],
        }),
        getPlants: builder.query({
            query: () => ({
                url: '/api/plants',
                credentials: 'include',
            }),
            transformResponse: (response) => response.plants,
            providesTags: ['Recipes'],
        }),
        getPlantByID: builder.query({
            query: (plant_id) => ({
                url: `/api/plants/${plant_id}`,
                credentials: 'include',
            }),
        }),
    }),
});

export const {
    useGetAccountQuery,
    useLoginMutation,
    useLogoutMutation,
    useSignupMutation,
    useGetFavoritesQuery,
    useCreateFavoriteMutation,
    useDeleteFavoriteMutation,
    useGetPlantsQuery,
    useGetPlantByIDQuery,
} = plantCareApi;
