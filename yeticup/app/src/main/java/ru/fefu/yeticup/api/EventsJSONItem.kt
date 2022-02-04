package ru.fefu.yeticup.api

data class EventsJSONItem(
    val championship_id: Int,
    val championship_name: String,
    val championship_picture: String,
    val date_id: String,
    val description: String,
    val location: String
)