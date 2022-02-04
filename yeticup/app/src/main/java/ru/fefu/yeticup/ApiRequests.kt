package ru.fefu.yeticup

import retrofit2.http.GET
import retrofit2.Call
import ru.fefu.yeticup.api.UserJSON

interface ApiRequests {

    @GET(value = "api/profile/5")
    fun getUser(): Call<UserJSON>

}