TICKET_SCHEMA = {
    "type" : "object",
    "required" : ["id", "partido", "monto"],
    "properties" : {
        "id" : {"type" : "integer"},
        "partido" : {"type" : "string"},
        "monto" : {"type" : "integer"}
    }
}

TICKET_GUARDADO_SCHEMA = {

    "type" : "object",
    "required" : ["userId", "id", "title", "body"],
    "properties" : {
        "userId" : {"type" : "integer"},
        "id" : {"type" : "integer"},
        "title" : {"type" : "string"},
        "body" : {"type" : "string"}
    }
}