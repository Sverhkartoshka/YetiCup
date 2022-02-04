package ru.fefu.yeticup.api

data class UserJSON(
    val School: String,
    val age: Int,
    val email: String,
    val first_name: String,
    val last_name: String,
    val location: String,
    val password: String,
    val phone_number: String,
    val second_name: Any,
    val user_id: Int
)